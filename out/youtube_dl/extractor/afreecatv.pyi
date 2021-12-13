from ..compat import compat_xpath as compat_xpath
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class AfreecaTVIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    @staticmethod
    def parse_video_key(key): ...
