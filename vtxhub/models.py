from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Input:
    method: str  # Required
    originalUrl: str   # Required
    protocol: str  # Required
    url: str  # Required
    body: dict = field(default_factory=dict)
    cookies: Optional[dict] = None
    fresh: bool = False
    headers: dict = field(default_factory=dict)
    ip: str = ''
    ips: list = field(default_factory=list)
    query: dict = field(default_factory=dict)
    secure: None = None  # ?
    signedCookies: Optional[dict] = None
    stale: bool = True  # ?
    subdomains: list = field(default_factory=list)
    xhr: Optional[dict] = None  # ?


@dataclass
class Output:
    status: int  # Required
    headers: dict = field(default_factory=dict)
    host: str = ''
    port: int = 0
    provider: str = '???'  # 'http' or 'https'
    factory: str = ''
    msg: str = ''  # Error message for network failures?
    code: int = -1  # Error code for network failures?
    size: int = 0
    preview: str = ''  # ~40 chars of readable output from the body


@dataclass
class Interception:
    _id: str  # Required
    input: Input  # Required
    output: Output  # Required
    breakpoint: str = ''
    status: str = 'new'
    result: str = 'running'
    server: str = ''
    interception: str = ''
    created_at: str = ''
    input_at: str = ''
    handle: str = ''
    user: dict = field(default_factory=dict)
    inputSize: int = 0
    outputSize: int = 0
    totalSize: int = 0
