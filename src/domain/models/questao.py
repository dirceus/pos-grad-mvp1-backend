from typing import List

from src.domain.models.alternativa import Alternativa
from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum
from datetime import datetime


class Questao:

    def __init__(self, codigo: int,
                 tipo: TipoQuestaoEnum,
                 enunciado: str,
                 alternativas: List[Alternativa],
                 instituicao: str,
                 ano: int,
                 evento: str,
                 disciplina: DisciplinaEnum,
                 assuntos: List[Assunto],
                 cadastrador: str,
                 data_cadastro: datetime = None
                 ):
        self.codigo = codigo
        self.tipo = tipo
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.instituicao = instituicao
        self.ano = ano
        self.evento = evento
        self.disciplina = disciplina
        self.assuntos = assuntos
        self.cadastrador = cadastrador
        self.data_cadastro = data_cadastro
        self.ativo = True
