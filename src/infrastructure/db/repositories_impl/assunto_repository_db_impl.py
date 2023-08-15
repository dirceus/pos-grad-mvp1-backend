from sqlalchemy.orm import Session

from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.repositories.assunto_repository import AssuntoRepository
from src.infrastructure.db.entities.assunto_entity import AssuntoEntity


class AssuntoRepositoryDbImpl(AssuntoRepository):

    def buscar_por_disciplina(self, disciplina: DisciplinaEnum):
        session = Session()
        questoes = session.query(AssuntoEntity).filter(AssuntoEntity.disciplina == disciplina.name)
        return list(map(lambda q: q.to_model(), questoes))

    def obter_por_codigo(self, codigo: int):
        session = Session()
        return session.query(AssuntoEntity).filter(AssuntoEntity.id == codigo).first()
