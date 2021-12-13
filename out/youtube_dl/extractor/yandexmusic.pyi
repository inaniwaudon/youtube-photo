from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class YandexMusicBaseIE(InfoExtractor): ...

class YandexMusicTrackIE(YandexMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class YandexMusicPlaylistBaseIE(YandexMusicBaseIE): ...

class YandexMusicAlbumIE(YandexMusicPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class YandexMusicPlaylistIE(YandexMusicPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class YandexMusicArtistBaseIE(YandexMusicPlaylistBaseIE): ...

class YandexMusicArtistTracksIE(YandexMusicArtistBaseIE):
    IE_NAME: str
    IE_DESC: str

class YandexMusicArtistAlbumsIE(YandexMusicArtistBaseIE):
    IE_NAME: str
    IE_DESC: str
