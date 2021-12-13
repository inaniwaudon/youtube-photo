from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, sanitized_Request as sanitized_Request
from .brightcove import BrightcoveLegacyIE as BrightcoveLegacyIE, BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor

class NownessBaseIE(InfoExtractor): ...

class NownessIE(NownessBaseIE):
    IE_NAME: str

class NownessPlaylistIE(NownessBaseIE):
    IE_NAME: str

class NownessSeriesIE(NownessBaseIE):
    IE_NAME: str
