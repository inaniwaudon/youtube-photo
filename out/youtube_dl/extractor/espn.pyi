from ..compat import compat_str as compat_str
from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor
from .once import OnceIE as OnceIE

class ESPNIE(OnceIE): ...

class ESPNArticleIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...

class FiveThirtyEightIE(InfoExtractor): ...
