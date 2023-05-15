import unittest

from data_models import IncorrectTranscriptError, WordToken, MyTranscription, RemoveOp, AddOp, ReplaceOp

test_transcription = MyTranscription(
    text=[WordToken(word='hi', word_id='wo1', ts_start=0, ts_end=10, speaker='John'),
          WordToken(word='I', word_id='wo2', ts_start=13, ts_end=23, speaker='John'),
          WordToken(word='am', word_id='wo3', ts_start=27, ts_end=35, speaker='John'),
          WordToken(word='john', word_id='wo4', ts_start=40, ts_end=50, speaker='John'),
          WordToken(word='and', word_id='wo5', ts_start=52, ts_end=64, speaker='Mary'),
          WordToken(word='I', word_id='wo6', ts_start=67, ts_end=77, speaker='Mary'),
          WordToken(word='am', word_id='wo7', ts_start=79, ts_end=85, speaker='Mary'),
          WordToken(word='mary', word_id='wo8', ts_start=90, ts_end=93, speaker='Mary')

          ],
    speakers=['John', 'Mary'],
    audio_file_id='au123456',
    transcript_id='tr123456',
    ts_end=93,
)


class TestWordToken(unittest.TestCase):

    def test_word_token_creation(self) -> None:
        word_token = WordToken(word='test', word_id='test_id', ts_start=0, ts_end=10, speaker='John')
        self.assertEqual(word_token.word, 'test')
        self.assertEqual(word_token.word_id, 'test_id')
        self.assertEqual(word_token.ts_start, 0)
        self.assertEqual(word_token.ts_end, 10)
        self.assertEqual(word_token.speaker, 'John')

    def test_eq(self) -> None:
        word_token_a = WordToken(word='test', word_id='id1', ts_start=0, ts_end=10, speaker='John')
        word_token_b = WordToken(word='test', word_id='id2', ts_start=0, ts_end=10, speaker='John')
        self.assertEqual(word_token_a, word_token_b)


class TestMyTranscription(unittest.TestCase):

    def test_my_transcription_creation(self) -> None:
        self.assertEqual(len(test_transcription.text), 8)
        self.assertEqual(test_transcription.ts_end, 93)
        self.assertEqual(len(test_transcription.speakers), 2)
        self.assertEqual(test_transcription.speakers[0], 'John')
        self.assertEqual(test_transcription.speakers[1], 'Mary')
        self.assertEqual(test_transcription.audio_file_id, 'au123456')
        self.assertEqual(test_transcription.transcript_id, 'tr123456')
        self.assertEqual(test_transcription.ts_end, 93)

    def test_eq(self) -> None:
        test_transcription_1 = MyTranscription(
            text=[WordToken(word='hi', word_id='wo1', ts_start=0, ts_end=10, speaker='John'),
                  WordToken(word='hi', word_id='wo2', ts_start=13, ts_end=23, speaker='Mary')],
            speakers=['John', 'Mary'],
            audio_file_id='au123456',
            transcript_id='tr123456',
            ts_end=93
        )
        test_transcription_2 = MyTranscription(
            text=[WordToken(word='hi', word_id='wo1', ts_start=0, ts_end=10, speaker='John'),
                  WordToken(word='hi', word_id='wo2', ts_start=13, ts_end=23, speaker='Mary')],
            speakers=['Mary', 'John'],
            audio_file_id='au123456',
            transcript_id='tr123456',
            ts_end=93
        )
        self.assertEqual(test_transcription_1, test_transcription_2)


class Test_EditOperationBase(unittest.TestCase):

    def test_execute_incorrect_transcript(self) -> None:
        edit_op = AddOp(transcript_id='tr78910', op_id='op1234', word='bye', ts_start=100, ts_end=120,
                        speaker='Mary')
        with self.assertRaises(IncorrectTranscriptError):
            edit_op.execute(test_transcription)


class TestRemoveOp(unittest.TestCase):

    def test_execute_remove_op(self) -> None:
        remove_op = RemoveOp(transcript_id='tr123456', op_id='op123', word_id='wo2')
        updated_transcription = remove_op.execute(test_transcription)

        self.assertEqual(len(updated_transcription.text), len(test_transcription.text) - 1)
        removed_word = next((word for word in test_transcription.text if word.word_id == remove_op.word_id), None)
        ground_truth_duration = removed_word.ts_end - removed_word.ts_start
        self.assertEqual(updated_transcription.ts_end, test_transcription.ts_end - ground_truth_duration)
        self.assertEqual(updated_transcription.text[1].word_id, test_transcription.text[2].word_id)


class TestAddOp(unittest.TestCase):
    def test_execute_add_op(self) -> None:
        add_op = AddOp(transcript_id='tr123456', op_id='op1234', word='nice', ts_start=86, ts_end=90,
                       speaker='Mary')

        updated_transcription = add_op.execute(test_transcription)

        # Check if the text field of the resulting transcription object has the correct length
        self.assertEqual(len(updated_transcription.text), len(test_transcription.text) + 1)

        # Check if the new WordToken object was correctly inserted into the text field
        self.assertEqual(updated_transcription.text[7].word, add_op.word)
        self.assertEqual(updated_transcription.text[7].ts_start, add_op.ts_start)
        self.assertEqual(updated_transcription.text[7].ts_end, add_op.ts_end)
        self.assertEqual(updated_transcription.text[7].speaker, add_op.speaker)

        # Check if the timestamps of the other WordToken objects were correctly updated
        self.assertEqual(updated_transcription.text[8].ts_start,
                         test_transcription.text[7].ts_start + add_op.ts_end - add_op.ts_start)
        self.assertEqual(updated_transcription.speakers, test_transcription.speakers)

        # Check if the audio_file_id field of the resulting transcription object is unchanged
        ground_truth_duration = add_op.ts_end - add_op.ts_start
        self.assertEqual(updated_transcription.ts_end, test_transcription.ts_end + ground_truth_duration)

        # Check if the transcript_id field of the resulting transcription object is unchanged
        self.assertEqual(updated_transcription.transcript_id, updated_transcription.transcript_id)


class TestReplaceOp(unittest.TestCase):

    def test_replace_word_token(self) -> None:
        replace_op = ReplaceOp(transcript_id='tr123456', op_id="op1235", replaced_word_id="wo4",
                               new_word="juan", new_ts_end=53, speaker="John")
        updated_transcription = replace_op.execute(test_transcription)

        self.assertEqual(len(updated_transcription.text), len(test_transcription.text))

        # Check if the new WordToken object was correctly inserted into the text field
        self.assertEqual(updated_transcription.text[3].word, replace_op.new_word)
        self.assertEqual(updated_transcription.text[3].ts_start, test_transcription.text[3].ts_start)
        self.assertEqual(updated_transcription.text[3].ts_end, replace_op.new_ts_end)
        self.assertEqual(updated_transcription.text[3].speaker, replace_op.speaker)

        # Check if the transcript_id field of the resulting transcription object is unchanged
        self.assertEqual(updated_transcription.transcript_id, updated_transcription.transcript_id)


if __name__ == '__main__':
    unittest.main()
