from ..utils import smuggle_url as smuggle_url, urlencode_postdata as urlencode_postdata, xpath_text as xpath_text
from .anvato import AnvatoIE as AnvatoIE
from .aws import AWSIE as AWSIE
from .common import InfoExtractor as InfoExtractor

class ScrippsNetworksWatchIE(AWSIE):
    IE_NAME: str

class ScrippsNetworksIE(InfoExtractor): ...
