import sys
import json
import operator
import collections

# The aim here is to find top 10 hash-tags
# reads the whole tweet log and parse it, calculates the frequency of each hashtag, sort, and print
def top_ten_hash(tweet_file):
    all_hash = collections.defaultdict(float)
    with open(tweet_file) as tf:
        for line in tf:
            tweet = json.loads(line)
            if 'entities' in tweet.keys():
                hashtags = tweet['entities']['hashtags']
                for hash in hashtags:
                    all_hash[str(hash['text'])] += 1.0
    sorted_hash = sorted(all_hash.items(), key=operator.itemgetter(1), reverse=True)
    for key, value in sorted_hash[0:10]:
        print(key, value)


def main():
    tweet_file = sys.argv[1]
    #tweet_file = "write_attempt.txt"
    top_ten_hash(tweet_file)


if __name__ == '__main__':
    main()