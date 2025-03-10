from flask import ( Flask, redirect )
from flask_migrate import Migrate

def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sodapop9@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    from . import models
    models.db.init_app(app)            
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello(): 
        return redirect('/pets')

#register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

#return the app
    return app