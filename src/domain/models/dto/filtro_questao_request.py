from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum


class FiltroQuestaoRequest:

    def __init__(self,
                 tipo: TipoQuestaoEnum,
                 instituicao: str,
                 ano: int,
                 evento: str,
                 disciplina: DisciplinaEnum,
                 assunto: Assunto,
                 cadastrador: str,
                 ativas: bool
                 ):

        self.tipo = tipo
        self.instituicao = instituicao
        self.ano = ano
        self.evento = evento
        self.disciplina = disciplina
        self.assunto = assunto
        self.cadastrador = cadastrador
        self.ativo = ativas