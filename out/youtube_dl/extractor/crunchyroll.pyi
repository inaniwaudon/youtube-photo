from ..aes import aes_cbc_decrypt as aes_cbc_decrypt
from ..compat import compat_b64decode as compat_b64decode, compat_etree_Element as compat_etree_Element, compat_etree_fromstring as compat_etree_fromstring, compat_str as compat_str, compat_urllib_parse_urlencode as compat_urllib_parse_urlencode, compat_urllib_request as compat_urllib_request, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, bytes_to_intlist as bytes_to_intlist, extract_attributes as extract_attributes, float_or_none as float_or_none, int_or_none as int_or_none, intlist_to_bytes as intlist_to_bytes, lowercase_escape as lowercase_escape, merge_dicts as merge_dicts, remove_end as remove_end, sanitized_Request as sanitized_Request, urlencode_postdata as urlencode_postdata, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor
from .vrv import VRVIE as VRVIE

class CrunchyrollBaseIE(InfoExtractor): ...

class CrunchyrollIE(CrunchyrollBaseIE, VRVIE):
    IE_NAME: str

class CrunchyrollShowPlaylistIE(CrunchyrollBaseIE):
    IE_NAME: str
