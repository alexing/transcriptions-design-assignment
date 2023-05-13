import numpy as np

from abc import ABCMeta, abstractmethod
from typing import Generic, Optional, TypeVar, List

from data_models import MyTranscription, TranscriptionNotPossible, _EditOperationBase
from db_utils import db_get_last_finished, db_store
from hardcoded_transcriptions import dummy_transcriptions, dummy_audios

Transcript = TypeVar("Transcript")
EditOperation = TypeVar("EditOperation")
Audio = np.ndarray
EditLog = List[EditOperation]


class TranscriptionAPI(Generic[Transcript, EditOperation], metaclass=ABCMeta):
    @abstractmethod
    def transcribe(self, audio: Audio) -> Transcript:
        pass

    @abstractmethod
    def edit(self, transcript: Transcript, edit_log: EditLog) -> Transcript:
        pass

    @abstractmethod
    async def store(self, transcript: Transcript, uid: str):
        pass

    @abstractmethod
    def get_last_finished(self, uid: str) -> Optional[Transcript]:
        pass


class MockTranscriptionAPI(TranscriptionAPI[MyTranscription, _EditOperationBase]):
    def transcribe(self, audio: Audio) -> MyTranscription:
        """A Mock transcription function
        You can create a hardcoded mapping from inputs to outputs, depending on your test cases
        """
        if np.array_equal(audio, dummy_audios['a']):
            return dummy_transcriptions['a']
        if np.array_equal(audio, dummy_audios['b']):
            return dummy_transcriptions['b']
        if np.array_equal(audio, dummy_audios['c']):
            return dummy_transcriptions['c']

        raise TranscriptionNotPossible('We are not able to transcribe that audio')

    def edit(self, transcript: MyTranscription, edit_log: EditLog) -> Transcript:
        for an_edit_op in edit_log:
            transcript = an_edit_op.execute(transcript)
        return transcript

    async def store(self, transcript: MyTranscription, uid: str) -> None:
        await db_store(transcript, uid)

    def get_last_finished(self, uid: str) -> Optional[Transcript]:
        return db_get_last_finished(uid)
