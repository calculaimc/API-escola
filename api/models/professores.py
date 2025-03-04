from pydantic import BaseModel, Field
from typing import Optional

class ProfessorPayload(BaseModel):
    nome: str = Field(..., max_length=100)
    idade: int
    materia: str = Field(..., min_length=4)
    observacoes: str = Field(..., max_length=150)