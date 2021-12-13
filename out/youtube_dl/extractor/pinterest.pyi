from ..compat import compat_str as compat_str
from ..utils import determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, try_get as try_get, unified_timestamp as unified_timestamp, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class PinterestBaseIE(InfoExtractor): ...
class PinterestIE(PinterestBaseIE): ...

class PinterestCollectionIE(PinterestBaseIE):
    @classmethod
    def suitable(cls, url): ...
