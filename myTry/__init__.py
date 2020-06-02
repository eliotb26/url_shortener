from flask import Flask


#this page automatically gets called by flask 

def create_app(test_config=None): 
    app = Flask(__name__)  
    app.secret_key = 'hashdfldjl'#securly send messages to user so others cannot snoop in and see this info
                            #make it long hard key that cannot be exposed. 

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app



