from typing import Optional

from pydantic import BaseModel


class SponsorRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]

class DonateDetailRequest(BaseModel):
    id: Optional[int]
    sponsor_id: Optional[int]
    account_number: Optional[str]
    transaction_code: Optional[str]
    donations: Optional[int]
