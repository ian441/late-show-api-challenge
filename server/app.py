from flask import Flask
from server.config import Config
from extensions import db, migrate, jwt
from server.controllers.auth_controller import auth_bp
from server.controllers.appearance_controller import appearance_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.guest_controller import guest_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    print("DB URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(episode_bp) 
    app.register_blueprint(guest_bp)
    app.register_blueprint(appearance_bp)
    
    
    @app.route('/')
    def home():
        return {'message': 'Late show API is running!'}
    
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)