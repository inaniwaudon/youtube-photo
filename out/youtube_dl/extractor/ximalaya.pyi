from .common import InfoExtractor as InfoExtractor

class XimalayaBaseIE(InfoExtractor): ...

class XimalayaIE(XimalayaBaseIE):
    IE_NAME: str
    IE_DESC: str

class XimalayaAlbumIE(XimalayaBaseIE):
    IE_NAME: str
    IE_DESC: str
