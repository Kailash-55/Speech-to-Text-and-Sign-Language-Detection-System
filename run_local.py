"""
Local development runner for NeuroAid.
Uses SQLite so no PostgreSQL server is needed.
Run: python run_local.py
"""
import os

# Set env vars before importing app
os.environ.setdefault("SESSION_SECRET", "dev-secret-key-change-in-production")
os.environ.setdefault(
    "DATABASE_URL",
    "sqlite:///neuroaid_local.db"
)

from app import app, db          # noqa: E402
import routes                    # noqa: F401, E402

with app.app_context():
    db.create_all()
    print("Database tables created/verified.")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("  NeuroAid – running at http://127.0.0.1:5000")
    print("="*50 + "\n")
    app.run(host="0.0.0.0", port=5000, debug=True)
