"""Pydantic schemas for patient data."""

from pydantic import BaseModel, ConfigDict


class PatientBase(BaseModel):
    """Common information about a patient."""

    name: str
    phone: str
    email: str


class PatientCreate(PatientBase):
    """Data required to create a patient."""


class PatientResponse(PatientBase):
    """Data returned for a patient."""

    id: int

    model_config = ConfigDict(from_attributes=True)
