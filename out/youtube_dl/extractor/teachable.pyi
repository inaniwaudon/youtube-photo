from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, get_element_by_class as get_element_by_class, int_or_none as int_or_none, strip_or_none as strip_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from .wistia import WistiaIE as WistiaIE

class TeachableBaseIE(InfoExtractor): ...
class TeachableIE(TeachableBaseIE): ...

class TeachableCourseIE(TeachableBaseIE):
    @classmethod
    def suitable(cls, url): ...
