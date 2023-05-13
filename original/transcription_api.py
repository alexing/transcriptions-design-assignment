from abc import ABCMeta, abstractmethod
from data_models import MyEditOperation, MyTranscription
import numpy as np
from typing import Generic, Optional, TypeVar, List

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


class MockTranscriptionAPI(TranscriptionAPI[MyTranscription, MyEditOperation]):
    def transcribe(self, audio: Audio) -> Transcript:
        """A Mock transcription function
        You can create a hardcoded mapping from inputs to outputs, depending on your test cases
        """
        pass  # TODO (Task 2) implement

    def edit(self, transcript: Transcript, edit_log: EditLog) -> Transcript:
        pass  # TODO (Task 2) implement

    async def store(self, transcript: Transcript, uid:str):
        pass # TODO (Task 2) implement

    def get_last_finished(self, uid: str) -> Optional[Transcript]:
        pass # TODO (Task 2) implement
