class Media(object):

    def __init__(self, media_id, kindle_asin, media_type, priority, platform, video_id, original_width,
                 original_height, image_url, metadata_url):
        self.id = media_id
        self.kindle_asin = kindle_asin
        self.media_type = media_type
        self.priority = priority
        self.platform = platform
        self.video_id = video_id
        self.original_width = original_width
        self.original_height = original_height
        self.image_url = image_url
        self.metadata_url = metadata_url
