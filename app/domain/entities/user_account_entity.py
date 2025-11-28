from dataclasses import dataclass
from typing import Optional

@dataclass
class UserAccount:
    id: str
    user_id: str
    account: str
    agency: str
    balance: str
    