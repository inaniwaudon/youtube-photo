from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, extract_attributes as extract_attributes, int_or_none as int_or_none, parse_age_limit as parse_age_limit, remove_end as remove_end, unescapeHTML as unescapeHTML, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class DiscoveryGoBaseIE(InfoExtractor): ...
class DiscoveryGoIE(DiscoveryGoBaseIE): ...

class DiscoveryGoPlaylistIE(DiscoveryGoBaseIE):
    @classmethod
    def suitable(cls, url): ...
