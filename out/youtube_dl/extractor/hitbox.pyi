from ..utils import clean_html as clean_html, compat_str as compat_str, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class HitboxIE(InfoExtractor):
    IE_NAME: str

class HitboxLiveIE(HitboxIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
