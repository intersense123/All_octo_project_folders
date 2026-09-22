from models import AngleCalculationSettings, SessionLocal

session = SessionLocal()
for row in session.query(AngleCalculationSettings).all():
    print(row.Key, row.Value)