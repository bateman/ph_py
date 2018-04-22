class Post:

    def __init__(self, post_id, name, tagline, created_at, day, comments_count, votes_count, discussion_url,
                 redirect_url, screenshot_url, maker_inside, user, current_user, comments=None, votes=None,
                 related_links=None, install_links=None, related_posts=None, media=None, description=None, topics=None,
                 external_links=None, featured=None, exclusive=None, product_state=None,
                 category_id=None, badges=None, reviews_count=None, positive_reviews_count=None,
                 negative_reviews_count=None, neutral_reviews_count=None, makers=None, platforms=None):

        from .. import helpers

        self.id = post_id
        self.name = name
        self.tagline = tagline
        self.created_at = created_at
        self.day = day
        self.comments_count = comments_count
        self.votes_count = votes_count
        self.discussion_url = discussion_url
        self.redirect_url = redirect_url
        self.screenshot_url = screenshot_url
        self.maker_inside = maker_inside
        self.current_user = current_user
        self.user = helpers.parse_users(user)
        self.comments = helpers.parse_comments(comments)
        self.votes = helpers.parse_votes(votes)
        self.related_links = helpers.parse_related_links(related_links)
        self.install_links = helpers.parse_install_links(install_links)
        #
        self.description = description
        self.featured = featured
        self.exclusive = exclusive
        self.product_state = product_state
        self.category_id = category_id
        self.reviews_count = reviews_count
        self.positive_reviews_count = positive_reviews_count
        self.negative_reviews_count = negative_reviews_count
        self.neutral_reviews_count = neutral_reviews_count
        self.makers = helpers.parse_users(makers)
        self.platforms = helpers.parse_platforms(platforms)
        self.topics = helpers.parse_topics(topics)
        self.external_links = helpers.parse_external_links(external_links)  # around the web
        self.badges = helpers.parse_badges(badges)
        self.related_posts = helpers.parse_related_posts(related_posts)
        self.media = helpers.parse_media(media)
        pass
