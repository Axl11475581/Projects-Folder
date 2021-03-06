import tweepy
import time

auth = tweepy.AppAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)
user = api.me()


# limit handler to overview the Twitter server requests
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# bot to like tweets base on keywords
search = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favourite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# Print all the users followers
# for follower in (tweepy.Cursor(api.followers).items()):
# if follower.name == "name":
# follower.follow()
# break {to stop the process}
# print(follower.name)
