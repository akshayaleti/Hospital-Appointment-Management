from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate


def create_appointment(db: Session, appointment: AppointmentCreate):
    overlapping_appointment = (
        db.query(Appointment)
        .filter(
            Appointment.appointment_start < appointment.appointment_end,
            Appointment.appointment_end > appointment.appointment_start,
            or_(
                Appointment.doctor_id == appointment.doctor_id,
                Appointment.patient_id == appointment.patient_id,
            ),
        )
        .first()
    )
    if overlapping_appointment:
        raise ValueError("Appointment overlapping")
    db_appointment = Appointment(
        patient_id=appointment.patient_id,
        doctor_id=appointment.doctor_id,
        appointment_start=appointment.appointment_start,
        appointment_end=appointment.appointment_end,
    )

    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def get_appointments(db: Session):
    return db.query(Appointment).all()


def get_appointment_by_id(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()
