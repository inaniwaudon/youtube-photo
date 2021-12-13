from ..compat import compat_kwargs as compat_kwargs, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor

class ViuBaseIE(InfoExtractor): ...
class ViuIE(ViuBaseIE): ...

class ViuPlaylistIE(ViuBaseIE):
    IE_NAME: str

class ViuOTTIE(InfoExtractor):
    IE_NAME: str
