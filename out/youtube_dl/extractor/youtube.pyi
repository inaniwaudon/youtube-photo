from ..compat import compat_HTTPError as compat_HTTPError, compat_chr as compat_chr, compat_parse_qs as compat_parse_qs, compat_str as compat_str, compat_urllib_parse_unquote_plus as compat_urllib_parse_unquote_plus, compat_urllib_parse_urlencode as compat_urllib_parse_urlencode, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse, compat_urlparse as compat_urlparse
from ..jsinterp import JSInterpreter as JSInterpreter
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, dict_get as dict_get, float_or_none as float_or_none, int_or_none as int_or_none, mimetype2ext as mimetype2ext, parse_codecs as parse_codecs, parse_duration as parse_duration, qualities as qualities, remove_start as remove_start, smuggle_url as smuggle_url, str_or_none as str_or_none, str_to_int as str_to_int, try_get as try_get, unescapeHTML as unescapeHTML, unified_strdate as unified_strdate, unsmuggle_url as unsmuggle_url, update_url_query as update_url_query, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor, SearchInfoExtractor as SearchInfoExtractor
from typing import Any

def parse_qs(url): ...

class YoutubeBaseInfoExtractor(InfoExtractor): ...

class YoutubeIE(YoutubeBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def extract_id(cls, url): ...

class YoutubeTabIE(YoutubeBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class YoutubePlaylistIE(InfoExtractor):
    IE_DESC: str
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class YoutubeYtBeIE(InfoExtractor): ...
class YoutubeYtUserIE(InfoExtractor): ...

class YoutubeFavouritesIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeSearchIE(SearchInfoExtractor, YoutubeBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: str

class YoutubeSearchDateIE(YoutubeSearchIE):
    IE_NAME: Any
    IE_DESC: str

class YoutubeFeedsInfoExtractor(YoutubeTabIE):
    @property
    def IE_NAME(self): ...

class YoutubeWatchLaterIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeRecommendedIE(YoutubeFeedsInfoExtractor):
    IE_DESC: str

class YoutubeSubscriptionsIE(YoutubeFeedsInfoExtractor):
    IE_DESC: str

class YoutubeHistoryIE(YoutubeFeedsInfoExtractor):
    IE_DESC: str

class YoutubeTruncatedURLIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: bool

class YoutubeTruncatedIDIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: bool
