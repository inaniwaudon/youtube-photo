from .compat import compat_realpath as compat_realpath
from .utils import encode_compat_str as encode_compat_str

def rsa_verify(message, signature, key): ...
def update_self(to_screen, verbose, opener): ...
def get_notes(versions, fromVersion): ...
def print_notes(to_screen, versions, fromVersion=...) -> None: ...