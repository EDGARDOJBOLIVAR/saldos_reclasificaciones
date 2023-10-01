from flask import Blueprint, jsonify, request
from utils.exeptions import ParameterException
from utils.utils import paginate_list
import json

main = Blueprint('search_blueprint', __name__)

@main.route('/')
def get_home():
    return jsonify({'status': True})

@main.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    metodo = request.method
    cabeceras = dict(request.headers)
    datos_cuerpo = request.data
    argumentos_url = request.args.to_dict()
    datos_formulario = request.form.to_dict()


    try:
        json_request = request.json
    except:
        json_request = None

    detalles_request = {
        # 'metodo': metodo,
        'cabeceras': cabeceras,
        'datos_cuerpo': datos_cuerpo.decode("utf-8"),  # Convertir a cadena si es necesario
        # 'argumentos_url': argumentos_url,
        'json_request': json_request, 
        'datos_formulario': datos_formulario
    }

    return jsonify(detalles_request)