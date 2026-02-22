from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Version(BaseModel):
    version_id: str
    timestamp: datetime
    author: str
    summary: Optional[str] = None

class AuditEvent(BaseModel):
    event_id: str
    type: str
    timestamp: datetime
    target_prompt_id: str
    details: Optional[str] = None

class Prompt(BaseModel):
    id: str
    title: str
    content: str
    tags: List[str] = []
    owner: str
    created_at: datetime
    updated_at: datetime
    status: str = "draft"

class CreatePrompt(BaseModel):
    title: str
    content: str
    owner: str
    tags: List[str] = []
