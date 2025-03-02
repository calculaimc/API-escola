from flask import Blueprint, jsonify, request
from api.controllers.alunos import AlunosController
from api.models.alunos import CreateAlunoPayload
from flasgger import swag_from
from api.spec.alunos import (
    create_aluno_doc,
    get_aluno_by_id_doc,
    get_alunos_doc,
    delete_aluno_by_id_doc,
    update_aluno_by_id
)

alunos_blueprint = Blueprint('aluno', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
@swag_from(get_alunos_doc)
def get_alunos():
    alunos_db = AlunosController().get_alunos()
    
    if not alunos_db:
        return jsonify(msg='nenhum aluno cadastrado'), 200
    
    return jsonify(alunos_db)

@alunos_blueprint.route('/alunos/<int:id>', methods=['GET'])
@swag_from(get_aluno_by_id_doc)
def get_aluno(id):
    aluno_db = AlunosController().get_aluno_by_id(id)

    if not aluno_db:
        return jsonify(error='aluno não encontrado'), 404
    
    return aluno_db

@alunos_blueprint.route('/aluno', methods=['POST'])
@swag_from(create_aluno_doc)
def create_aluno():
    novo_aluno = request.get_json()

    CreateAlunoPayload(**novo_aluno)

    if not AlunosController().create_aluno(novo_aluno):
        return jsonify(error='id da turma não existe'), 404
    
    return jsonify(msg='aluno cadastrado com sucesso'), 200

@alunos_blueprint.route('/aluno/<int:id>', methods=['DELETE'])
@swag_from(delete_aluno_by_id_doc)
def delete_aluno(id):

    if not AlunosController().delete_aluno(id):
        return jsonify(error='aluno não encontrado para deletar'), 404
    
    return jsonify(msg='aluno deletado com sucesso'), 200

@alunos_blueprint.route('/aluno/<int:id>', methods=['PUT'])
@swag_from(update_aluno_by_id)
def update_aluno(id):
    aluno_atualizado = request.get_json()

    CreateAlunoPayload(**aluno_atualizado)
    
    if not AlunosController().update_aluno(aluno_atualizado, id):
        return jsonify(error='aluno não encontrado para atualizar'), 404
    
    return jsonify(msg='aluno deletado com sucesso!')