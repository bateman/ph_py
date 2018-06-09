from .models.badges import Badge
from .models.comment import Comment
from .models.external_link import ExternalLink
from .models.install_link import InstallLink
from .models.media import Media
from .models.notification import Notification
from .models.post import Post
from .models.related_link import RelatedLink
from .models.topics import Topic
from .models.user import User
from .models.user_details import UserDetails
from .models.vote import Vote


def parse_notifications(notifications):
    return [
        Notification(
            notification["id"],
            notification["body"],
            notification["seen"],
            notification["sentence"],
            notification["type"],
            notification["reference"],
            notification["from_user"],
            notification["to_user"]
        ) for notification in notifications
    ]


def parse_details(details):
    return UserDetails(
        details["id"],
        details["name"],
        details["headline"],
        details["created_at"],
        details["username"],
        details["image_url"],
        details["profile_url"],
        details["votes_count"],
        details["posts_count"],
        details["maker_of_count"],
        details["email"],
        details["role"],
        details["permissions"],
        details["notifications"],
        details["first_time_user"]
    )


def parse_posts(posts):
    if isinstance(posts, list):
        return [
            Post(
                post["id"],
                post["name"],
                post["tagline"],
                post["created_at"],
                post["day"],
                post["comments_count"],
                post["votes_count"],
                post["discussion_url"],
                post["redirect_url"],
                post["screenshot_url"],
                post["maker_inside"],
                post["user"],
                post["current_user"] if "current_user" in post else None
            ) for post in posts]
    else:
        return Post(
            posts["id"],
            posts["name"],
            posts["tagline"],
            posts["created_at"],
            posts["day"],
            posts["comments_count"],
            posts["votes_count"],
            posts["discussion_url"],
            posts["redirect_url"],
            posts["screenshot_url"],
            posts["maker_inside"],
            posts["user"],
            posts["current_user"] if "current_user" in posts else None,
            # added
            posts["comments"],
            posts["votes"],
            posts["related_links"],
            posts["install_links"],
            posts["related_posts"],
            posts["media"],
            posts["description"],
            posts["topics"],
            posts["external_links"],
            posts["featured"],
            posts["exclusive"],
            posts["product_state"],
            posts["category_id"],
            posts["badges"],
            posts["reviews_count"],
            posts["positive_reviews_count"],
            posts["negative_reviews_count"],
            posts["neutral_reviews_count"],
            posts["makers"],
            posts["platforms"]
        )


def parse_users(users):
    if isinstance(users, list):
        return [
            User(
                user["id"],
                user["name"],
                user["headline"],
                user["created_at"],
                user["username"],
                user["image_url"],
                user["profile_url"],
                user["twitter_username"],
                user["website_url"]
            ) for user in users]
    elif users:
        return User(
            users["id"],
            users["name"],
            users["headline"],
            users["created_at"],
            users["username"],
            users["image_url"],
            users["profile_url"],
            users["twitter_username"],
            users["website_url"]
        )
    else:
        return None


def parse_user(user):
    if user:
        return User(
            user["id"],
            user["name"],
            user["headline"],
            user["created_at"],
            user["username"],
            user["image_url"],
            user["profile_url"],
            user["twitter_username"],
            user["website_url"],
            # added
            user["collections_count"],
            user["followed_topics_count"],
            user["followers"],
            user["followers_count"],
            user["followings"],
            user["followings_count"],
            user["header_image_url"],
            user["maker_of"],
            user["maker_of_count"],
            user["posts"],
            user["posts_count"],
            user["votes"],
            user["votes_count"]
            # mancano collections_followed_count, daily_strake
        )
    else:
        return None


def parse_followings_or_followers(users):
    if isinstance(users, list):
        return [
            {
                "id": user["user"]["id"],
                "created_at": user["created_at"],
                "name":  user["user"]["name"],
                "username":  user["user"]["username"]
            } for user in users]
    elif users:
        return {
            "id": users["user"]["id"],
            "created_at": users["created_at"],
            "name":  users["user"]["name"],
            "username":  users["user"]["username"]
        }


def parse_votes(votes):
    if isinstance(votes, list):
        return [
            {
                "id": vote["id"],
                "created_at": vote["created_at"],
                "post_id": vote["post_id"],
                "user_id": vote["user_id"]
            } for vote in votes]
    elif votes:
        return {
            "id": votes["id"],
            "created_at": votes["created_at"],
            "post_id": votes["post_id"],
            "user_id": votes["user_id"]
        }


def parse_related_links(related_links):
    if isinstance(related_links, list):
        return [
            RelatedLink(
                related_link["id"],
                related_link["url"],
                related_link["title"],
                related_link["domain"],
                related_link["favicon"],
                related_link["post_id"],
                related_link["user_id"],
            ) for related_link in related_links]
    elif related_links:
        return RelatedLink(
            related_links["id"],
            related_links["url"],
            related_links["title"],
            related_links["domain"],
            related_links["favicon"],
            related_links["post_id"],
            related_links["user_id"],
        )


def parse_install_links(install_links):
    if isinstance(install_links, list):
        return [
            InstallLink(
                install_link["platform"],
                install_link["created_at"],
                install_link["redirect_url"],
                install_link["post_id"],
            ) for install_link in install_links]
    elif install_links:
        return InstallLink(
            install_links["platform"],
            install_links["created_at"],
            install_links["redirect_url"],
            install_links["post_id"],
        )


def parse_comments(comments):
    if isinstance(comments, list):
        return [
            Comment(
                comment["id"],
                comment["body"],
                comment["created_at"],
                comment["post_id"],
                comment["parent_comment_id"],
                comment["user_id"],
                comment["child_comments_count"],
                comment["maker"],
                comment["user"],
                comment["child_comments"]
            ) for comment in comments]
    elif comments:
        return Comment(
            comments["id"],
            comments["body"],
            comments["created_at"],
            comments["post_id"],
            comments["parent_comment_id"],
            comments["user_id"],
            comments["child_comments_count"],
            comments["maker"],
            comments["user"],
            comments["child_comments"],
        )


def parse_topics(topics):
    if isinstance(topics, list):
        return [Topic(
            topic["id"],
            topic["name"],
            topic["slug"]
        ) for topic in topics]
    else:
        return None


def parse_badges(badges):
    if isinstance(badges, list):
        return [Badge(
            badge["id"],
            badge["type"],
            badge["data"]["date"],
            badge["data"]["period"],
            badge["data"]["position"]
        ) for badge in badges]
    else:
        return None


def parse_platforms(platforms):
    if isinstance(platforms, list) and platforms:
        pass
    else:
        return None


def parse_external_links(external_links):
    if isinstance(external_links, list) and external_links:
        return [ExternalLink(
            external_link["id"],
            external_link["title"],
            external_link["description"],
            external_link["author"],
            external_link["source"],
            external_link["url"],
            external_link["favicon_image_uuid"],
            external_link["link_type"]
        ) for external_link in external_links]
    else:
        return None


def parse_media(media):
    if isinstance(media, list) and media:
        return [Media(
            m["id"],
            m["kindle_asin"],
            m["media_type"],
            m["priority"],
            m["platform"],
            m["video_id"],
            m["original_width"],
            m["original_height"],
            m["image_url"],
            _get_metadata_url(m),
        ) for m in media]
    else:
        return None


def _get_metadata_url(media):
    metadata_url = None
    if media["metadata"]:
        metadata_url = media["metadata"]["url"]
    return metadata_url


def parse_related_posts(posts):
    if isinstance(posts, list) and posts:
        return [post["id"] for post in posts]
    else:
        return None
