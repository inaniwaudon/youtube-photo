from ..compat import compat_b64decode as compat_b64decode, compat_urllib_parse_unquote_plus as compat_urllib_parse_unquote_plus
from ..utils import ExtractorError as ExtractorError, KNOWN_EXTENSIONS as KNOWN_EXTENSIONS, determine_ext as determine_ext, int_or_none as int_or_none, js_to_json as js_to_json, parse_filesize as parse_filesize, rot47 as rot47, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class SharedBaseIE(InfoExtractor): ...

class SharedIE(SharedBaseIE):
    IE_DESC: str

class VivoIE(SharedBaseIE):
    IE_DESC: str
