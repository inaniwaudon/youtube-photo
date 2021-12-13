from ..compat import compat_parse_qs as compat_parse_qs, compat_str as compat_str, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import OnDemandPagedList as OnDemandPagedList, int_or_none as int_or_none, merge_dicts as merge_dicts, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, try_get as try_get, update_url_query as update_url_query, urljoin as urljoin
from .turner import TurnerBaseIE as TurnerBaseIE

class NBACVPBaseIE(TurnerBaseIE): ...
class NBAWatchBaseIE(NBACVPBaseIE): ...

class NBAWatchEmbedIE(NBAWatchBaseIE):
    IENAME: str

class NBAWatchIE(NBAWatchBaseIE):
    IE_NAME: str

class NBAWatchCollectionIE(NBAWatchBaseIE):
    IE_NAME: str

class NBABaseIE(NBACVPBaseIE): ...

class NBAEmbedIE(NBABaseIE):
    IENAME: str

class NBAIE(NBABaseIE):
    IENAME: str

class NBAChannelIE(NBABaseIE):
    IENAME: str
