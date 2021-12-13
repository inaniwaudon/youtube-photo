from ..compat import compat_HTTPError as compat_HTTPError
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, extract_attributes as extract_attributes, float_or_none as float_or_none, get_element_by_class as get_element_by_class, int_or_none as int_or_none, merge_dicts as merge_dicts, str_or_none as str_or_none, strip_or_none as strip_or_none, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor
from .gigya import GigyaBaseIE as GigyaBaseIE

class CanvasIE(InfoExtractor): ...

class CanvasEenIE(InfoExtractor):
    IE_DESC: str

class VrtNUIE(GigyaBaseIE):
    IE_DESC: str

class DagelijkseKostIE(InfoExtractor):
    IE_DESC: str
