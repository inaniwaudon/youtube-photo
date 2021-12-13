from ..compat import compat_itertools_count as compat_itertools_count, compat_str as compat_str, compat_urllib_parse_urlencode as compat_urllib_parse_urlencode
from ..utils import float_or_none as float_or_none, sanitized_Request as sanitized_Request
from .common import InfoExtractor as InfoExtractor

class NetEaseMusicBaseIE(InfoExtractor):
    def extract_formats(self, info): ...
    @classmethod
    def convert_milliseconds(cls, ms): ...
    def query_api(self, endpoint, video_id, note): ...

class NetEaseMusicIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicAlbumIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicSingerIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicListIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicMvIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicProgramIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicDjRadioIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str
