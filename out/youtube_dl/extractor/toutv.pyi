from ..compat import compat_HTTPError as compat_HTTPError
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, merge_dicts as merge_dicts
from .radiocanada import RadioCanadaIE as RadioCanadaIE

class TouTvIE(RadioCanadaIE):
    IE_NAME: str
