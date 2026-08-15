from app.schemas.patient import PatientCreate
from app.services.patient import create_patient, get_patient_by_id, get_patients


def test_create_patient(db):
    patient_data = PatientCreate(
        name="John Doe", email="john@example.com", phone="1234567890"
    )

    patient = create_patient(db, patient_data)

    assert patient.name == "John Doe"
    assert patient.email == "john@example.com"
    assert patient.phone == "1234567890"
    assert patient.id is not None


def test_get_patients(db):
    patient_data = PatientCreate(
        name="Jane Doe", email="jane@example.com", phone="0987654321"
    )
    create_patient(db, patient_data)
    patients = get_patients(db)
    assert len(patients) == 1
    assert patients[0].name == "Jane Doe"


def test_get_patient_by_id(db):
    patient_data = PatientCreate(
        name="Alice Smith", email="alice@example.com", phone="5551234567"
    )
    patient = create_patient(db, patient_data)
    result = get_patient_by_id(db, patient.id)
    assert result is not None
    assert result.id == patient.id
    assert result.name == "Alice Smith"


def test_get_patient_by_id_not_found(db):
    result = get_patient_by_id(db, 999)
    assert result is None
