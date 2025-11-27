from dataclasses import dataclass
from typing import Optional

@dataclass
class LoginDto:
    email: str
    password: str