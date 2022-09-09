from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from xmlrpc.client import boolean


@dataclass
class VideoGamePlatform(Enum):
    ONE = "One"
    PS4 = "PS4"
    PS5 = "PS5"
    SWITCH = "Switch"
    PC = "PC"


@dataclass
class VideoGame:
    name: str
    release_date: str
    studio: str
    ratings: str
    platforms: List[VideoGamePlatform]


@dataclass
class GetGamesFilters:
    name: Optional[str] = None
    release_date: Optional[str] = None
    ascending: boolean = False
    studio: Optional[str] = None
    ratings: Optional[int] = None
    platform: Optional[VideoGamePlatform] = None
