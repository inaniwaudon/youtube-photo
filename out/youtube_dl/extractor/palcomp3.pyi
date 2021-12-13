from ..compat import compat_str as compat_str
from ..utils import int_or_none as int_or_none, str_or_none as str_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class PalcoMP3BaseIE(InfoExtractor): ...

class PalcoMP3IE(PalcoMP3BaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PalcoMP3ArtistIE(PalcoMP3BaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PalcoMP3VideoIE(PalcoMP3BaseIE):
    IE_NAME: str
