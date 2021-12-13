from .common import InfoExtractor as InfoExtractor

class OnceIE(InfoExtractor):
    ADAPTIVE_URL_TEMPLATE: str
    PROGRESSIVE_URL_TEMPLATE: str
