from app import create_app, db
from app.models import User
from config import Config

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=Config.PORT,debug=True)
