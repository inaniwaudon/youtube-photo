from ..utils import clean_podcast_url as clean_podcast_url, int_or_none as int_or_none, try_get as try_get, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class GooglePodcastsBaseIE(InfoExtractor): ...

class GooglePodcastsIE(GooglePodcastsBaseIE):
    IE_NAME: str

class GooglePodcastsFeedIE(GooglePodcastsBaseIE):
    IE_NAME: str
