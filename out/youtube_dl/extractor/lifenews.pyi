from ..compat import compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, remove_end as remove_end
from .common import InfoExtractor as InfoExtractor

class LifeNewsIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class LifeEmbedIE(InfoExtractor):
    IE_NAME: str
