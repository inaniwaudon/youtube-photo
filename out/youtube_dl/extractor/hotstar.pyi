from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, str_or_none as str_or_none, try_get as try_get, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class HotStarBaseIE(InfoExtractor): ...

class HotStarIE(HotStarBaseIE):
    IE_NAME: str

class HotStarPlaylistIE(HotStarBaseIE):
    IE_NAME: str
