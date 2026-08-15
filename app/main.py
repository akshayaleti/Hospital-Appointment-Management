"""Main entry point for the Hospital Management API."""

from fastapi import FastAPI

from app.routers import appointment, doctor, patient

app = FastAPI(title="Hospital Management")
app.include_router(patient.router)
app.include_router(doctor.router)
app.include_router(appointment.router)
