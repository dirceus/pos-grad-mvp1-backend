from typing import List, Optional

from pydantic import BaseModel, Field

from src.domain.models.alternativa import Alternativa
from src.domain.models.assunto import Assunto
from src.domain.models.dto.alternativa_request import AlternativaRequest
from src.domain.models.dto.cadastro_questao_request import CadastroQuestaoRequest
from src.domain.models.dto.filtro_questao_request import FiltroQuestaoRequest
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum
from src.domain.models.questao import Questao


class AlternativaSchema(BaseModel):
    descricao: str
    is_correta: bool


class CadastrarQuestaoSchema(BaseModel):
    tipo: TipoQuestaoEnum
    disciplina: DisciplinaEnum
    ano: int
    instituicao: str
    evento: Optional[str]
    assuntos: List[int]
    enunciado: str
    alternativas: List[AlternativaSchema] = Field(..., min_items=3, max_items=5)

    def to_dto(self) -> CadastroQuestaoRequest:
        return CadastroQuestaoRequest(self.tipo,
                                      self.enunciado,
                                      list(map(lambda a: AlternativaRequest(a.descricao, a.is_correta),
                                               self.alternativas)),
                                      self.instituicao,
                                      self.ano,
                                      self.evento,
                                      self.disciplina,
                                      self.assuntos)


class QuestaoSchema(BaseModel):
    codigo: int
    tipo: TipoQuestaoEnum
    disciplina: DisciplinaEnum
    ano: int
    instituicao: str
    evento: str
    enunciado: str
    assuntos: Optional[List[int]]
    alternativas: List[AlternativaSchema]
    cadastrador: str


class QuestaoSimplesSchema(BaseModel):
    codigo: int
    tipo: TipoQuestaoEnum
    disciplina: DisciplinaEnum
    ano: int
    instituicao: str
    evento: str
    enunciado: str
    cadastrador: str


class QuestaoPath(BaseModel):
    codigo: int


class FiltroQuestaoSchema(BaseModel):
    tipo: Optional[TipoQuestaoEnum]
    disciplina: Optional[DisciplinaEnum]
    ano: Optional[int]
    instituicao: Optional[str]
    evento: Optional[str]

    def to_dto(self) -> FiltroQuestaoRequest:
        return FiltroQuestaoRequest(
            self.tipo,
            self.instituicao,
            self.ano,
            self.evento,
            self.disciplina,
        )
