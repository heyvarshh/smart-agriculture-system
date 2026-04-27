# Smart Kisan 🌾

A full-stack farm management dashboard I built to help track farmers, crops, sensors, and irrigation — all from one place.

The idea is simple: Indian farmers deal with a lot of moving parts (weather, water, soil health, crop cycles). This system puts everything on a single screen so you can actually make sense of it.

## What it does

- **Farmer management** — register farmers, track their land, contact info, active/inactive status
- **Crop tracking** — sow dates, expected harvest, growth stage (shown as a percentage), health status
- **Sensor & zone monitoring** — each field zone has water level readings and flow rate info
- **Irrigation control** — see which zones are ON/OFF, water levels at a glance
- **Activity logs** — who did what and when, with severity levels (OK / Warning / Critical)
- **Analytics** — basic overview endpoint (still building this out)

## Tech stack

**Backend:**
- Python + Flask
- MySQL (via PyMySQL + SQLAlchemy)
- Flask-CORS for frontend communication

**Frontend:**
- Single-page HTML/CSS/JS app (no framework, no build step)
- Chart.js for data visualization
- Google Fonts (Plus Jakarta Sans, Playfair Display, JetBrains Mono)
- All CSS and JS is inline — the whole frontend is one `index.html` file

## Project structure

```
├── backend/
│   ├── app.py              # Flask app factory, registers all blueprints
│   ├── config.py           # DB connection string, secret key
│   ├── models.py           # SQLAlchemy models (Farmer, Crop, Zone, Log)
│   ├── seed.py             # Populates the database with sample data
│   ├── requirements.txt
│   └── routes/
│       ├── farmers.py      # /api/farmers
│       ├── crops.py        # /api/crops
│       ├── sensors.py      # /api/sensors
│       ├── irrigation.py   # /api/irrigation
│       ├── analytics.py    # /api/analytics
│       └── logs.py         # /api/logs
│
└── frontend/
    └── index.html          # The entire frontend (HTML + CSS + JS)
```

## Getting started

### 1. Clone this repo

```bash
git clone https://github.com/heyvarshh/smart-agriculture-system.git
cd smart-agriculture-system
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure the database

Open `backend/config.py` and update the MySQL connection string with your own credentials:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:yourpassword@localhost/smart_agri'
```

Make sure you've created the `smart_agri` database in MySQL first:

```sql
CREATE DATABASE smart_agri;
```

### 4. Seed sample data

```bash
python seed.py
```

This drops existing tables (if any), recreates them, and fills in some test data — 5 farmers, 4 crops, 4 irrigation zones, and a few activity logs.

### 5. Run the backend

```bash
python app.py
```

API runs on `http://localhost:5002`

### 6. Open the frontend

Just open `frontend/index.html` in your browser. It talks to the backend at port 5002.

## API endpoints

| Method | Endpoint           | What it returns              |
|--------|--------------------|------------------------------|
| GET    | `/api/farmers`     | List of all registered farmers |
| GET    | `/api/crops`       | All crops with growth info   |
| GET    | `/api/sensors`     | Sensor/zone data             |
| GET    | `/api/irrigation`  | Irrigation zone status       |
| GET    | `/api/analytics`   | Analytics placeholder        |
| GET    | `/api/logs`        | Activity log entries         |

## Screenshots

The dashboard has a login screen with a split layout (info panel + form), then a sidebar-based dashboard with stat cards, tables, and charts. It uses an earthy green color palette — forest greens, mint, sage, with warm whites and gold accents.

## Things I'd like to add later

- POST/PUT/DELETE endpoints (right now it's read-only)
- JWT authentication instead of the mock login
- Weather API integration
- Mobile-responsive layout
- Deployment on Render or Railway

## License

Feel free to use this however you want. No license restrictions.
