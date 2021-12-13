from ..compat import compat_str as compat_str
from ..utils import determine_ext as determine_ext, dict_get as dict_get, int_or_none as int_or_none, str_or_none as str_or_none, strip_or_none as strip_or_none, try_get as try_get, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class SVTBaseIE(InfoExtractor): ...
class SVTIE(SVTBaseIE): ...
class SVTPlayBaseIE(SVTBaseIE): ...

class SVTPlayIE(SVTPlayBaseIE):
    IE_DESC: str

class SVTSeriesIE(SVTPlayBaseIE):
    @classmethod
    def suitable(cls, url): ...

class SVTPageIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
