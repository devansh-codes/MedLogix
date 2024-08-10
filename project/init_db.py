from main import app, db  # Ensure you import both app and db

def init_db():
    """Initialize the database."""
    with app.app_context():
        db.create_all()  # Create all tables

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")


