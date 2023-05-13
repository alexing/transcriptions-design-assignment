from data_models import RemoveOp, AddOp, ReplaceOp, generate_mock_id

edit_log_1_tr_a = [
    RemoveOp(transcript_id='tr1', op_id=generate_mock_id('op'), word_id='wo12'),
    RemoveOp(transcript_id='tr1', op_id=generate_mock_id('op'), word_id='wo15'),
    AddOp(transcript_id='tr1', op_id=generate_mock_id('op'), word='Arsenal', ts_start=138, ts_end=160, speaker='Mary'),
    ReplaceOp(transcript_id='tr1', op_id=generate_mock_id('op'), replaced_word_id='wo8', new_word='argue',
              new_ts_end=94, speaker='John')
]
edit_log_2_tr_a = [
    RemoveOp(transcript_id='tr1', op_id=generate_mock_id('op'), word_id='wo12'),
    RemoveOp(transcript_id='tr1', op_id=generate_mock_id('op'), word_id='wo10'),
    RemoveOp(transcript_id='tr1', op_id=generate_mock_id('op'), word_id='wo11'),
    AddOp(transcript_id='tr1', op_id=generate_mock_id('op'), word='River', ts_start=150, ts_end=160, speaker='Mary'),
    AddOp(transcript_id='tr1', op_id=generate_mock_id('op'), word='Plate', ts_start=161, ts_end=170, speaker='Mary'),
]
edit_log_3_tr_a = [
    RemoveOp(transcript_id='tr1', op_id=generate_mock_id('op'), word_id='wo10'),
    RemoveOp(transcript_id='tr1', op_id=generate_mock_id('op'), word_id='wo11'),
    AddOp(transcript_id='tr1', op_id=generate_mock_id('op'), word='River', ts_start=150, ts_end=160, speaker='Mary'),
    AddOp(transcript_id='tr1', op_id=generate_mock_id('op'), word='Plate', ts_start=161, ts_end=171, speaker='Mary'),
]

edit_log_1_tr_b = [
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo10'),
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo11'),
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo12'),
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo13'),
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo14'),
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo15'),
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo16')
]

edit_log_2_tr_b = [
    ReplaceOp(transcript_id='tr2', op_id=generate_mock_id('op'), replaced_word_id='wo4',
              new_word='dinosaur', new_ts_end=1500, speaker='John'),
    ReplaceOp(transcript_id='tr2', op_id=generate_mock_id('op'), replaced_word_id='wo7',
              new_word='road', new_ts_end=3300, speaker='John'),
    ReplaceOp(transcript_id='tr2', op_id=generate_mock_id('op'), replaced_word_id='wo12',
              new_word='extinct', new_ts_end=5000, speaker='Mary'),
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo13'),
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo14'),
    RemoveOp(transcript_id='tr2', op_id=generate_mock_id('op'), word_id='wo15')
]

edit_log_1_tr_c = [
    ReplaceOp(transcript_id='tr3', op_id=generate_mock_id('op'), replaced_word_id='wo2',
              new_word='is', new_ts_end=260, speaker='Jane'),
    ReplaceOp(transcript_id='tr3', op_id=generate_mock_id('op'), replaced_word_id='wo4',
              new_word='best', new_ts_end=350, speaker='Jane'),
    ReplaceOp(transcript_id='tr3', op_id=generate_mock_id('op'), replaced_word_id='wo5',
              new_word='of', new_ts_end=456, speaker='Jane'),
    AddOp(transcript_id='tr3', op_id=generate_mock_id('op'), word='all', ts_start=406, ts_end=450, speaker='Jane'),
    AddOp(transcript_id='tr3', op_id=generate_mock_id('op'), word='time', ts_start=451, ts_end=500, speaker='Jane'),
    RemoveOp(transcript_id='tr3', op_id=generate_mock_id('op'), word_id='wo11'),
]

edit_log_2_tr_c = [
    RemoveOp(transcript_id='tr3', op_id=generate_mock_id('op'), word_id='wo7'),
    RemoveOp(transcript_id='tr3', op_id=generate_mock_id('op'), word_id='wo10')
]
