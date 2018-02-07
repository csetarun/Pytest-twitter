import tweepy
import json

class TestClass(object):
    f = open('keys.json')
    keys = json.load(f)
    consumer_key = keys['api_key']
    consumer_secret = keys['api_secret']
    access_token = keys['token']
    access_token_secret = keys['token_secret']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #Testing whether the credentials provided are working or not.
    def test_credentials(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        assert auth.get_authorization_url()!=tweepy.TweepError

    #Using in-built function for validating credentials
    def test_credentials_built_in(self):
            user = self.api.verify_credentials()
            assert type(user) is tweepy.models.User

    #Testing whether the function is returning exactly 20 statuses.
    def test_user_timeline_count(self):
        timeline = self.api.user_timeline(id='realDonaldTrump',count=20)
        assert len(timeline) is 20

    #Testing user_timeline method for valid statuses.
    def test_user_timeline_count(self):
        timeline = self.api.user_timeline(id='realDonaldTrump',count=20)
        assert type(timeline[0]) is tweepy.models.Status

    #Testing get_user method for valid User.
    def test_get_user(self):
        user = self.api.get_user(id='realDonaldTrump')
        assert type(user) is tweepy.models.User

    #Testing show_friendship method for verifying 'following' relationship between two users.
    def test_is_following(self):
        friendship = self.api.show_friendship(source_screen_name='venuseswilliams',target_screen_name='serenawilliams')
        assert friendship[0].following is True

    #This method should return most recent tweets of the user that have been retweeted by others.
    def test_retweets_of_me(self):
        retweets = self.api.retweets_of_me(count=2)
        assert len(retweets) is 2
        assert type(retweets[0]) is tweepy.models.Status

    #Testing followers method is returning vaild users.
    def test_followers(self):
        followers = self.api.followers(id='realDonaldTrump')
        assert type(followers[0]) is tweepy.models.User

    #Testing search_users is returning users info.
    def test_search_users(self):
        users = self.api.search_users(q='trump')
        assert type(users[0]) is tweepy.models.User

    #Testing friends_ids is returning ids or not.
    def test_friend_ids(self):
        friend_ids = self.api.friends_ids(id='realDonaldTrump')
        assert type(friend_ids[0]) is int

    #Testing followers_ids is returning ids or not.
    def  test_followers_ids(self):
        followers_ids = self.api.followers_ids(id='realDonaldTrump')
        assert type(followers_ids[0]) is int
