from data_models import MyTranscription, WordToken

updated_transcription_1a = MyTranscription(
    text=[WordToken(word='Today', word_id='wo1', ts_start=0, ts_end=10, speaker='John'),
          WordToken(word='in', word_id='wo2', ts_start=11, ts_end=23, speaker='John'),
          WordToken(word='our', word_id='wo3', ts_start=24, ts_end=35, speaker='John'),
          WordToken(word='new', word_id='wo4', ts_start=36, ts_end=50, speaker='John'),
          WordToken(word='podcast', word_id='wo5', ts_start=51, ts_end=64, speaker='John'),
          WordToken(word='we', word_id='wo6', ts_start=65, ts_end=77, speaker='John'),
          WordToken(word='will', word_id='wo7', ts_start=78, ts_end=85, speaker='John'),
          WordToken(word='argue', word_id='wo3283576567', ts_start=86, ts_end=94, speaker='John'),
          WordToken(word='about', word_id='wo9', ts_start=95, ts_end=101, speaker='John'),
          WordToken(word='the', word_id='wo10', ts_start=102, ts_end=110, speaker='John'),
          WordToken(word='world.', word_id='wo11', ts_start=111, ts_end=116, speaker='John'),
          WordToken(word='Lets', word_id='wo13', ts_start=118, ts_end=127, speaker='Mary'),
          WordToken(word='go!', word_id='wo14', ts_start=128, ts_end=137, speaker='Mary'),
          WordToken(word='Arsenal', word_id='wo2904950990', ts_start=139, ts_end=161, speaker='Mary')],
    speakers=['Mary', 'John'], audio_file_id='au1', transcript_id='tr1', ts_end=161)

updated_transcription_2a = MyTranscription(
    text=[WordToken(word='Today', word_id='wo1', ts_start=0, ts_end=10, speaker='John'),
          WordToken(word='in', word_id='wo2', ts_start=11, ts_end=23, speaker='John'),
          WordToken(word='our', word_id='wo3', ts_start=24, ts_end=35, speaker='John'),
          WordToken(word='new', word_id='wo4', ts_start=36, ts_end=50, speaker='John'),
          WordToken(word='podcast', word_id='wo5', ts_start=51, ts_end=64, speaker='John'),
          WordToken(word='we', word_id='wo6', ts_start=65, ts_end=77, speaker='John'),
          WordToken(word='will', word_id='wo7', ts_start=78, ts_end=85, speaker='John'),
          WordToken(word='talk', word_id='wo8', ts_start=86, ts_end=93, speaker='John'),
          WordToken(word='about', word_id='wo9', ts_start=94, ts_end=100, speaker='John'),
          WordToken(word='Lets', word_id='wo13', ts_start=104, ts_end=113, speaker='Mary'),
          WordToken(word='go!', word_id='wo14', ts_start=114, ts_end=123, speaker='Mary'),
          WordToken(word='<...>', word_id='wo15', ts_start=124, ts_end=143, speaker='John'),
          WordToken(word='River', word_id='wo3355253465', ts_start=150, ts_end=160, speaker='Mary'),
          WordToken(word='Plate', word_id='wo1817326000', ts_start=161, ts_end=170, speaker='Mary')],
    speakers=['John', 'Mary'], audio_file_id='au1', transcript_id='tr1', ts_end=170)

updated_transcription_1b = MyTranscription(
    text=[WordToken(word='Why', word_id='wo1', ts_start=0, ts_end=500, speaker='John'),
          WordToken(word='did', word_id='wo2', ts_start=501, ts_end=700, speaker='John'),
          WordToken(word='the', word_id='wo3', ts_start=701, ts_end=900, speaker='John'),
          WordToken(word='chicken', word_id='wo4', ts_start=901, ts_end=1600, speaker='John'),
          WordToken(word='cross', word_id='wo5', ts_start=1601, ts_end=2200, speaker='John'),
          WordToken(word='the', word_id='wo6', ts_start=2201, ts_end=2400, speaker='John'),
          WordToken(word='road', word_id='wo7', ts_start=2401, ts_end=3200, speaker='John'),
          WordToken(word='?', word_id='wo8', ts_start=3201, ts_end=3250, speaker='John'),
          WordToken(word='<...>', word_id='wo9', ts_start=3251, ts_end=3300, speaker='John')],
    speakers=['John'], audio_file_id='au2', transcript_id='tr2', ts_end=3300)

