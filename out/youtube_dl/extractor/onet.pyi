from ..utils import ExtractorError as ExtractorError, NO_DEFAULT as NO_DEFAULT, determine_ext as determine_ext, float_or_none as float_or_none, get_element_by_class as get_element_by_class, int_or_none as int_or_none, js_to_json as js_to_json, parse_iso8601 as parse_iso8601, remove_start as remove_start, strip_or_none as strip_or_none, url_basename as url_basename
from .common import InfoExtractor as InfoExtractor

class OnetBaseIE(InfoExtractor): ...
class OnetMVPIE(OnetBaseIE): ...

class OnetIE(OnetBaseIE):
    IE_NAME: str

class OnetChannelIE(OnetBaseIE):
    IE_NAME: str

class OnetPlIE(InfoExtractor):
    IE_NAME: str
