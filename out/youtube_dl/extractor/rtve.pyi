from ..compat import compat_b64decode as compat_b64decode, compat_struct_unpack as compat_struct_unpack
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, float_or_none as float_or_none, qualities as qualities, remove_end as remove_end, remove_start as remove_start, std_headers as std_headers
from .common import InfoExtractor as InfoExtractor

class RTVEALaCartaIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class RTVEInfantilIE(RTVEALaCartaIE):
    IE_NAME: str
    IE_DESC: str

class RTVELiveIE(RTVEALaCartaIE):
    IE_NAME: str
    IE_DESC: str

class RTVETelevisionIE(InfoExtractor):
    IE_NAME: str
