from ..utils import ExtractorError as ExtractorError, js_to_json as js_to_json
from .common import InfoExtractor as InfoExtractor

class PicartoIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...

class PicartoVodIE(InfoExtractor): ...
