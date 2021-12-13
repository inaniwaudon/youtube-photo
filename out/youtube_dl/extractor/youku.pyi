from ..utils import ExtractorError as ExtractorError, get_element_by_class as get_element_by_class, js_to_json as js_to_json, str_or_none as str_or_none, strip_jsonp as strip_jsonp
from .common import InfoExtractor as InfoExtractor

class YoukuIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    @staticmethod
    def get_ysuid(): ...
    def get_format_name(self, fm): ...

class YoukuShowIE(InfoExtractor):
    IE_NAME: str
