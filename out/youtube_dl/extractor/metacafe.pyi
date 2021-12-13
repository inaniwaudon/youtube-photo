from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse as compat_urllib_parse, compat_urllib_parse_unquote as compat_urllib_parse_unquote
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, get_element_by_attribute as get_element_by_attribute, int_or_none as int_or_none, mimetype2ext as mimetype2ext
from .common import InfoExtractor as InfoExtractor

class MetacafeIE(InfoExtractor):
    IE_NAME: str
    def report_disclaimer(self) -> None: ...
