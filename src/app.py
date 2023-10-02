from flask import Flask, jsonify
from config import config
from routes import Generate, Search
from utils.exeptions import ParameterException

app = Flask(__name__)

def page_not_found(error):
    return jsonify({'success': False, 'message': 'Not found page'}), 404

@app.errorhandler(ParameterException)
def handle_parameter_exceptions(ex):
    return jsonify({'success': False, 'message': f'Parametros invalidos: {ex}'}), 400

@app.errorhandler(Exception)
def handle_exceptions(ex):
    return jsonify({'success': False, 'message': f'Error interno: {ex}'}), 500

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Search.main, url_prefix='/api/search')
    app.register_blueprint(Generate.main, url_prefix='/api/generate')

    # Error Handlers
    app.register_error_handler(404, page_not_found)

    app.run(host=config['host'], port=config['port'])