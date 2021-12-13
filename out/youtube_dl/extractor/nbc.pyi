from ..compat import compat_urllib_parse_unquote as compat_urllib_parse_unquote
from ..utils import int_or_none as int_or_none, parse_duration as parse_duration, smuggle_url as smuggle_url, try_get as try_get, unified_timestamp as unified_timestamp, update_url_query as update_url_query
from .adobepass import AdobePassIE as AdobePassIE
from .common import InfoExtractor as InfoExtractor
from .theplatform import ThePlatformIE as ThePlatformIE

class NBCIE(AdobePassIE): ...
class NBCSportsVPlayerIE(InfoExtractor): ...
class NBCSportsIE(InfoExtractor): ...
class NBCSportsStreamIE(AdobePassIE): ...
class NBCNewsIE(ThePlatformIE): ...

class NBCOlympicsIE(InfoExtractor):
    IE_NAME: str

class NBCOlympicsStreamIE(AdobePassIE):
    IE_NAME: str
