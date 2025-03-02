CREATE TABLE professores(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	idade INTEGER  NOT NULL,
	materia VARCHAR(100)  NOT NULL,
	observacoes TEXT
);
SELECT * FROM professores;

CREATE TABLE turmas (
	id SERIAL PRIMARY KEY,
	descricao VARCHAR(100) NOT NULL,
	professor_id INTEGER,
	ativo BOOLEAN NOT NULL, 
	FOREIGN KEY (professor_id) REFERENCES professores(id)
);
SELECT * FROM turmas;

CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,                    
    nome VARCHAR(100) NOT NULL,               
    idade INT NOT NULL,                                
    turma_id INT,                            
    data_nascimento DATE NOT NULL,                    
    nota_primeiro_semestre FLOAT,          
    nota_segundo_semestre FLOAT,              
    media_final FLOAT,                       

    FOREIGN KEY (turma_id) REFERENCES turmas(id) ON DELETE SET NULL
);
SELECT * FROM alunos;