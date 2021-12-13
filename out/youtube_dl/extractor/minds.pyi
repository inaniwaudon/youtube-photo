from ..compat import compat_str as compat_str
from ..utils import clean_html as clean_html, int_or_none as int_or_none, str_or_none as str_or_none, strip_or_none as strip_or_none
from .common import InfoExtractor as InfoExtractor
from typing import Any

class MindsBaseIE(InfoExtractor): ...

class MindsIE(MindsBaseIE):
    IE_NAME: str

class MindsFeedBaseIE(MindsBaseIE): ...

class MindsChannelIE(MindsFeedBaseIE):
    IE_NAME: Any

class MindsGroupIE(MindsFeedBaseIE):
    IE_NAME: Any
