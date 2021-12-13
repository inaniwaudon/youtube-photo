from ..compat import compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, int_or_none as int_or_none, parse_duration as parse_duration, try_get as try_get, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from .dailymotion import DailymotionIE as DailymotionIE

class FranceTVBaseInfoExtractor(InfoExtractor): ...
class FranceTVIE(InfoExtractor): ...
class FranceTVSiteIE(FranceTVBaseInfoExtractor): ...
class FranceTVEmbedIE(FranceTVBaseInfoExtractor): ...

class FranceTVInfoIE(FranceTVBaseInfoExtractor):
    IE_NAME: str

class FranceTVInfoSportIE(FranceTVBaseInfoExtractor):
    IE_NAME: str

class GenerationWhatIE(InfoExtractor):
    IE_NAME: str

class CultureboxIE(FranceTVBaseInfoExtractor): ...
class FranceTVJeunesseIE(FranceTVBaseInfoExtractor): ...
