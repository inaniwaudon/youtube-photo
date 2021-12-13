from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, get_element_by_attribute as get_element_by_attribute, int_or_none as int_or_none, lowercase_escape as lowercase_escape, std_headers as std_headers, try_get as try_get, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class InstagramIE(InfoExtractor): ...
class InstagramPlaylistIE(InfoExtractor): ...

class InstagramUserIE(InstagramPlaylistIE):
    IE_DESC: str
    IE_NAME: str

class InstagramTagIE(InstagramPlaylistIE):
    IE_DESC: str
    IE_NAME: str
