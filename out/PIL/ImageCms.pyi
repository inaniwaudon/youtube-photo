from ._util import deferred_error as deferred_error
from PIL import Image as Image
from typing import Any

DESCRIPTION: str
VERSION: str
core: Any
INTENT_PERCEPTUAL: int
INTENT_RELATIVE_COLORIMETRIC: int
INTENT_SATURATION: int
INTENT_ABSOLUTE_COLORIMETRIC: int
DIRECTION_INPUT: int
DIRECTION_OUTPUT: int
DIRECTION_PROOF: int
FLAGS: Any

class ImageCmsProfile:
    def __init__(self, profile) -> None: ...
    def tobytes(self): ...

class ImageCmsTransform(Image.ImagePointHandler):
    transform: Any
    input_mode: Any
    output_mode: Any
    output_profile: Any
    def __init__(
        self,
        input,
        output,
        input_mode,
        output_mode,
        intent=...,
        proof: Any | None = ...,
        proof_intent=...,
        flags: int = ...,
    ) -> None: ...
    def point(self, im): ...
    def apply(self, im, imOut: Any | None = ...): ...
    def apply_in_place(self, im): ...

def get_display_profile(handle: Any | None = ...): ...

class PyCMSError(Exception): ...

def profileToProfile(
    im,
    inputProfile,
    outputProfile,
    renderingIntent=...,
    outputMode: Any | None = ...,
    inPlace: bool = ...,
    flags: int = ...,
): ...
def getOpenProfile(profileFilename): ...
def buildTransform(
    inputProfile, outputProfile, inMode, outMode, renderingIntent=..., flags: int = ...
): ...
def buildProofTransform(
    inputProfile,
    outputProfile,
    proofProfile,
    inMode,
    outMode,
    renderingIntent=...,
    proofRenderingIntent=...,
    flags=...,
): ...

buildTransformFromOpenProfiles = buildTransform
buildProofTransformFromOpenProfiles = buildProofTransform

def applyTransform(im, transform, inPlace: bool = ...): ...
def createProfile(colorSpace, colorTemp: int = ...): ...
def getProfileName(profile): ...
def getProfileInfo(profile): ...
def getProfileCopyright(profile): ...
def getProfileManufacturer(profile): ...
def getProfileModel(profile): ...
def getProfileDescription(profile): ...
def getDefaultIntent(profile): ...
def isIntentSupported(profile, intent, direction): ...
def versions(): ...