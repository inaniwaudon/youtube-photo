from ..utils import ExtractorError as ExtractorError, GeoRestrictedError as GeoRestrictedError, int_or_none as int_or_none, update_url_query as update_url_query, urlencode_postdata as urlencode_postdata
from .theplatform import ThePlatformIE as ThePlatformIE

class AENetworksBaseIE(ThePlatformIE): ...

class AENetworksIE(AENetworksBaseIE):
    IE_NAME: str
    IE_DESC: str

class AENetworksListBaseIE(AENetworksBaseIE): ...

class AENetworksCollectionIE(AENetworksListBaseIE):
    IE_NAME: str

class AENetworksShowIE(AENetworksListBaseIE):
    IE_NAME: str

class HistoryTopicIE(AENetworksBaseIE):
    IE_NAME: str
    IE_DESC: str

class HistoryPlayerIE(AENetworksBaseIE):
    IE_NAME: str

class BiographyIE(AENetworksBaseIE): ...
