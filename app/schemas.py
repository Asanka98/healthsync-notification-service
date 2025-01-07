from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
    Pending = "Pending"
    Sent = "Sent"

class NotificationBase(BaseModel):
    patient_name: str
    message: str
    notification_time: datetime
    status: StatusEnum | None = StatusEnum.Pending

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int

    class Config:
        orm_mode = True
