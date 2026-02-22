from backend.app.models import Prompt, Version, CreatePrompt
from datetime import datetime

def test_prompt_model():
    p = Prompt(id="1", title="T", content="C", owner="owner", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    assert p.title == "T" and p.owner == "owner"

def test_version_model():
    v = Version(version_id="v1", timestamp=datetime.utcnow(), author="author", summary="init")
    assert v.author == "author" and v.summary == "init"

def test_create_prompt_model():
    cp = CreatePrompt(title="T", content="C", owner="owner", tags=[])
    assert cp.title == "T" and cp.owner == "owner"
