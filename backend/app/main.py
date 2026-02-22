from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4
from datetime import datetime

# In-memory stores (V1 MVP)
prompts_db = {}
versions_db = {}
audits_db = []

app = FastAPI(title="Prompts System API")

class Version(BaseModel):
    version_id: str
    timestamp: datetime
    author: str
    summary: Optional[str] = ""

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
    tags: List[str] = Field(default_factory=list)
    owner: str
    created_at: datetime
    updated_at: datetime
    status: str = "draft"

class CreatePrompt(BaseModel):
    title: str
    content: str
    owner: str
    tags: List[str] = Field(default_factory=list)

@app.post("/prompts", response_model=Prompt)
def create_prompt(payload: CreatePrompt):
    pid = str(uuid4())
    now = datetime.utcnow()
    p = Prompt(id=pid, title=payload.title, content=payload.content, owner=payload.owner,
               tags=payload.tags, created_at=now, updated_at=now)
    prompts_db[pid] = p
    versions_db[pid] = []
    # initial version
    v = Version(version_id=str(uuid4()), timestamp=now, author=payload.owner, summary="Initial version")
    versions_db[pid].append(v)
    return p

@app.get("/prompts", response_model=List[Prompt])
def list_prompts():
    return list(prompts_db.values())

class VersionPayload(BaseModel):
    author: str
    summary: Optional[str] = ""

@app.post("/prompts/{prompt_id}/versions", response_model=Version)
def add_version(prompt_id: str, payload: VersionPayload):
    if prompt_id not in prompts_db:
        raise HTTPException(status_code=404, detail="Prompt not found")
    now = datetime.utcnow()
    v = Version(version_id=str(uuid4()), timestamp=now, author=payload.author, summary=payload.summary)
    versions_db[prompt_id].append(v)
    prompts_db[prompt_id].updated_at = now
    return v

@app.get("/prompts/{prompt_id}/versions", response_model=List[Version])
def get_versions(prompt_id: str):
    if prompt_id not in prompts_db:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return versions_db.get(prompt_id, [])

@app.post("/audits", response_model=AuditEvent)
def log_audit(event: AuditEvent):
    audits_db.append(event)
    return event
