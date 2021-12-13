from ..compat import compat_HTTPError as compat_HTTPError
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class VidmeIE(InfoExtractor):
    IE_NAME: str

class VidmeListBaseIE(InfoExtractor): ...

class VidmeUserIE(VidmeListBaseIE):
    IE_NAME: str

class VidmeUserLikesIE(VidmeListBaseIE):
    IE_NAME: str
