Future improvements:
1) Actually using a db and move to using data classes related to it. SQLalchemy is a good solution for this.
2) Regarding this dataclasses, an improvement to its design would be to create the dataclass `DialogueChunk`. 
A MyTranscription instance would have an element called `dialogue` which would be a `List[DialogueChunk]`. 
This `DialogueChunk` would have a `List[WordToken]` and a `speaker`. This way we could simulate a conversation better 
and closer to reality.
Of course, every method would have to adapt to this.
3) More test cases, because you never have enough tests. Maybe even a real integration tests once we have more real 
components to the system.

 -------
The goal of this assignment is to implement a mock model for a multi-speaker transcription editing, as a direct continuation to the interview question.

The assignment is open-ended and you can use any design and dependency you wish, as long as you adhere to the given constraints. We definitely encourage you to bring your own design style to the code.

There are four tasks - they can of course be done in any order. They are marked by `#TODO (Task <#>)`
1. Data modeling - Design `MyTranscription` and `MyEditOperation` data models (You can add inheritance from other data modeling tools)
2. Editing - Implement the `MockTranscriptionApi` class. This is the core of the assignment
    - The `transcribe` method should only act statically (you're not expected to implement a transcription mechanism)
    - The `edit` method should be fully implemented, to allow edit operations
    - The `store` and `get_last_finished` operations, should allow versioning of a transcription based on a provided `uid`. Some edits may be partial and not finished, so you should incorporate it into your design.
    - Persistence is only required within the same run - you're not required to use a DB, so you can either store them in-memory or in the a file
    - Note that `store` is defined as `async`, so even if you choose to store in-memory, make sure you write your code as if it had an awaited I/O operation running behind the scenes.
3. Creating test cases - Generate test cases for the aforementioned functions (try to use minimal examples that cover your code well)
4. Use a testing framework (Optional) - You can refactor the `test.py` file to use a testing framework in case you want more flexibility for your tests
