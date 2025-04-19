from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    location = Column(String)

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    hire_date = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department")

class Performance(Base):
    __tablename__ = "performance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    rating = Column(Float)
    review_date = Column(Date)
    comments = Column(String)

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    date = Column(Date)
    status = Column(String)
    working_hours = Column(Float)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    deadline = Column(Date)
    employee_id = Column(Integer, ForeignKey("employees.id"))
