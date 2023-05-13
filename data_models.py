import random

from abc import ABC, abstractmethod
from copy import deepcopy
from dataclasses import dataclass
from typing import List


class IncorrectTranscriptError(Exception):
    pass


class TranscriptionNotPossible(Exception):
    pass


def generate_mock_id(id_for_type: str) -> str:
    """This is a mock function to get an id, probably would be automatic with a DB ORM"""
    hash = str(random.getrandbits(128))
    return f"{id_for_type[:2]}{hash[:10]}"


SILENCE_TOKEN = "<...>"


@dataclass
class WordToken:
    word: str
    word_id: str
    ts_start: int
    ts_end: int
    speaker: str

    def __eq__(self, other):
        if not isinstance(other, WordToken):
            return False
        return \
            self.word == other.word and \
            self.ts_start == other.ts_start and \
            self.ts_end == other.ts_end and \
            self.speaker == other.speaker


@dataclass
class MyTranscription:
    text: List[WordToken]
    speakers: List[str]
    audio_file_id: str
    transcript_id: str
    ts_end: int
    stored: bool = False

    def add_speaker(self, speaker: str) -> None:
        if speaker not in self.speakers:
            self.speakers.append(speaker)

    def remove_speaker(self, speaker: str) -> None:
        if speaker in self.speakers:
            self.speakers.remove(speaker)

    def __eq__(self, other):
        if not isinstance(other, MyTranscription):
            return False
        return \
            self.text == other.text and \
            sorted(self.speakers) == sorted(other.speakers) and \
            self.audio_file_id == other.audio_file_id and \
            self.transcript_id == other.transcript_id and \
            self.ts_end == other.ts_end


@dataclass
class _EditOperationBase(ABC):
    transcript_id: str
    op_id: str

    @abstractmethod
    def execute(self, transcript: MyTranscription) -> MyTranscription:
        """This would be a good place to add validations"""
        if transcript.transcript_id != self.transcript_id:
            raise IncorrectTranscriptError(f'This op ({self.op_id}) belongs to transcript {self.transcript_id}.')

        return deepcopy(transcript)  # if not the original transcript will be modified by reference


@dataclass
class RemoveOp(_EditOperationBase):
    word_id: str
    op_type: str = 'remove'

    def execute(self, original_transcript: MyTranscription) -> MyTranscription:
        transcript = super().execute(original_transcript)
        index = next((index for (index, word) in enumerate(transcript.text) if word.word_id == self.word_id), None)
        popped_word = transcript.text.pop(index)
        duration = popped_word.ts_end - popped_word.ts_start
        for i in range(index, len(transcript.text)):
            a_word_token = transcript.text[i]
            a_word_token.ts_start = a_word_token.ts_start - duration
            a_word_token.ts_end = a_word_token.ts_end - duration
            transcript.text[i] = a_word_token
        transcript.ts_end = transcript.text[-1].ts_end

        # in case they remove everything from one speaker
        transcript.speakers = list(set([word.speaker for word in transcript.text]))

        return transcript


@dataclass
class AddOp(_EditOperationBase):
    word: str
    ts_start: int
    ts_end: int
    speaker: str
    op_type: str = 'add'

    def execute(self, original_transcript: MyTranscription) -> MyTranscription:
        transcript = super().execute(original_transcript)
        new_word_token = WordToken(word=self.word, word_id=generate_mock_id('word'), ts_start=self.ts_start,
                                   ts_end=self.ts_end, speaker=self.speaker)
        duration = self.ts_end - self.ts_start
        # modify all ts values, append and sort
        for i in range(len(transcript.text)):
            if transcript.text[i].ts_start > self.ts_start:
                a_word_token = transcript.text[i]
                a_word_token.ts_start = a_word_token.ts_start + duration
                a_word_token.ts_end = a_word_token.ts_end + duration
                transcript.text[i] = a_word_token
        transcript.text.append(new_word_token)

        transcript.text = sorted(transcript.text, key=lambda x: x.ts_start)
        transcript.ts_end = transcript.text[-1].ts_end
        return transcript


@dataclass
class ReplaceOp(_EditOperationBase):
    replaced_word_id: str
    new_word: str
    new_ts_end: int
    speaker: str
    op_type: str = 'replace'

    def execute(self, original_transcript: MyTranscription) -> MyTranscription:
        transcript = super().execute(original_transcript)
        index = next((index for (index, word) in enumerate(transcript.text) if word.word_id == self.replaced_word_id),
                     None)
        replaced_word = transcript.text[index]
        previous_duration = replaced_word.ts_end - replaced_word.ts_start
        ts_start = replaced_word.ts_start

        new_word_token = WordToken(word=self.new_word, word_id=generate_mock_id('word'), ts_start=ts_start,
                                   ts_end=self.new_ts_end, speaker=self.speaker)
        transcript.text[index] = new_word_token

        duration = self.new_ts_end - ts_start
        for i in range(index + 1, len(transcript.text)):
            a_word_token = transcript.text[i]
            a_word_token.ts_start = a_word_token.ts_start + duration - previous_duration
            a_word_token.ts_end = a_word_token.ts_end + duration - previous_duration
            transcript.text[i] = a_word_token

        transcript.ts_end = transcript.text[-1].ts_end
        return transcript
