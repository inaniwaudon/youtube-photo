from ..compat import compat_etree_fromstring as compat_etree_fromstring, compat_str as compat_str, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_urlparse as compat_urlparse, compat_xml_parse_error as compat_xml_parse_error
from ..utils import ExtractorError as ExtractorError, HEADRequest as HEADRequest, KNOWN_EXTENSIONS as KNOWN_EXTENSIONS, UnsupportedError as UnsupportedError, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, is_html as is_html, js_to_json as js_to_json, merge_dicts as merge_dicts, mimetype2ext as mimetype2ext, orderedSet as orderedSet, parse_duration as parse_duration, sanitized_Request as sanitized_Request, smuggle_url as smuggle_url, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, unsmuggle_url as unsmuggle_url, url_or_none as url_or_none, xpath_attr as xpath_attr, xpath_text as xpath_text, xpath_with_ns as xpath_with_ns
from .anvato import AnvatoIE as AnvatoIE
from .apa import APAIE as APAIE
from .arcpublishing import ArcPublishingIE as ArcPublishingIE
from .arkena import ArkenaIE as ArkenaIE
from .arte import ArteTVEmbedIE as ArteTVEmbedIE
from .brightcove import BrightcoveLegacyIE as BrightcoveLegacyIE, BrightcoveNewIE as BrightcoveNewIE
from .channel9 import Channel9IE as Channel9IE
from .cloudflarestream import CloudflareStreamIE as CloudflareStreamIE
from .common import InfoExtractor as InfoExtractor
from .commonprotocols import RtmpIE as RtmpIE
from .condenast import CondeNastIE as CondeNastIE
from .dailymail import DailyMailIE as DailyMailIE
from .dailymotion import DailymotionIE as DailymotionIE
from .dbtv import DBTVIE as DBTVIE
from .digiteka import DigitekaIE as DigitekaIE
from .drtuber import DrTuberIE as DrTuberIE
from .eagleplatform import EaglePlatformIE as EaglePlatformIE
from .expressen import ExpressenIE as ExpressenIE
from .facebook import FacebookIE as FacebookIE
from .foxnews import FoxNewsIE as FoxNewsIE
from .googledrive import GoogleDriveIE as GoogleDriveIE
from .indavideo import IndavideoEmbedIE as IndavideoEmbedIE
from .instagram import InstagramIE as InstagramIE
from .joj import JojIE as JojIE
from .jwplatform import JWPlatformIE as JWPlatformIE
from .kaltura import KalturaIE as KalturaIE
from .kinja import KinjaEmbedIE as KinjaEmbedIE
from .limelight import LimelightBaseIE as LimelightBaseIE
from .liveleak import LiveLeakIE as LiveLeakIE
from .medialaan import MedialaanIE as MedialaanIE
from .mediaset import MediasetIE as MediasetIE
from .mediasite import MediasiteIE as MediasiteIE
from .megaphone import MegaphoneIE as MegaphoneIE
from .mofosex import MofosexEmbedIE as MofosexEmbedIE
from .mtv import MTVServicesEmbeddedIE as MTVServicesEmbeddedIE
from .myvi import MyviIE as MyviIE
from .nbc import NBCSportsVPlayerIE as NBCSportsVPlayerIE
from .nexx import NexxEmbedIE as NexxEmbedIE, NexxIE as NexxIE
from .odnoklassniki import OdnoklassnikiIE as OdnoklassnikiIE
from .onionstudios import OnionStudiosIE as OnionStudiosIE
from .ooyala import OoyalaIE as OoyalaIE
from .peertube import PeerTubeIE as PeerTubeIE
from .piksel import PikselIE as PikselIE
from .pladform import PladformIE as PladformIE
from .pornhub import PornHubIE as PornHubIE
from .redtube import RedTubeIE as RedTubeIE
from .rutube import RutubeIE as RutubeIE
from .rutv import RUTVIE as RUTVIE
from .senateisvp import SenateISVPIE as SenateISVPIE
from .simplecast import SimplecastIE as SimplecastIE
from .soundcloud import SoundcloudEmbedIE as SoundcloudEmbedIE
from .spankwire import SpankwireIE as SpankwireIE
from .sportbox import SportBoxIE as SportBoxIE
from .springboardplatform import SpringboardPlatformIE as SpringboardPlatformIE
from .svt import SVTIE as SVTIE
from .teachable import TeachableIE as TeachableIE
from .theplatform import ThePlatformIE as ThePlatformIE
from .threeqsdn import ThreeQSDNIE as ThreeQSDNIE
from .tnaflix import TNAFlixNetworkEmbedIE as TNAFlixNetworkEmbedIE
from .tube8 import Tube8IE as Tube8IE
from .tunein import TuneInBaseIE as TuneInBaseIE
from .tvc import TVCIE as TVCIE
from .twentymin import TwentyMinutenIE as TwentyMinutenIE
from .udn import UDNEmbedIE as UDNEmbedIE
from .ustream import UstreamIE as UstreamIE
from .vbox7 import Vbox7IE as Vbox7IE
from .vice import ViceIE as ViceIE
from .videa import VideaIE as VideaIE
from .videomore import VideomoreIE as VideomoreIE
from .videopress import VideoPressIE as VideoPressIE
from .viewlift import ViewLiftEmbedIE as ViewLiftEmbedIE
from .vimeo import VHXEmbedIE as VHXEmbedIE, VimeoIE as VimeoIE
from .viqeo import ViqeoIE as ViqeoIE
from .vk import VKIE as VKIE
from .vshare import VShareIE as VShareIE
from .vzaar import VzaarIE as VzaarIE
from .washingtonpost import WashingtonPostIE as WashingtonPostIE
from .webcaster import WebcasterFeedIE as WebcasterFeedIE
from .wistia import WistiaIE as WistiaIE
from .xfileshare import XFileShareIE as XFileShareIE
from .xhamster import XHamsterEmbedIE as XHamsterEmbedIE
from .yapfiles import YapFilesIE as YapFilesIE
from .youporn import YouPornIE as YouPornIE
from .youtube import YoutubeIE as YoutubeIE
from .zype import ZypeIE as ZypeIE

class GenericIE(InfoExtractor):
    IE_DESC: str
    IE_NAME: str
    def report_following_redirect(self, new_url) -> None: ...
