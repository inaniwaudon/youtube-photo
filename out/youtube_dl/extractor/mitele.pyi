from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601
from .telecinco import TelecincoIE as TelecincoIE

class MiTeleIE(TelecincoIE):
    IE_DESC: str
