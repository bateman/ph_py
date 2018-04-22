class User:

    def __init__(self, user_id, name, headline, created_at, username, image_url, profile_url, twitter_username=None,
                 website_url=None):
        self.id = user_id
        self.name = name
        self.headline = headline
        self.created_at = created_at
        self.username = username
        self.image_url = image_url
        self.profile_url = profile_url
        self.twitter_username = twitter_username
        self.website_url = website_url
