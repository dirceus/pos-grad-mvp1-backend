from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum


class AssuntoResponse:

    def __init__(self, assunto: Assunto):
        self.codigo = assunto.codigo
        self.disciplina = {assunto.disciplina.name: assunto.disciplina.value}
        self.descricao = assunto.descricao

    def to_model(self) -> Assunto:
        return Assunto(self.codigo, DisciplinaEnum[self.disciplina[0].key], self.descricao, )
