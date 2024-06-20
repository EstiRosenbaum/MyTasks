from pydantic import BaseModel
from typing import Optional

class CopyModel(BaseModel):
    from_container_name: str
    to_container_name: str
    from_blob_location: str
    to_folder: str
    as_subdir: Optional[bool] = False
