"""Pydantic schemas for doctor data."""

from pydantic import BaseModel, ConfigDict


class DoctorBase(BaseModel):
    """Common information about a doctor."""

    name: str
    specialization: str


class DoctorCreate(DoctorBase):
    """Data required to create a doctor."""


class DoctorResponse(DoctorBase):
    """Data returned for a doctor."""

    id: int

    model_config = ConfigDict(from_attributes=True)
