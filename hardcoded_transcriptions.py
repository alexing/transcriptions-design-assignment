import numpy as np

from data_models import MyTranscription, WordToken, SILENCE_TOKEN

dummy_audios = {
    'a': np.array([b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a',
                   b'\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14',
                   b'\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e']),
    'b': np.array([b'\x01\x23\x45\x67\x89\xab\xcd\xef\xff',
                   b'\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33',
                   b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99']),
    'c': np.array([b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99',
                   b'\x99\x88\x77\x66\x55\x44\x33\x22\x11\x00',
                   b'\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa'])

}
dummy_transcriptions = {
    'a': MyTranscription(
        text=[WordToken(word='Today', word_id='wo1', ts_start=0, ts_end=10, speaker='John'),
              WordToken(word='in', word_id='wo2', ts_start=11, ts_end=23, speaker='John'),
              WordToken(word='our', word_id='wo3', ts_start=24, ts_end=35, speaker='John'),
              WordToken(word='new', word_id='wo4', ts_start=36, ts_end=50, speaker='John'),
              WordToken(word='podcast', word_id='wo5', ts_start=51, ts_end=64, speaker='John'),
              WordToken(word='we', word_id='wo6', ts_start=65, ts_end=77, speaker='John'),
              WordToken(word='will', word_id='wo7', ts_start=78, ts_end=85, speaker='John'),
              WordToken(word='talk', word_id='wo8', ts_start=86, ts_end=93, speaker='John'),
              WordToken(word='about', word_id='wo9', ts_start=94, ts_end=100, speaker='John'),
              WordToken(word='the', word_id='wo10', ts_start=101, ts_end=109, speaker='John'),
              WordToken(word='world.', word_id='wo11', ts_start=110, ts_end=115, speaker='John'),
              WordToken(word=SILENCE_TOKEN, word_id='wo12', ts_start=116, ts_end=130, speaker='John'),
              WordToken(word='Lets', word_id='wo13', ts_start=131, ts_end=140, speaker='Mary'),
              WordToken(word='go!', word_id='wo14', ts_start=141, ts_end=150, speaker='Mary'),
              WordToken(word=SILENCE_TOKEN, word_id='wo15', ts_start=151, ts_end=170, speaker='John')
              ],
        speakers=['John', 'Mary'],
        audio_file_id='au1',
        transcript_id='tr1',
        ts_end=170
    ),
    'b': MyTranscription(
        text=[WordToken("Why", "wo1", 0, 500, "John"),
              WordToken("did", "wo2", 501, 700, "John"),
              WordToken("the", "wo3", 701, 900, "John"),
              WordToken("chicken", "wo4", 901, 1600, "John"),
              WordToken("cross", "wo5", 1601, 2200, "John"),
              WordToken("the", "wo6", 2201, 2400, "John"),
              WordToken("road", "wo7", 2401, 3200, "John"),
              WordToken("?", "wo8", 3201, 3250, "John"),
              WordToken(word=SILENCE_TOKEN, word_id='wo9', ts_start=3251, ts_end=3300, speaker='John'),
              WordToken("To", "wo10", 3301, 3500, "Mary"),
              WordToken("get", "wo11", 3501, 3900, "Mary"),
              WordToken("to", "wo12", 3901, 4000, "Mary"),
              WordToken("the", "wo13", 4001, 4200, "Mary"),
              WordToken("other", "wo14", 4201, 4600, "Mary"),
              WordToken("side.", "wo15", 4601, 5100, "Mary"),
              WordToken(word=SILENCE_TOKEN, word_id='wo16', ts_start=5101, ts_end=5300, speaker='Mary')
              ],
        speakers=["John", "Mary"],
        audio_file_id="au2",
        transcript_id="tr2",
        ts_end=5300
    ),
    'c': MyTranscription(
        text=[
            WordToken("who", "wo1", 1, 200, "Jane"),
            WordToken("scored", "wo2", 201, 250, "Jane"),
            WordToken("the", "wo3", 251, 300, "Jane"),
            WordToken("last", "wo4", 301, 350, "Jane"),
            WordToken("goal", "wo5", 351, 450, "Jane"),
            WordToken(SILENCE_TOKEN, "wo7", 451, 500, "Mary"),
            WordToken("Lionel", "wo8", 501, 550, "Mary"),
            WordToken("Messi", "wo9", 551, 700, "Mary"),
            WordToken(SILENCE_TOKEN, "wo10", 701, 1000, "Mary"),
            WordToken("asdfjja;sldkfja;l", "wo11", 1001, 2000, "Frank")  # some garbage, why not
        ],
        speakers=["Jane", "Mary", "Frank"],
        audio_file_id="au3",
        transcript_id="tr3",
        ts_end=2000
    )
}
