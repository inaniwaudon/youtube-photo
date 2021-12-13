from .common import InfoExtractor as InfoExtractor

class WashingtonPostIE(InfoExtractor):
    IE_NAME: str

class WashingtonPostArticleIE(InfoExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
