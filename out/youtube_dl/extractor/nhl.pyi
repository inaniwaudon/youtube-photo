from ..compat import compat_str as compat_str
from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class NHLBaseIE(InfoExtractor): ...

class NHLIE(NHLBaseIE):
    IE_NAME: str
