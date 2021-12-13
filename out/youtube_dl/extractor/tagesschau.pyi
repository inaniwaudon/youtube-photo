from ..utils import determine_ext as determine_ext, js_to_json as js_to_json, parse_filesize as parse_filesize, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class TagesschauPlayerIE(InfoExtractor):
    IE_NAME: str

class TagesschauIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
