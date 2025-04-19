# 🚀 Employee Data API

A FastAPI-based project for managing and visualizing employee data, including departments, performance, attendance, and project assignments.
## ⚙️ Setup Instructions

1. **Clone the repo**
git clone <your-repo-url> cd fastapi_employee_project

2. **Create a virtual environment**
python -m venv venv source venv/bin/activate # Windows: venv\Scripts\activate


3. **Install dependencies**
pip install -r requirements.txt

4. **Create `.env` file**
DATABASE_URL=postgresql://<user>:<password>@localhost/<database>

5. **Run migrations**
alembic upgrade head

6. **Run the API**
uvicorn app.main:app --reload
