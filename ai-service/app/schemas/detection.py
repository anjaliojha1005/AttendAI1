from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List

class BoundingBox(BaseModel):
    x: int
    y: int
    width: int
    height: int
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)

class DetectionResponse(BaseModel):
    success: bool
    face_count: int
    faces: List[BoundingBox]
    processing_time_ms: float
    is_mock: bool
    mock_disclaimer: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    error: Optional[str] = None

class Base64ImageRequest(BaseModel):
    image_base64: str

class MatchFacesResponse(BaseModel):
    status: str
    message: str
    isMock: bool

class EngagementIngestRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    student_id: int = Field(ge=1)
    name: str = Field(min_length=1, max_length=120)
    timestamp: Optional[float] = Field(default=None, ge=0)
    presence_duration: float = Field(default=0.0, ge=0, le=86400)
    movement_score: float = Field(default=0.5, ge=0, le=1)
    speech_ratio: float = Field(default=0.0, ge=0, le=1)
    inactivity_duration: float = Field(default=0.0, ge=0, le=86400)
    attendance_status: str = Field(default="pending", pattern="^(pending|present|absent|late|excused)$")

class SimulateSessionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    duration_seconds: int = Field(default=15, ge=1, le=300)
    num_students: int = Field(default=5, ge=1, le=200)
