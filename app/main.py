from fastapi import FastAPI
from .routes import employees, summary
from .database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI application instance
app = FastAPI(
    title="Employee Data API",
    description="API for employee data management and visualization",
    version="1.0.0"
)

# Include routers
app.include_router(employees.router, prefix="/employees", tags=["Employees"])
app.include_router(summary.router, prefix="/summary", tags=["Summary"])

# Health check route
@app.get("/health/")
def health_check():
    return {"status": "ok"}

# Root route
@app.get("/")
def root():
    return {
        "message": "Welcome to the Employee Data API",
        "docs_url": "/docs",
        "health_check": "/health/"
    }
