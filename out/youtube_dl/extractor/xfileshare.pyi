from ..compat import compat_chr as compat_chr
from ..utils import ExtractorError as ExtractorError, decode_packed_codes as decode_packed_codes, determine_ext as determine_ext, int_or_none as int_or_none, js_to_json as js_to_json, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor
from typing import Any

def aa_decode(aa_code): ...

class XFileShareIE(InfoExtractor):
    IE_DESC: Any
