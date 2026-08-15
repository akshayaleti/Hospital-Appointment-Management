from app.schemas.doctor import DoctorCreate
from app.services.doctor import create_doctor, get_doctor_by_id, get_doctors


def test_create_doctor(db):
    doctor_data = DoctorCreate(
        name="Dr. Smith",
        specialization="Cardiology",
    )
    doctor = create_doctor(db, doctor_data)

    assert doctor.id is not None
    assert doctor.name == "Dr. Smith"
    assert doctor.specialization == "Cardiology"


def test_get_doctors(db):
    doctor_data = DoctorCreate(
        name="Dr. Johnson",
        specialization="Neurology",
    )
    create_doctor(db, doctor_data)
    doctors = get_doctors(db)

    assert len(doctors) == 1
    assert doctors[0].name == "Dr. Johnson"


def test_get_doctor_by_id(db):
    doctor_data = DoctorCreate(
        name="Dr. Williams",
        specialization="Pediatrics",
    )
    doctor = create_doctor(db, doctor_data)
    result = get_doctor_by_id(db, doctor.id)

    assert result is not None
    assert result.id == doctor.id
    assert result.name == "Dr. Williams"


def test_get_doctor_by_id_not_found(db):
    result = get_doctor_by_id(db, 999)
    assert result is None
