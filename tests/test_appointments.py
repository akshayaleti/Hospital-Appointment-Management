from datetime import UTC, datetime

import pytest

from app.models.doctor import Doctor
from app.models.patient import Patient
from app.schemas.appointment import AppointmentCreate
from app.services.appointment import (
    create_appointment,
    get_appointment_by_id,
    get_appointments,
)


def create_test_patient(db):
    patient = Patient(
        name="John Doe",
        email="john.doe@example.com",
        phone="1234567890",
    )

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient


def create_test_doctor(db):
    doctor = Doctor(
        name="Dr. Smith",
        specialization="Cardiology",
    )

    db.add(doctor)
    db.commit()
    db.refresh(doctor)

    return doctor


def test_create_appointment(db):
    patient = create_test_patient(db)
    doctor = create_test_doctor(db)

    appointment_data = AppointmentCreate(
        patient_id=patient.id,
        doctor_id=doctor.id,
        appointment_start=datetime(2026, 8, 20, 10, 0, tzinfo=UTC),
        appointment_end=datetime(2026, 8, 20, 11, 0, tzinfo=UTC),
    )

    appointment = create_appointment(db, appointment_data)

    assert appointment.id is not None
    assert appointment.patient_id == patient.id
    assert appointment.doctor_id == doctor.id


def test_get_appointments(db):
    patient = create_test_patient(db)
    doctor = create_test_doctor(db)

    appointment_data = AppointmentCreate(
        patient_id=patient.id,
        doctor_id=doctor.id,
        appointment_start=datetime(2026, 8, 20, 10, 0, tzinfo=UTC),
        appointment_end=datetime(2026, 8, 20, 11, 0, tzinfo=UTC),
    )

    create_appointment(db, appointment_data)

    appointments = get_appointments(db)

    assert len(appointments) == 1


def test_get_appointment_by_id(db):
    patient = create_test_patient(db)
    doctor = create_test_doctor(db)

    appointment_data = AppointmentCreate(
        patient_id=patient.id,
        doctor_id=doctor.id,
        appointment_start=datetime(2026, 8, 20, 10, 0, tzinfo=UTC),
        appointment_end=datetime(2026, 8, 20, 11, 0, tzinfo=UTC),
    )

    appointment = create_appointment(db, appointment_data)

    result = get_appointment_by_id(db, appointment.id)

    assert result is not None
    assert result.id == appointment.id


def test_get_appointment_by_id_not_found(db):
    result = get_appointment_by_id(db, 99999)

    assert result is None


def test_overlapping_appointment(db):
    patient = create_test_patient(db)
    doctor = create_test_doctor(db)

    # First appointment: 10:00 - 11:00
    first_appointment = AppointmentCreate(
        patient_id=patient.id,
        doctor_id=doctor.id,
        appointment_start=datetime(2026, 8, 20, 10, 0, tzinfo=UTC),
        appointment_end=datetime(2026, 8, 20, 11, 0, tzinfo=UTC),
    )

    create_appointment(db, first_appointment)

    # Second appointment: 10:30 - 11:30
    # This overlaps with the first appointment.
    second_appointment = AppointmentCreate(
        patient_id=patient.id,
        doctor_id=doctor.id,
        appointment_start=datetime(2026, 8, 20, 10, 30, tzinfo=UTC),
        appointment_end=datetime(2026, 8, 20, 11, 30, tzinfo=UTC),
    )

    with pytest.raises(ValueError, match="Appointment overlapping"):
        create_appointment(db, second_appointment)
