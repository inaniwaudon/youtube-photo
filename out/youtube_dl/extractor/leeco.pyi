from ..compat import compat_b64decode as compat_b64decode, compat_ord as compat_ord, compat_str as compat_str, compat_urllib_parse_urlencode as compat_urllib_parse_urlencode
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, encode_data_uri as encode_data_uri, int_or_none as int_or_none, orderedSet as orderedSet, parse_iso8601 as parse_iso8601, str_or_none as str_or_none, url_basename as url_basename, urshift as urshift
from .common import InfoExtractor as InfoExtractor

class LeIE(InfoExtractor):
    IE_DESC: str
    def ror(self, param1, param2): ...
    def calc_time_key(self, param1): ...
    @staticmethod
    def decrypt_m3u8(encrypted_data): ...

class LePlaylistIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...

class LetvCloudIE(InfoExtractor):
    IE_DESC: str
    @staticmethod
    def sign_data(obj) -> None: ...
