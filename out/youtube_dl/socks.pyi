import socket
from .compat import compat_ord as compat_ord, compat_struct_pack as compat_struct_pack, compat_struct_unpack as compat_struct_unpack
from typing import Any, NamedTuple

SOCKS4_VERSION: int
SOCKS4_REPLY_VERSION: int
SOCKS4_DEFAULT_DSTIP: Any
SOCKS5_VERSION: int
SOCKS5_USER_AUTH_VERSION: int
SOCKS5_USER_AUTH_SUCCESS: int

class Socks4Command:
    CMD_CONNECT: int
    CMD_BIND: int

class Socks5Command(Socks4Command):
    CMD_UDP_ASSOCIATE: int

class Socks5Auth:
    AUTH_NONE: int
    AUTH_GSSAPI: int
    AUTH_USER_PASS: int
    AUTH_NO_ACCEPTABLE: int

class Socks5AddressType:
    ATYP_IPV4: int
    ATYP_DOMAINNAME: int
    ATYP_IPV6: int

class ProxyError(socket.error):
    ERR_SUCCESS: int
    def __init__(self, code: Any | None = ..., msg: Any | None = ...) -> None: ...

class InvalidVersionError(ProxyError):
    def __init__(self, expected_version, got_version) -> None: ...

class Socks4Error(ProxyError):
    ERR_SUCCESS: int
    CODES: Any

class Socks5Error(ProxyError):
    ERR_GENERAL_FAILURE: int
    CODES: Any

class ProxyType:
    SOCKS4: int
    SOCKS4A: int
    SOCKS5: int

class Proxy(NamedTuple):
    type: Any
    host: Any
    port: Any
    username: Any
    password: Any
    remote_dns: Any

class sockssocket(socket.socket):
    def __init__(self, *args, **kwargs) -> None: ...
    def setproxy(self, proxytype, addr, port, rdns: bool = ..., username: Any | None = ..., password: Any | None = ...) -> None: ...
    def recvall(self, cnt): ...
    def connect(self, address) -> None: ...
    def connect_ex(self, address): ...
