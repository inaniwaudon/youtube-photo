from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, merge_dicts as merge_dicts, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class ProSiebenSat1BaseIE(InfoExtractor): ...

class ProSiebenSat1IE(ProSiebenSat1BaseIE):
    IE_NAME: str
    IE_DESC: str
