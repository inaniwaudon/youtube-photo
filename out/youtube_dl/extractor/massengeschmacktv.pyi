from ..utils import clean_html as clean_html, determine_ext as determine_ext, int_or_none as int_or_none, js_to_json as js_to_json, mimetype2ext as mimetype2ext, parse_filesize as parse_filesize
from .common import InfoExtractor as InfoExtractor

class MassengeschmackTVIE(InfoExtractor):
    IE_NAME: str
