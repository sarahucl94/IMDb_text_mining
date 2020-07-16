# Aligining subs and DVS text

Very old scripts (need to revise them) for simple textmining of IMDb reviews. Overall, these scripts take reviews and analyse them for valence to be used for naturalistic neuroimaging studies. They also segment the audio into dialogue vs non-dialogue, which can later be used for speech-to-text on either AWS or Google API. The non-dialogue segments contain Descriptive Video Service (DVS) for the visually impaired. Initially, I was planning to annotate the subtitles+DVS second-by-second, but most movies do not have DVS audio and this project was put on hold until more audio data is made available.



The 2 IMDB_.py files take user and critic reviews from IMDb for one movie and put them into a .txt file

Word_Valence_Calculator.py groups the words from the paper into a valence category to be used for comparison below

The 2 Wc_by_.py files compare the reviews to the valence words/Neurosynth words for one movie and outputs relevant statistics

The 2 audio_get_.py files analyse the subtitles and output first the times in-between them, which will be when DVS is present. These times are matched to the audio of the movie to output one DVS audio file to be sent to the Google API.

