from ..utils import clean_html as clean_html, determine_ext as determine_ext, int_or_none as int_or_none, js_to_json as js_to_json, qualities as qualities, unified_strdate as unified_strdate, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class NovaEmbedIE(InfoExtractor): ...

class NovaIE(InfoExtractor):
    IE_DESC: str
