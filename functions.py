import pylyrics3
import nltk


# Getting lyrics for a specified author from LyricWikia
def get_lyrics(artist_name):

    # Get lyrics
    lyrics = pylyrics3.get_artist_lyrics(artist_name)

    # Get number of songs
    songs_number = len(lyrics)

    # Store lyrics as a string
    lyrics_raw = ""
    for key in lyrics:
        current = lyrics[key]
        lyrics_raw += current

    return lyrics_raw, songs_number


# Further processing lyrics
def process_lyrics(lyrics_raw):

    # Returns lyrics processed and tagged by part of speech with nltk module

    # Remove newlines
    lyrics_raw.replace("\n", "")

    # Tokenize words
    text = nltk.word_tokenize(lyrics_raw)

    # Lowercase all letters, remove numerics, remove most popular "I"
    text = [word.lower() for word in text if word.isalpha()]
    text = [word for word in text if word != "i"]

    # Tag words
    processed = nltk.pos_tag(text, tagset='universal')

    return processed


# Returns a list of 50 most frequent words which are in given part of speech
def get_top(processed_lyrics, partofspeech):

    # Parts of speech are:
    #  - NOUN (nouns)
    #  - VERB (verbs)
    #  - ADJ (adjectives)
    #  - ADV (adverbs)
    #  - PRON (pronouns)
    #  - DET (determiners and articles)
    #  - ADP (prepositions and postpositions)
    #  - NUM (numerals) # - CONJ (conjunctions) # - PRT (particles)
    #  - . (punctuation marks) # - X (a catch-all for other categories such as abbreviations or foreign words)

    # Checking if given word is a specified part of speech
    processed_lyrics = [x for x in processed_lyrics if x[1] == partofspeech]

    # Creating a ranking
    fdist = nltk.FreqDist(processed_lyrics)

    # Initializing formatted results
    if partofspeech == "NOUN":
        top_words = "Top 10 nouns" + "\n"
    else:
        top_words = "Top 10 adjectives" + "\n"

    # Creating a formatted list of top10 results
    counter = 1
    for word, frequency in fdist.most_common(10):
        top_words += str(counter) + ". " + word[0] + " -  repeated " + str(frequency) + " times \n"
        counter += 1

    return top_words


