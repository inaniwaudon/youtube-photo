from ..utils import clean_html as clean_html, clean_podcast_url as clean_podcast_url, int_or_none as int_or_none, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class ACastBaseIE(InfoExtractor): ...

class ACastIE(ACastBaseIE):
    IE_NAME: str

class ACastChannelIE(ACastBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
