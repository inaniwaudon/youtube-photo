from ..compat import compat_str as compat_str
from ..utils import try_get as try_get, unescapeHTML as unescapeHTML, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class WWEBaseIE(InfoExtractor): ...
class WWEIE(WWEBaseIE): ...

class WWEPlaylistIE(WWEBaseIE):
    @classmethod
    def suitable(cls, url): ...
