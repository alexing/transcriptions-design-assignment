import aiofiles as aiof
import dataclasses
import json
import os
import pandas as pd
import time

from typing import Any, Optional

from data_models import MyTranscription, WordToken

DB_FILE = f"db.tsv"


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, an_object: Any) -> Any:
        if dataclasses.is_dataclass(an_object):
            return dataclasses.asdict(an_object)
        return super().default(an_object)


def json_to_dataclass(a_json_string: str) -> Optional[MyTranscription]:
    json_dict = json.loads(a_json_string)
    list_of_word_tokens = []
    for word in json_dict['text']:
        list_of_word_tokens.append(WordToken(**word))
    return MyTranscription(text=list_of_word_tokens, speakers=json_dict['speakers'],
                           audio_file_id=json_dict['audio_file_id'],
                           transcript_id=json_dict['transcript_id'], ts_end=json_dict['ts_end'])


async def db_store(transcript: MyTranscription, uid: str) -> None:
    async with aiof.open(DB_FILE, mode="a" if os.path.exists(DB_FILE) else "w") as f:
        timestamp = str(time.time())
        row = f"{uid}\t{json.dumps(transcript, cls=EnhancedJSONEncoder)}\t{timestamp}\n"
        await f.write(row)
        await f.flush()
        transcript.stored = True
        print('done saving')


def db_get_last_finished(uid: str) -> Optional[MyTranscription]:
    df = pd.read_csv(DB_FILE, delimiter='\t', names=['uid', 'transcript_json', 'timestamp'])
    if uid not in df['uid'].values:
        return None
    uid_transcripts = df[df['uid'] == uid]
    transcript_json = uid_transcripts.loc[uid_transcripts['timestamp'].idxmax()]['transcript_json']
    return json_to_dataclass(transcript_json)
