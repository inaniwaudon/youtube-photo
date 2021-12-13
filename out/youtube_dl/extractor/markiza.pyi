from ..compat import compat_str as compat_str
from ..utils import orderedSet as orderedSet, parse_duration as parse_duration, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class MarkizaIE(InfoExtractor): ...

class MarkizaPageIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
