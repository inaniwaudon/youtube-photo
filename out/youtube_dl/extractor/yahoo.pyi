from ..compat import compat_str as compat_str, compat_urllib_parse as compat_urllib_parse
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, smuggle_url as smuggle_url, try_get as try_get, url_or_none as url_or_none
from .brightcove import BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor, SearchInfoExtractor as SearchInfoExtractor

class YahooIE(InfoExtractor):
    IE_DESC: str

class YahooSearchIE(SearchInfoExtractor):
    IE_DESC: str
    IE_NAME: str

class YahooGyaOPlayerIE(InfoExtractor):
    IE_NAME: str

class YahooGyaOIE(InfoExtractor):
    IE_NAME: str

class YahooJapanNewsIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
