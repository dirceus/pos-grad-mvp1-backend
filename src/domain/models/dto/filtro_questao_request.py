from typing import Optional

from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum


class FiltroQuestaoRequest:

    def __init__(self,
                 tipo: Optional[TipoQuestaoEnum],
                 instituicao: Optional[str],
                 ano: Optional[int],
                 evento: Optional[str],
                 disciplina: Optional[DisciplinaEnum],
                 ):

        self.tipo = tipo
        self.instituicao = instituicao
        self.ano = ano
        self.evento = evento
        self.disciplina = disciplina
