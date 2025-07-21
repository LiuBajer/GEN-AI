from pydantic import BaseModel
from typing import Dict, Any, Optional

class ApmokymoDuomenys(BaseModel):
    data: str
    chunk_size: Optional[int] = 500
    overlap: Optional[int] = 50
    metadata: Optional[Dict[str, Any]]