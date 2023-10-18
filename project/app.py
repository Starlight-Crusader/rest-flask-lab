from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint


from models.database import db
from models.escooter import EScooter


def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskacc:flaskpass@localhost/prlab'
    db.init_app(app)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app-name': 'Electro Scooter API'
        }
    )

    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)
    
    return app


if __name__ == '__main__':
    app = create_app()
    import routes
    app.run()