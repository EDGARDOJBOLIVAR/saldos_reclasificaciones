from flask import Blueprint, jsonify
from models.AuditTaskImplModel import AuditTaskImplModel
from models.CorteDatosModel import CorteDatosModel
from models.CorteDatos2Model import CorteDatos2Model
from models.CorteModel import CorteModel

main = Blueprint('generate_blueprint', __name__)

@main.route('/')
def get_home():
    return jsonify({'status': True})

@main.route('/instant/db', methods=['GET'])
def instant_db():
    success = True
    Data = AuditTaskImplModel.getAll()

    elements = []
    if Data is not None:
        inserted = CorteModel.insert()
        CorteDatosModel.inserts(inserted, Data)
        CorteDatos2Model.inserts(inserted, Data)
        elements.append({"inserted": inserted})
    else:
        success = False

    return jsonify({'success': success, 'size': len(elements), 'data': elements})