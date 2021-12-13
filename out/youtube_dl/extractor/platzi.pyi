from ..compat import compat_b64decode as compat_b64decode, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, str_or_none as str_or_none, try_get as try_get, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class PlatziBaseIE(InfoExtractor): ...
class PlatziIE(PlatziBaseIE): ...

class PlatziCourseIE(PlatziBaseIE):
    @classmethod
    def suitable(cls, url): ...
