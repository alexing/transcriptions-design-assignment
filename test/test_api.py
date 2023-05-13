import os
import unittest

from typing import List, Tuple

from asyncio import create_task, gather, sleep, run
from data_models import MyTranscription
from db_utils import DB_FILE
from hardcoded_transcriptions import dummy_audios, dummy_transcriptions
from test_data.edit_logs import edit_log_1_tr_a, edit_log_1_tr_b, edit_log_1_tr_c, edit_log_2_tr_a, edit_log_2_tr_b, \
    edit_log_2_tr_c, edit_log_3_tr_a
from test_data.updated_transcriptions import integration_test_transcription_1, integration_test_transcription_4, \
    updated_transcription_1a, updated_transcription_1b, updated_transcription_1c, updated_transcription_2a, \
    updated_transcription_2b
from transcription_api import Audio, EditLog, MockTranscriptionAPI


async def mock_stuck_store(**kwargs):
    print('awaiting 15 seconds...')
    await sleep(15)
    print('store timed out!')


async def run_async_test_store(transcription_api: MockTranscriptionAPI):
    # store_test_params contains a specific uid, an initial_transcript, a list of edit logs with a boolean
    # specifying if it was successful or not and the expected result transcript.
    store_test_params: List[Tuple[str, MyTranscription, List[Tuple[EditLog, bool]], MyTranscription]] = [

        ('alex', dummy_transcriptions['a'], [(edit_log_1_tr_a, True), (edit_log_3_tr_a, False)],
         integration_test_transcription_1),  # 2nd update doesnt go through
        ('micaela', dummy_transcriptions['b'], [(edit_log_1_tr_b, False)], dummy_transcriptions['b']),  # no update
        ('juan', dummy_transcriptions['c'], [(edit_log_1_tr_c, True), (edit_log_2_tr_c, True)],
         integration_test_transcription_4)  # 2 updates go through correctly
    ]

    for uid, initial_transcript, edit_logs_with_status, expected_transcript in store_test_params:
        # Here we'll simulate some possible scenarios where a store procedure can go wrong
        await transcription_api.store(initial_transcript, uid)
        curr_transcript = initial_transcript
        last_finished = initial_transcript
        tasks = []
        for edit_log, store_successful in edit_logs_with_status:
            curr_transcript = transcription_api.edit(transcript=curr_transcript, edit_log=edit_log)
            # let's schedule store tasks
            if store_successful:
                tasks.append(create_task(transcription_api.store(transcript=curr_transcript, uid=uid)))
                last_finished = curr_transcript
            else:
                tasks.append(create_task(mock_stuck_store(transcript=curr_transcript, uid=uid)))  # if store gets stuck!
        await sleep(5)  # more simulation: sleep 5 seconds just to allow at least one of the saves to go through.
        assert transcription_api.get_last_finished(uid=uid) == expected_transcript
        assert last_finished == expected_transcript
        await gather(*tasks)


class TestTranscriptionApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.transcription_api = MockTranscriptionAPI()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)

    def test_transcribe(self):
        transcribe_test_params: List[Tuple[Audio, MyTranscription]] = [
            (dummy_audios['a'], dummy_transcriptions['a']),
            (dummy_audios['b'], dummy_transcriptions['b']),
            (dummy_audios['c'], dummy_transcriptions['c'])
        ]
        for audio, expected_transcript in transcribe_test_params:
            self.assertTrue(expected_transcript == self.transcription_api.transcribe(audio))

    def test_edit(self):
        edit_test_params: List[Tuple[MyTranscription, EditLog, MyTranscription]] = [
            (dummy_transcriptions['a'], edit_log_1_tr_a, updated_transcription_1a),
            (dummy_transcriptions['a'], edit_log_2_tr_a, updated_transcription_2a),
            (dummy_transcriptions['b'], edit_log_1_tr_b, updated_transcription_1b),  # removes 1 speaker
            (dummy_transcriptions['b'], edit_log_2_tr_b, updated_transcription_2b),
            (dummy_transcriptions['c'], edit_log_1_tr_c, updated_transcription_1c)
        ]
        for origin_transcript, edit_log, expected_transcript in edit_test_params:
            edited_transcript = self.transcription_api.edit(origin_transcript, edit_log)
            assert edited_transcript == expected_transcript

    def test_integration_store(self):
        run(run_async_test_store(self.transcription_api))

    async def test_marked_as_stored(self):
        edited_transcript = self.transcription_api.edit(dummy_transcriptions['a'], edit_log_2_tr_a)
        await self.transcription_api.store(transcript=edited_transcript, uid='alex')
        self.assertTrue(edited_transcript.stored)


if __name__ == '__main__':
    unittest.main()
