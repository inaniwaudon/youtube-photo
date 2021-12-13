from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, find_xpath_attr as find_xpath_attr, int_or_none as int_or_none, js_to_json as js_to_json, orderedSet as orderedSet, parse_age_limit as parse_age_limit, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, smuggle_url as smuggle_url, strip_or_none as strip_or_none, try_get as try_get, xpath_element as xpath_element, xpath_text as xpath_text, xpath_with_ns as xpath_with_ns
from .common import InfoExtractor as InfoExtractor

class CBCIE(InfoExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class CBCPlayerIE(InfoExtractor):
    IE_NAME: str

class CBCWatchBaseIE(InfoExtractor): ...

class CBCWatchVideoIE(CBCWatchBaseIE):
    IE_NAME: str

class CBCWatchIE(CBCWatchBaseIE):
    IE_NAME: str

class CBCOlympicsIE(InfoExtractor):
    IE_NAME: str
