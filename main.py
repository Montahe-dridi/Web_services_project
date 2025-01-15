from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from app.Resources.Users import blp as UserBlueprint
from app.Resources.Rides import blp as RideBlueprint
from app.Models.db import db

def create_app():
    app = Flask(__name__)

    # App configuration
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Carpooling API"
    app.config["API_VERSION"] = "1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///carpooling.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "super-secret-key"

    db.init_app(app)
    api = Api(app)
    jwt = JWTManager(app)

    if __name__ == "__main__":
      app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
