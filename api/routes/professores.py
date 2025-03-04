from flask import Blueprint, jsonify, request
from api.controllers.professores import ProfessoresController
from api.models.professores import ProfessorPayload
from flasgger import swag_from
from api.spec.professores import (
    get_professores_doc,
    get_professor_by_id_doc,
    create_professor_doc,
    delete_professor_by_id_doc,
    update_professor_doc
)

professores_blueprint = Blueprint('professor', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
@swag_from(get_professores_doc)
def get_professores():
    professores_db = ProfessoresController().get_professores()

    if not professores_db:
        return jsonify(msg='nenhum professor encontrado'), 204
    
    return jsonify(professores_db), 200

@professores_blueprint.route('/professores/<int:id>', methods=['GET'])
@swag_from(get_professor_by_id_doc)
def get_professor_by_id(id):
    professor_db = ProfessoresController().get_professor_by_id(id)

    if not professor_db:
        return jsonify(error='professor não encontrado'), 404
    
    return jsonify(professor_db), 200

@professores_blueprint.route('/professor', methods=['POST'])
@swag_from(create_professor_doc)
def create_professor():
    novo_professor = request.get_json()

    ProfessorPayload(**novo_professor)

    if not ProfessoresController().create_professor(novo_professor):
        return jsonify(error='professor deve ter no mínimo 20 anos'), 422
    
    return jsonify(msg='professor cadastrado com sucesso'), 201

@professores_blueprint.route('/professor/<int:id>', methods=['DELETE'])
@swag_from(delete_professor_by_id_doc)
def delete_professor(id):

    if not ProfessoresController().delete_professor_by_id(id):
        return jsonify(error='professor não encontrado para deletar')
    
    return jsonify(msg='professor deletado com sucesso')

@professores_blueprint.route('/professor/<int:id>', methods=['PUT'])
@swag_from(update_professor_doc)
def update_professor(id):
    professor_atualizado = request.get_json()
    ProfessorPayload(**professor_atualizado)

    query = ProfessoresController().update_professor_by_id(id, professor_atualizado)
    if query['resultado'] != 'sucesso':
        return jsonify(error=query['motivo']), query['status_code']
    
    return jsonify(msg='professor atualizado com sucesso'), 200