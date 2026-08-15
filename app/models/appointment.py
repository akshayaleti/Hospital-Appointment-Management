"""this shows how appointment works"""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Appointment(Base):
    """
    Represents an appointment in the hospital.
    """

    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    appointment_start: Mapped[datetime] = mapped_column(DateTime)
    appointment_end: Mapped[datetime] = mapped_column(DateTime)
