from ..utils import ExtractorError as ExtractorError, find_xpath_attr as find_xpath_attr, int_or_none as int_or_none, update_url_query as update_url_query, xpath_element as xpath_element, xpath_text as xpath_text
from .theplatform import ThePlatformFeedIE as ThePlatformFeedIE

class CBSBaseIE(ThePlatformFeedIE): ...
class CBSIE(CBSBaseIE): ...
