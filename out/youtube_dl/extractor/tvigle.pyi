from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, parse_age_limit as parse_age_limit, try_get as try_get, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class TvigleIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
