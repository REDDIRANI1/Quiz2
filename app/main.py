from fastapi import FastAPI
from .routes import employees, summary
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Data API",
    description="API for employee data management and visualization",
    version="1.0.0"
)

app.include_router(employees.router, prefix="/employees", tags=["Employees"])
app.include_router(summary.router, prefix="/summary", tags=["Summary"])

@app.get("/health/")
def health_check():
    return {"status": "ok"}
