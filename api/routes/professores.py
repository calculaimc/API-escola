from flask import Blueprint, jsonify, request
from api.controllers.professores import ProfessoresController
from api.models.professores import ProfessorPayload

professores_blueprint = Blueprint('professor', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores_db = ProfessoresController().get_professores()

    if not professores_db:
        return jsonify(msg='nenhum professor encontrado')
    
    return jsonify(professores_db)

@professores_blueprint.route('/professores/<int:id>', methods=['GET'])
def get_professor_by_id(id):
    professor_db = ProfessoresController().get_professor_by_id(id)

    if not professor_db:
        return jsonify(error='professor não encontrado')
    
    return jsonify(professor_db)

@professores_blueprint.route('/professor', methods=['POST'])
def create_professor():
    novo_professor = request.get_json()

    ProfessorPayload(**novo_professor)

    if not ProfessoresController().create_professor(novo_professor):
        return jsonify(error='professor deve ter no mínimo 20 anos')
    
    return jsonify(msg='professor cadastrado com sucesso')

@professores_blueprint.route('/professor/<int:id>', methods=['DELETE'])
def delete_professor(id):

    if not ProfessoresController().delete_professor_by_id(id):
        return jsonify(error='professor não encontrado para deletar')
    
    return jsonify(msg='professor deletado com sucesso')

@professores_blueprint.route('/professor/<int:id>', methods=['PUT'])
def update_professor(id):
    professor_atualizado = request.get_json()
    ProfessorPayload(**professor_atualizado)

    query = ProfessoresController().update_professor_by_id(id, professor_atualizado)
    if query['resultado'] != 'sucesso':
        return jsonify(error=query['motivo']), query['status_code']
    
    return jsonify(msg='professor atualizado com sucesso'), 200