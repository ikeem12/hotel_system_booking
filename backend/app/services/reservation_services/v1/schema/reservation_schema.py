from pydantic import BaseModel, EmailStr
from typing import Optional,Dict, Literal

class ReservationSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    check_in: str
    check_out: str
    rooms: Dict[Literal['Individual','Doble','Familiar','Suite'], int]