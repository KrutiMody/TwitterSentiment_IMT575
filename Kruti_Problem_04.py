import sys
import json
import string
import collections

# Calculate frequency of each word in all tweets
def freqency(tweet_file):
    freq = collections.defaultdict(int)
    with open(tweet_file) as tf:
        for line in tf:
            tweet = json.loads(line)
            if 'text' in tweet.keys():
                words = str(tweet['text']).split()
                for word in words:
                    word = clean_word(word)
                    freq[word] += 1
    all_term_sum = sum(freq.values())
    sorted_freq = collections.OrderedDict(sorted(freq.items()))
    for key, value in sorted_freq.items():
        print(key, value / all_term_sum)

# remove the punctuations in the words
def clean_word(word):
    word = word.lower()
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word if ch not in exclude)
    return word


def main():
    tweet_file = sys.argv[1]
    #tweet_file = "write_attempt.txt"
    freqency(tweet_file)


if __name__ == '__main__':
    main()