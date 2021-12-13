from ..utils import ExtractorError as ExtractorError, get_element_by_attribute as get_element_by_attribute
from .ard import ARDMediathekBaseIE as ARDMediathekBaseIE

class SRMediathekIE(ARDMediathekBaseIE):
    IE_NAME: str
    IE_DESC: str
