from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum


class AssuntoResponse:

    def __init__(self, assunto: Assunto):
        self.codigo = assunto.codigo
        self.disciplina = assunto.disciplina
        self.descricao = assunto.descricao
