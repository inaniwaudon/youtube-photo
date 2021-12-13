from ..compat import compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, InAdvancePagedList as InAdvancePagedList, orderedSet as orderedSet, str_to_int as str_to_int, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class MotherlessIE(InfoExtractor): ...

class MotherlessGroupIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
