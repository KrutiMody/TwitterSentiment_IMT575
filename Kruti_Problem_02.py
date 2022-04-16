import sys
import json

'''
Here, we reads the whole output file and parse it.
After parsing we calculate the sentiment of each tweet.
'''

# calculates sentiment of the input text
def sentiment(text, sent_lib):
  words = str(text).split()
  score = 0.0
  for word in words:
    word_score = sent_lib.get(word, 0.0)
    score += word_score
  return score


# loads the sentiment library
def sentiment_library(sent_file):
  sent_lines = open(sent_file)
  scores = {}
  for line in sent_lines:
    term, score = line.split("\t")
    scores[term] = int(score)
  return scores

def tweet_sentiment(tweet_file, sent_lib):
    with open(tweet_file,encoding='utf-8') as tf:
        for line in tf:
            #print(line)
            tweet = json.loads(line)
            if 'text' in tweet.keys():
                #print(tweet['text'])
                score = sentiment(tweet['text'], sent_lib)
                print(score)


def main():
    #sentiment_file = sys.argv[1]
    #tweet_file = sys.argv[2]
    sentiment_file = "AFINN-111.txt"
    tweet_file = "write_attempt.txt"
    sent_lib = sentiment_library(sentiment_file)
    tweet_sentiment(tweet_file, sent_lib)


if __name__ == '__main__':
    main()
