from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, get_element_by_attribute as get_element_by_attribute, parse_iso8601 as parse_iso8601, remove_end as remove_end
from .common import InfoExtractor as InfoExtractor

class XuiteIE(InfoExtractor):
    IE_DESC: str
