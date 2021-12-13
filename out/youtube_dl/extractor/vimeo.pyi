from ..compat import compat_HTTPError as compat_HTTPError, compat_kwargs as compat_kwargs, compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, determine_ext as determine_ext, get_element_by_class as get_element_by_class, int_or_none as int_or_none, js_to_json as js_to_json, merge_dicts as merge_dicts, parse_filesize as parse_filesize, parse_iso8601 as parse_iso8601, sanitized_Request as sanitized_Request, smuggle_url as smuggle_url, std_headers as std_headers, str_or_none as str_or_none, try_get as try_get, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, unsmuggle_url as unsmuggle_url, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class VimeoBaseInfoExtractor(InfoExtractor): ...

class VimeoIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoOndemandIE(VimeoIE):
    IE_NAME: str

class VimeoChannelIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoUserIE(VimeoChannelIE):
    IE_NAME: str

class VimeoAlbumIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoGroupsIE(VimeoChannelIE):
    IE_NAME: str

class VimeoReviewIE(VimeoBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class VimeoWatchLaterIE(VimeoChannelIE):
    IE_NAME: str
    IE_DESC: str

class VimeoLikesIE(VimeoChannelIE):
    IE_NAME: str
    IE_DESC: str

class VHXEmbedIE(VimeoBaseInfoExtractor):
    IE_NAME: str
