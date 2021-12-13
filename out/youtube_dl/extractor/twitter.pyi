from ..compat import compat_HTTPError as compat_HTTPError, compat_parse_qs as compat_parse_qs, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import ExtractorError as ExtractorError, dict_get as dict_get, float_or_none as float_or_none, int_or_none as int_or_none, strip_or_none as strip_or_none, try_get as try_get, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor
from .periscope import PeriscopeBaseIE as PeriscopeBaseIE, PeriscopeIE as PeriscopeIE

class TwitterBaseIE(InfoExtractor): ...

class TwitterCardIE(InfoExtractor):
    IE_NAME: str

class TwitterIE(TwitterBaseIE):
    IE_NAME: str

class TwitterAmplifyIE(TwitterBaseIE):
    IE_NAME: str

class TwitterBroadcastIE(TwitterBaseIE, PeriscopeBaseIE):
    IE_NAME: str
