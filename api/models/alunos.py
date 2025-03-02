from pydantic import BaseModel, Field
from typing import Optional

class CreateAlunoPayload(BaseModel):
    nome: str = Field(..., max_length=100)
    idade: int
    turma_id: int
    data_nascimento: str
    nota_primeiro_semestre: Optional[float] = None
    nota_segundo_semestre: Optional[float] = None
    media_final: Optional[float] = None 
