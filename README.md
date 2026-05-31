# 🌿 Zity Dashboard — Intelligent Sales Analytics & Prediction

> **Visualize. Analyze. Predict.**

A smart web application for e-commerce sales analysis and prediction, built during an internship at **VALA Creative Internet Solutions**.

---

## 📋 Overview

**Zity Dashboard** is an intelligent web platform designed to centralize, analyze, and visualize sales data from the Zity e-commerce site. It replaces manual CSV-based data management with an automated, interactive, and AI-powered solution.

The system allows administrators and analysts to:
- Import and process sales data via CSV files
- Monitor key performance indicators (KPIs) in real time
- Visualize trends through interactive charts
- Predict future sales using Machine Learning models
- Generate structured PDF reports with recommendations

---

## ✨ Features

### 🔐 Authentication & Security
- Email / password login with JWT tokens
- **Biometric login** via hand recognition (MediaPipe)
- Password reset via email verification code (Gmail SMTP)
- Role-based access control (RBAC): **Admin** and **Analyst**

### 📊 Analytics Dashboard
- KPI cards: total orders, revenue, quantities sold, distinct products
- Monthly and daily revenue evolution charts
- Product distribution donut chart
- Top products ranking with visual bars
- Date range filtering

### 📂 CSV Import
- Drag & drop file upload
- Automatic column validation and data cleaning
- Import history with archive tracking
- Duplicate detection

### 🤖 Machine Learning Predictions
- Three models compared automatically:
  - Linear Regression
  - **Regression + Seasonality** *(best performer — R² 76.8%)*
  - Moving Average
- Train/Test split validation (80/20)
- Next month revenue and quantity prediction
- Per-product prediction with stock recommendations
- Real vs. predicted revenue comparison chart

### 📄 PDF Reports
- Auto-generated reports including KPIs, top products, ML predictions
- Analyst recommendations sent to admin
- Downloadable by both roles

### 👥 User Management *(Admin only)*
- Invite users via email token
- CRUD operations on users and products
- Role assignment (Admin / Analyst)
- Profile photo, password change

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Backend** | Python, FastAPI, Jinja2 |
| **Database** | PostgreSQL, SQLAlchemy |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5 |
| **Charts** | Chart.js |
| **ML** | Scikit-learn, NumPy, Pandas |
| **Auth** | JWT (python-jose), Passlib |
| **PDF** | ReportLab |
| **Email** | Gmail SMTP |
| **Biometrics** | MediaPipe Hands |
| **Modeling** | AstahUML, PlantUML, draw.io |

---

## 📁 Project Structure

```
zity-dashboard/
├── app/
│   ├── main.py                  # FastAPI entry point
│   ├── database.py              # DB connection
│   ├── models/
│   │   ├── user.py
│   │   ├── sales.py
│   │   ├── prediction.py
│   │   ├── product.py
│   │   └── csv_archive.py
│   ├── routers/
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   ├── upload_csv.py
│   │   ├── predictions.py
│   │   ├── reports.py
│   │   ├── products.py
│   │   ├── users.py
│   │   └── profile.py
│   ├── services/
│   │   ├── analytics.py         # KPIs, charts data
│   │   └── prediction.py        # ML models & training
│   └── utils/
│       └── security.py          # JWT, hashing
├── templates/                   # Jinja2 HTML templates
├── static/
│   └── photos/                  # Profile photos, logos
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- PostgreSQL
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/zity-dashboard.git
cd zity-dashboard

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your settings
```

### `.env` configuration

```env
DATABASE_URL=postgresql://user:password@localhost:5432/zity_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_FROM=your_email@gmail.com
```

### Run the application

```bash
uvicorn app.main:app --reload
```

Open your browser at: **http://localhost:8000**

---

## 📊 CSV File Format

To import sales data, your CSV must follow this structure:

| Column | Type | Example | Required |
|--------|------|---------|----------|
| `sales_date` | date (YYYY-MM-DD) | 2025-01-15 | ✅ |
| `product_name` | text | Huile d'argan | ✅ |
| `quantity` | integer | 3 | ✅ |
| `unit_price` | decimal | 120.00 | ✅ |
| `total_price` | decimal | 360.00 | ⬜ Optional |
| `revenue` | decimal | 360.00 | ⬜ Optional |

---

## 🧠 ML Model Performance

Tested on 5 months of sales data (80/20 train/test split):

| Model | R² Score | Selected |
|-------|----------|----------|
| Linear Regression | 66.8% | ❌ |
| **Regression + Seasonality** | **76.8%** | ✅ |
| Moving Average | 0.0% | ❌ |

---

## 👤 Default Roles

| Role | Permissions |
|------|-------------|
| **Admin** | Full access: import CSV, manage users & products, view predictions, download reports, accept/reject recommendations |
| **Analyst** | Read access: view dashboard, analyze predictions, generate and send PDF reports with recommendations |

---

## 📸 Screenshots

| Dashboard | Predictions | Import CSV |
|-----------|-------------|------------|
| KPIs + Charts | ML Models Comparison | Drag & Drop Upload |

---

## 🎓 Academic Context

This project was developed as a **final-year internship** for the:

> **Bachelor's Degree in Artificial Intelligence and Data Science Engineering**
> Université Cadi Ayyad — Marrakech



---

## 📄 License

This project is developed for academic purposes.
© 2026 Samia Ait Rami — All rights reserved.

---

## 🙏 Acknowledgements

Special thanks to the team at **VALA Creative Internet Solutions** for their warm welcome, guidance, and support throughout this internship.
