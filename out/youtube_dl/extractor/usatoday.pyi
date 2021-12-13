from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, get_element_by_attribute as get_element_by_attribute, parse_duration as parse_duration, try_get as try_get, update_url_query as update_url_query
from .common import InfoExtractor as InfoExtractor

class USATodayIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str
