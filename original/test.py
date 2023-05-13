import asyncio
from typing import Dict, List, Optional, Tuple
from data_models import MyEditOperation, MyTranscription
from transcription_api import (
    Audio,
    EditLog,
    MockTranscriptionAPI,
)

# TODO (Task 3) implement
transcribe_test_params: Dict[Audio, MyTranscription] = {}
edit_test_params: List[Tuple[MyTranscription, EditLog, MyTranscription]] = {}
store_test_params: List[Tuple[str, MyTranscription, List[Tuple[EditLog, bool]], MyTranscription]] = {}


async def run_test():
    # TODO (Task 4 - optional)

    transcription_api = MockTranscriptionAPI()

    for audio, expected_transcript in transcribe_test_params.items():
        assert expected_transcript == transcription_api.transcribe(audio)

    for origin_transcript, edit_log, expected_transcript in edit_test_params:
        edited_transcript = transcription_api.edit(origin_transcript, edit_log)
        assert edited_transcript == expected_transcript

    for uid, initial_transcript, edit_logs_with_status, expected_transcript in edit_test_params:
        transcription_api.store(initial_transcript)
        curr_transcript = initial_transcript
        last_finished = initial_transcript
        for edit_log, is_partial in edit_logs_with_status:
            curr_transcript = transcription_api.edit(
                transcript=curr_transcript, edit_log=edit_log
            )
            await transcription_api.store(transcript=curr_transcript, uid=uid)

            if not is_partial:
                last_finished = curr_transcript
        assert transcription_api.get_last_finished(uid=uid) == expected_transcript
        assert last_finished == expected_transcript


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_test())
