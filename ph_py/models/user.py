class User:

    def __init__(self, user_id, name, headline, created_at, username, image_url, profile_url, twitter_username,
                 website_url, collections_count=None, followed_topics_count=None, followers=None, followers_count=None,
                 followings=None, followings_count=None, header_image_url=None, maker_of=None, maker_of_count=None,
                 posts=None, posts_count=None, votes=None, votes_count=None):
        self.id = user_id
        self.name = name
        self.headline = headline
        self.created_at = created_at
        self.username = username
        self.image_url = image_url
        self.profile_url = profile_url
        self.twitter_username = twitter_username
        self.website_url = website_url
        # optional
        self.collections_count = collections_count
        self.followed_topics_count = followed_topics_count
        self.followers = followers
        self.followers_count = followers_count
        self.followings = followings
        self.followings_count = followings_count
        self.header_image_url = header_image_url
        self.maker_of = maker_of
        self.maker_of_count = maker_of_count
        self.posts = posts
        self.posts_count = posts_count
        self.votes = votes
        self.votes_count = votes_count
