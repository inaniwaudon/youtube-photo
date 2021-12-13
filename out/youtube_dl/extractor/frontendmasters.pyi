from ..compat import compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, parse_duration as parse_duration, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class FrontendMastersBaseIE(InfoExtractor): ...
class FrontendMastersPageBaseIE(FrontendMastersBaseIE): ...
class FrontendMastersIE(FrontendMastersBaseIE): ...
class FrontendMastersLessonIE(FrontendMastersPageBaseIE): ...

class FrontendMastersCourseIE(FrontendMastersPageBaseIE):
    @classmethod
    def suitable(cls, url): ...