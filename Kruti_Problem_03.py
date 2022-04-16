import sys
import json
import string
import collections

# loads the sentiment library
def sentiment_library(sent_file):
    sent_lines = open(sent_file)
    scores = {}
    for line in sent_lines:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores


# reads the whole tweet log and parse it, calculates the sentiment of each tweet
def tweet_sentiment(tweet_file, sent_lib):
    term_lib = {}
    with open(tweet_file) as tf:
        for line in tf:
            tweet = json.loads(line)
            if 'text' in tweet.keys():
                word = clean_word(tweet['text'])
                score = sentiment(word, sent_lib)
                if score != 0:
                    new_term_lib = update_sentiment(score, word, sent_lib)
                    term_lib = merge_term_lib(term_lib, new_term_lib)
                sorted_term_lib = collections.OrderedDict(sorted(term_lib.items()))
    for key, value in sorted_term_lib.items():
        print(key, round(value,4))

# append the newly calculated word sentiments to the original file
def merge_term_lib(x, y):
    return dict([(n, x.get(n, 0) + y.get(n, 0)) for n in set(x) | set(y)])

# remove the punctuations in the words
def clean_word(word):
    word = str(word.lower())
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word if ch not in exclude)
    return word

# identify words not in dictionary but in tweet and calculate sentiment of word in tweet
# new word score is calculated by tweet score divided by number of words in the tweet
def update_sentiment(score, tweet, sent_lib):
    term_lib = {}
    words = tweet.split()
    for word in words:
        if word.startswith('@') != True:
            if sent_lib.__contains__(word) != True and word != '':
                term_score = score / round(len(words),4)
                #term_score = score / 10
                term_lib[word] = term_score
    return term_lib


# calculates sentiment of the tweet input param
def sentiment(tweet, sent_lib):
    words = tweet.split()
    score = 0.0
    for word in words:
        word_score = sent_lib.get(word, 0.0)
        score += word_score
    return score


def main():
    sentiment_file = sys.argv[1]
    tweet_file = sys.argv[2]
    #sentiment_file = "AFINN-111.txt"
    #tweet_file = "write_attempt.txt"
    sent_lib = sentiment_library(sentiment_file)
    tweet_sentiment(tweet_file, sent_lib)


if __name__ == '__main__':
    main()
