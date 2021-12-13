from ..compat import compat_HTTPError as compat_HTTPError, compat_urllib_parse as compat_urllib_parse, compat_urllib_parse_urlencode as compat_urllib_parse_urlencode
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor

class VRVBaseIE(InfoExtractor): ...

class VRVIE(VRVBaseIE):
    IE_NAME: str

class VRVSeriesIE(VRVBaseIE):
    IE_NAME: str
