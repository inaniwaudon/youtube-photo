from ..utils import clean_html as clean_html, extract_attributes as extract_attributes, unified_strdate as unified_strdate, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class ArchiveOrgIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
