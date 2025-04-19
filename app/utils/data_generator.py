from faker import Faker
from datetime import datetime
fake = Faker()

def generate_employee():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "hire_date": fake.date_this_decade(),
        "department": fake.job()
    }
