from ..compat import compat_urllib_parse_urlparse as compat_urllib_parse_urlparse, compat_urlparse as compat_urlparse
from ..utils import determine_ext as determine_ext, extract_attributes as extract_attributes, int_or_none as int_or_none, js_to_json as js_to_json, mimetype2ext as mimetype2ext, orderedSet as orderedSet, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor
from typing import Any

class CondeNastIE(InfoExtractor):
    IE_DESC: Any
    EMBED_URL: Any
