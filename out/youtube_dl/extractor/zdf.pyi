from ..compat import compat_str as compat_str
from ..utils import NO_DEFAULT as NO_DEFAULT, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, merge_dicts as merge_dicts, orderedSet as orderedSet, parse_codecs as parse_codecs, qualities as qualities, try_get as try_get, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class ZDFBaseIE(InfoExtractor): ...
class ZDFIE(ZDFBaseIE): ...

class ZDFChannelIE(ZDFBaseIE):
    @classmethod
    def suitable(cls, url): ...
