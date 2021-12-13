from ..utils import clean_podcast_url as clean_podcast_url, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, try_get as try_get, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class SimplecastBaseIE(InfoExtractor): ...

class SimplecastIE(SimplecastBaseIE):
    IE_NAME: str

class SimplecastEpisodeIE(SimplecastBaseIE):
    IE_NAME: str

class SimplecastPodcastIE(SimplecastBaseIE):
    IE_NAME: str
