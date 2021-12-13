from ..compat import compat_parse_qs as compat_parse_qs, compat_str as compat_str, compat_urllib_parse_urlencode as compat_urllib_parse_urlencode, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, dict_get as dict_get, float_or_none as float_or_none, int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, qualities as qualities, try_get as try_get, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from typing import Any, NamedTuple

class TwitchBaseIE(InfoExtractor): ...

class TwitchVodIE(TwitchBaseIE):
    IE_NAME: str

class TwitchCollectionIE(TwitchBaseIE): ...
class TwitchPlaylistBaseIE(TwitchBaseIE): ...

class TwitchVideosIE(TwitchPlaylistBaseIE):

    class Broadcast(NamedTuple):
        type: Any
        label: Any
    @classmethod
    def suitable(cls, url): ...

class TwitchVideosClipsIE(TwitchPlaylistBaseIE):

    class Clip(NamedTuple):
        filter: Any
        label: Any

class TwitchVideosCollectionsIE(TwitchPlaylistBaseIE): ...

class TwitchStreamIE(TwitchBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class TwitchClipsIE(TwitchBaseIE):
    IE_NAME: str
