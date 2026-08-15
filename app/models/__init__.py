"""Database models for the hospital management application."""

from app.models.appointment import Appointment as Appointment
from app.models.doctor import Doctor as Doctor
from app.models.patient import Patient as Patient

__all__ = [
    "Appointment",
    "Doctor",
    "Patient",
]
