"""Pydantic schemas for appointment data."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AppointmentBase(BaseModel):
    """Common appointment information."""

    patient_id: int
    doctor_id: int
    appointment_start: datetime
    appointment_end: datetime


class AppointmentCreate(AppointmentBase):
    """Data required to create an appointment."""

    model_config = ConfigDict(from_attributes=True)


class AppointmentResponse(AppointmentBase):
    """Data returned for an appointment."""

    id: int

    model_config = ConfigDict(from_attributes=True)
