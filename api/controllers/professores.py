from api.database.conector import DatabaseManager

class ProfessoresController():
    def __init__(self) -> None:
        ...

    def get_professores(self) -> list:
        return [ professor._asdict() for professor in DatabaseManager().select_all('SELECT * FROM professores')]
    
    def get_professor_by_id(self, id: int) -> dict:
        professor_db = DatabaseManager().select_one(f'SELECT * FROM professores WHERE id = {id}')
        professor_db = professor_db._asdict() if professor_db else {}
        return professor_db
    
    def create_professor(self, novo_professor: dict) -> bool:

        if novo_professor['idade'] < 20:
            return False

        DatabaseManager().execute_sql_str(f"INSERT INTO professores(nome, idade, materia, observacoes) VALUES('{novo_professor.get('nome')}', {novo_professor.get('idade')}, '{novo_professor.get('materia')}', '{novo_professor.get('observacoes')}')")
        return True
    
    def delete_professor_by_id(self, id: int) -> bool:
        if DatabaseManager().select_one(f'SELECT * FROM professores WHERE id = {id}') is None:
            return False
        DatabaseManager().execute_sql_str(f'DELETE FROM professores WHERE id = {id}')
        return True
    
    def update_professor_by_id(self, id: int, professor_atualizado: dict) -> dict:

        if DatabaseManager().select_one(f'SELECT * FROM professores WHERE id = {id}') is None:
            return {
                "resultado": 'error',
                "motivo": 'professor não encontrado para atualizar',
                "status_code": 404
            }

        if professor_atualizado['idade'] < 20:
            return {
                "resultado": 'error',
                "motivo": 'professor deve ter no mínimo 20 anos',
                "status_code": 422
            }
        
        DatabaseManager().execute_sql_str(f"""UPDATE professores
                                          SET nome = '{professor_atualizado['nome']}',
                                          idade = {professor_atualizado['idade']},
                                          materia = '{professor_atualizado['materia']}',
                                          observacoes = '{professor_atualizado['observacoes']}'
                                          WHERE id = {id}""")
        
        return {
                "resultado": 'sucesso',
            }