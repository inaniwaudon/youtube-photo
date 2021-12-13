from ..compat import compat_parse_qs as compat_parse_qs, compat_str as compat_str, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import bool_or_none as bool_or_none, determine_ext as determine_ext, int_or_none as int_or_none, try_get as try_get, unified_timestamp as unified_timestamp, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class RutubeBaseIE(InfoExtractor): ...

class RutubeIE(RutubeBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class RutubeEmbedIE(RutubeBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubePlaylistBaseIE(RutubeBaseIE): ...

class RutubeChannelIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubeMovieIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubePersonIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubePlaylistIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...
