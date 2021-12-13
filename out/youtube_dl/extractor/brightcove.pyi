from ..compat import compat_HTTPError as compat_HTTPError, compat_etree_fromstring as compat_etree_fromstring, compat_parse_qs as compat_parse_qs, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse, compat_urlparse as compat_urlparse, compat_xml_parse_error as compat_xml_parse_error
from ..utils import ExtractorError as ExtractorError, UnsupportedError as UnsupportedError, clean_html as clean_html, extract_attributes as extract_attributes, find_xpath_attr as find_xpath_attr, fix_xml_ampersands as fix_xml_ampersands, float_or_none as float_or_none, int_or_none as int_or_none, js_to_json as js_to_json, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, smuggle_url as smuggle_url, str_or_none as str_or_none, try_get as try_get, unescapeHTML as unescapeHTML, unsmuggle_url as unsmuggle_url, update_url_query as update_url_query, url_or_none as url_or_none
from .adobepass import AdobePassIE as AdobePassIE
from .common import InfoExtractor as InfoExtractor

class BrightcoveLegacyIE(InfoExtractor):
    IE_NAME: str

class BrightcoveNewIE(AdobePassIE):
    IE_NAME: str
