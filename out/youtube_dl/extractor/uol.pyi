from ..compat import compat_str as compat_str, compat_urllib_parse_urlencode as compat_urllib_parse_urlencode
from ..utils import clean_html as clean_html, int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, qualities as qualities, update_url_query as update_url_query
from .common import InfoExtractor as InfoExtractor

class UOLIE(InfoExtractor):
    IE_NAME: str
