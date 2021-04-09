from datetime import datetime
from enum import Enum
from typing import Any, Deque, Dict, List, Optional, TypedDict, Union

from pydantic import BaseModel

StdTypes = Union[bool, int, float, str, dict]
DictAny = Dict[str, Any]


class CRUD(str, Enum):
    POST = "POST"
    DELETE = "DELETE"
    GET = "GET"
    UPDATE = "PUT"
