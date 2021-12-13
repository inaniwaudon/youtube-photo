from ..compat import compat_etree_fromstring as compat_etree_fromstring, compat_http_client as compat_http_client, compat_str as compat_str, compat_urllib_error as compat_urllib_error, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_urllib_parse_unquote_plus as compat_urllib_parse_unquote_plus
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, error_to_compat_str as error_to_compat_str, float_or_none as float_or_none, get_element_by_id as get_element_by_id, int_or_none as int_or_none, js_to_json as js_to_json, limit_length as limit_length, parse_count as parse_count, qualities as qualities, sanitized_Request as sanitized_Request, try_get as try_get, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class FacebookIE(InfoExtractor):
    IE_NAME: str

class FacebookPluginsVideoIE(InfoExtractor): ...