updated_transcription_2b = MyTranscription(
    text=[WordToken(word='Why', word_id='wo1', ts_start=0, ts_end=500, speaker='John'),
          WordToken(word='did', word_id='wo2', ts_start=501, ts_end=700, speaker='John'),
          WordToken(word='the', word_id='wo3', ts_start=701, ts_end=900, speaker='John'),
          WordToken(word='dinosaur', word_id='wo9320360012', ts_start=901, ts_end=1500, speaker='John'),
          WordToken(word='cross', word_id='wo5', ts_start=1501, ts_end=2100, speaker='John'),
          WordToken(word='the', word_id='wo6', ts_start=2101, ts_end=2300, speaker='John'),
          WordToken(word='road', word_id='wo1098300502', ts_start=2301, ts_end=3300, speaker='John'),
          WordToken(word='?', word_id='wo8', ts_start=3301, ts_end=3350, speaker='John'),
          WordToken(word='<...>', word_id='wo9', ts_start=3351, ts_end=3400, speaker='John'),
          WordToken(word='To', word_id='wo10', ts_start=3401, ts_end=3600, speaker='Mary'),
          WordToken(word='get', word_id='wo11', ts_start=3601, ts_end=4000, speaker='Mary'),
          WordToken(word='extinct', word_id='wo2669041039', ts_start=4001, ts_end=5000, speaker='Mary'),
          WordToken(word='<...>', word_id='wo16', ts_start=5004, ts_end=5203, speaker='Mary')],
    speakers=['John', 'Mary'], audio_file_id='au2', transcript_id='tr2', ts_end=5203)

updated_transcription_1c = MyTranscription(
    text=[WordToken(word='who', word_id='wo1', ts_start=1, ts_end=200, speaker='Jane'),
          WordToken(word='is', word_id='wo2841267681', ts_start=201, ts_end=260, speaker='Jane'),
          WordToken(word='the', word_id='wo3', ts_start=261, ts_end=310, speaker='Jane'),
          WordToken(word='best', word_id='wo1328827946', ts_start=311, ts_end=350, speaker='Jane'),
          WordToken(word='of', word_id='wo1215259113', ts_start=351, ts_end=456, speaker='Jane'),
          WordToken(word='all', word_id='wo2345679822', ts_start=406, ts_end=450, speaker='Jane'),
          WordToken(word='time', word_id='wo2583321959', ts_start=451, ts_end=500, speaker='Jane'),
          WordToken(word='<...>', word_id='wo7', ts_start=550, ts_end=599, speaker='Mary'),
          WordToken(word='Lionel', word_id='wo8', ts_start=600, ts_end=649, speaker='Mary'),
          WordToken(word='Messi', word_id='wo9', ts_start=650, ts_end=799, speaker='Mary'),
          WordToken(word='<...>', word_id='wo10', ts_start=800, ts_end=1099, speaker='Mary')],
    speakers=['Jane', 'Mary'], audio_file_id='au3', transcript_id='tr3', ts_end=1099)

integration_test_transcription_1 = MyTranscription(
    text=[WordToken(word='Today', word_id='wo1', ts_start=0, ts_end=10, speaker='John'),
          WordToken(word='in', word_id='wo2', ts_start=11, ts_end=23, speaker='John'),
          WordToken(word='our', word_id='wo3', ts_start=24, ts_end=35, speaker='John'),
          WordToken(word='new', word_id='wo4', ts_start=36, ts_end=50, speaker='John'),
          WordToken(word='podcast', word_id='wo5', ts_start=51, ts_end=64, speaker='John'),
          WordToken(word='we', word_id='wo6', ts_start=65, ts_end=77, speaker='John'),
          WordToken(word='will', word_id='wo7', ts_start=78, ts_end=85, speaker='John'),
          WordToken(word='argue', word_id='wo1938650442', ts_start=86, ts_end=94, speaker='John'),
          WordToken(word='about', word_id='wo9', ts_start=95, ts_end=101, speaker='John'),
          WordToken(word='the', word_id='wo10', ts_start=102, ts_end=110, speaker='John'),
          WordToken(word='world.', word_id='wo11', ts_start=111, ts_end=116, speaker='John'),
          WordToken(word='Lets', word_id='wo13', ts_start=118, ts_end=127, speaker='Mary'),
          WordToken(word='go!', word_id='wo14', ts_start=128, ts_end=137, speaker='Mary'),
          WordToken(word='Arsenal', word_id='wo7128934249', ts_start=139, ts_end=161, speaker='Mary')],
    speakers=['John', 'Mary'], audio_file_id='au1', transcript_id='tr1', ts_end=161)

integration_test_transcription_4 = MyTranscription(
    text=[WordToken(word='who', word_id='wo1', ts_start=1, ts_end=200, speaker='Jane'),
          WordToken(word='is', word_id='wo2368608699', ts_start=201, ts_end=260, speaker='Jane'),
          WordToken(word='the', word_id='wo3', ts_start=261, ts_end=310, speaker='Jane'),
          WordToken(word='best', word_id='wo2337657983', ts_start=311, ts_end=350, speaker='Jane'),
          WordToken(word='of', word_id='wo2205842373', ts_start=351, ts_end=456, speaker='Jane'),
          WordToken(word='all', word_id='wo3066108661', ts_start=406, ts_end=450, speaker='Jane'),
          WordToken(word='time', word_id='wo1086757723', ts_start=451, ts_end=500, speaker='Jane'),
          WordToken(word='Lionel', word_id='wo8', ts_start=551, ts_end=600, speaker='Mary'),
          WordToken(word='Messi', word_id='wo9', ts_start=601, ts_end=750, speaker='Mary')],
    speakers=['Jane', 'Mary'], audio_file_id='au3', transcript_id='tr3', ts_end=750)
