from ..compat import compat_urllib_parse_unquote as compat_urllib_parse_unquote
from ..utils import int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor

class XiamiBaseIE(InfoExtractor): ...

class XiamiSongIE(XiamiBaseIE):
    IE_NAME: str
    IE_DESC: str

class XiamiPlaylistBaseIE(XiamiBaseIE): ...

class XiamiAlbumIE(XiamiPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class XiamiArtistIE(XiamiPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class XiamiCollectionIE(XiamiPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str
