"""Patient API routes."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.patient import PatientCreate, PatientResponse
from app.services.patient import (
    create_patient as create_patient_service,
)
from app.services.patient import (
    get_patient_by_id,
)
from app.services.patient import (
    get_patients as get_patients_service,
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)


@router.post("/", response_model=PatientResponse)
def create_patient_endpoint(
    patient: PatientCreate,
    db: Session = Depends(get_db),
):
    """Create a new patient."""

    return create_patient_service(db, patient)


@router.get("/", response_model=list[PatientResponse])
def get_patients(
    db: Session = Depends(get_db),
):
    """Return all patients."""

    return get_patients_service(db)


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
):
    """Return a patient by ID."""

    patient = get_patient_by_id(db, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    return patient
