from typing import List

from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.dto.alternativa_response import AlternativaResponse
from src.domain.models.questao import Questao
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum


class CadastroQuestaoRequest:

    def __init__(self,
                 tipo: TipoQuestaoEnum,
                 enunciado: str,
                 alternativas: List[AlternativaResponse],
                 instituicao: str,
                 ano: int,
                 evento: str,
                 disciplina: DisciplinaEnum,
                 assuntos: List[Assunto]):
        self.tipo = tipo
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.instituicao = instituicao
        self.ano = ano
        self.evento = evento
        self.disciplina = disciplina
        self.assuntos = assuntos

    def to_model(self) -> Questao:
        return Questao(None,
                       self.tipo,
                       self.enunciado,
                       list(map(lambda it: it.to_model(), self.alternativas)),
                       self.instituicao,
                       self.ano,
                       self.evento,
                       self.disciplina,
                       self.assuntos,
                       None
                       )
