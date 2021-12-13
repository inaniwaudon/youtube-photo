from ..utils import ExtractorError as ExtractorError, js_to_json as js_to_json, unified_strdate as unified_strdate, update_url_query as update_url_query, urlencode_postdata as urlencode_postdata, xpath_element as xpath_element, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class Laola1TvEmbedIE(InfoExtractor):
    IE_NAME: str

class Laola1TvBaseIE(Laola1TvEmbedIE): ...

class Laola1TvIE(Laola1TvBaseIE):
    IE_NAME: str

class EHFTVIE(Laola1TvBaseIE):
    IE_NAME: str

class ITTFIE(InfoExtractor): ...
