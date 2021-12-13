from typing import Any, ClassVar

littlecms_version: str

class CmsProfile:
    attributes: ClassVar[getset_descriptor] = ...
    blue_colorant: ClassVar[getset_descriptor] = ...
    blue_primary: ClassVar[getset_descriptor] = ...
    chromatic_adaptation: ClassVar[getset_descriptor] = ...
    chromaticity: ClassVar[getset_descriptor] = ...
    clut: ClassVar[getset_descriptor] = ...
    colorant_table: ClassVar[getset_descriptor] = ...
    colorant_table_out: ClassVar[getset_descriptor] = ...
    colorimetric_intent: ClassVar[getset_descriptor] = ...
    connection_space: ClassVar[getset_descriptor] = ...
    copyright: ClassVar[getset_descriptor] = ...
    creation_date: ClassVar[getset_descriptor] = ...
    device_class: ClassVar[getset_descriptor] = ...
    green_colorant: ClassVar[getset_descriptor] = ...
    green_primary: ClassVar[getset_descriptor] = ...
    header_flags: ClassVar[getset_descriptor] = ...
    header_manufacturer: ClassVar[getset_descriptor] = ...
    header_model: ClassVar[getset_descriptor] = ...
    icc_measurement_condition: ClassVar[getset_descriptor] = ...
    icc_version: ClassVar[getset_descriptor] = ...
    icc_viewing_condition: ClassVar[getset_descriptor] = ...
    intent_supported: ClassVar[getset_descriptor] = ...
    is_matrix_shaper: ClassVar[getset_descriptor] = ...
    luminance: ClassVar[getset_descriptor] = ...
    manufacturer: ClassVar[getset_descriptor] = ...
    media_black_point: ClassVar[getset_descriptor] = ...
    media_white_point: ClassVar[getset_descriptor] = ...
    media_white_point_temperature: ClassVar[getset_descriptor] = ...
    model: ClassVar[getset_descriptor] = ...
    perceptual_rendering_intent_gamut: ClassVar[getset_descriptor] = ...
    profile_description: ClassVar[getset_descriptor] = ...
    profile_id: ClassVar[getset_descriptor] = ...
    red_colorant: ClassVar[getset_descriptor] = ...
    red_primary: ClassVar[getset_descriptor] = ...
    rendering_intent: ClassVar[getset_descriptor] = ...
    saturation_rendering_intent_gamut: ClassVar[getset_descriptor] = ...
    screening_description: ClassVar[getset_descriptor] = ...
    target: ClassVar[getset_descriptor] = ...
    technology: ClassVar[getset_descriptor] = ...
    version: ClassVar[getset_descriptor] = ...
    viewing_condition: ClassVar[getset_descriptor] = ...
    xcolor_space: ClassVar[getset_descriptor] = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def is_intent_supported(self, *args, **kwargs) -> Any: ...

def buildProofTransform(*args, **kwargs) -> Any: ...
def buildTransform(*args, **kwargs) -> Any: ...
def createProfile(*args, **kwargs) -> Any: ...
def profile_frombytes(*args, **kwargs) -> Any: ...
def profile_fromstring(*args, **kwargs) -> Any: ...
def profile_open(*args, **kwargs) -> Any: ...
def profile_tobytes(*args, **kwargs) -> Any: ...