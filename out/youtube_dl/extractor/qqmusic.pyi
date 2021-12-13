from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, strip_jsonp as strip_jsonp, unescapeHTML as unescapeHTML
from .common import InfoExtractor as InfoExtractor

class QQMusicIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    @staticmethod
    def m_r_get_ruin(): ...

class QQPlaylistBaseIE(InfoExtractor):
    @staticmethod
    def qq_static_url(category, mid): ...
    def get_singer_all_songs(self, singmid, num): ...
    def get_entries_from_page(self, singmid): ...

class QQMusicSingerIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicAlbumIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicToplistIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicPlaylistIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str
