class ExternalLink:

    def __init__(self, external_link_id, url, title, description, author, source, favicon_image_uuid, link_type):
        self.id = external_link_id
        self.url = url
        self.title = title
        self.description = description
        self.author = author
        self.source = source
        self.favicon_image_uuid = favicon_image_uuid
        self.link_type = link_type
