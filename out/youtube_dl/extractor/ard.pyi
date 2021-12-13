from ..compat import compat_etree_fromstring as compat_etree_fromstring
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, parse_duration as parse_duration, qualities as qualities, str_or_none as str_or_none, try_get as try_get, unified_strdate as unified_strdate, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor
from .generic import GenericIE as GenericIE

class ARDMediathekBaseIE(InfoExtractor): ...

class ARDMediathekIE(ARDMediathekBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class ARDIE(InfoExtractor): ...
class ARDBetaMediathekIE(ARDMediathekBaseIE): ...
