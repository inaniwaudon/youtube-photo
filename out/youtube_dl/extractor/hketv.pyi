from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, merge_dicts as merge_dicts, parse_count as parse_count, str_or_none as str_or_none, try_get as try_get, unified_strdate as unified_strdate, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class HKETVIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
