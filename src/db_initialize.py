import os
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base

# Use PostgreSQL via SQLAlchemy
# Prefer environment variable, fallback to a sensible local default
# Use PostgreSQL via SQLAlchemy (hard-coded for now)
DATABASE_URL ='postgresql://neondb_owner:npg_bTWgHe6rEha3@ep-lucky-field-a8ri14ns-pooler.eastus2.azure.neon.tech/predictive_maintenance?sslmode=require&channel_binding=require'


Base = declarative_base()


class EquipmentEvent(Base):
    __tablename__ = "equipment_events"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    temperature = Column(Float, nullable=False)
    vibration = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    run_hours = Column(Float, nullable=False)

    failure_risk = Column(Float, nullable=False)
    maintenance_required = Column(Boolean, nullable=False)


def get_engine():
    """Return a SQLAlchemy engine for the app."""
    return create_engine(DATABASE_URL, echo=False, future=True)


def init_db():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created (or already exist) in PostgreSQL:", DATABASE_URL)


if __name__ == "__main__":
    init_db()
