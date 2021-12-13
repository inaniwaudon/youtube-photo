from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, orderedSet as orderedSet, str_or_none as str_or_none
from .common import InfoExtractor as InfoExtractor

class GloboIE(InfoExtractor): ...

class GloboArticleIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
