from typing import List, Optional

from src.domain.models.dto.filtro_questao_request import FiltroQuestaoRequest
from src.domain.models.questao import Questao
from src.domain.models.repositories.questao_repository import QuestaoRepository
from src.infrastructure.db.connection import Session
from src.infrastructure.db.entities.questao_entity import QuestaoEntity


class QuestaoRepositoryDbImpl(QuestaoRepository):

    def pesquisar_por_disciplina(self, filtro: FiltroQuestaoRequest) -> List[Questao]:
        return self.obter_todos()

    def obter_por_codigo(self, codigo: int) -> Optional[Questao]:
        session = Session()
        questao = session.query(QuestaoEntity).filter(QuestaoEntity.id == codigo).first()
        if questao:
            return questao.to_model()
        return None

    def obter_todos(self) -> List[Questao]:
        session = Session()
        questoes = session.query(QuestaoEntity).all()
        return list(map(lambda q: q.to_model(), questoes))

    def salvar(self, questao: Questao) -> Questao:
        session = Session()
        questao_entity = QuestaoEntity(questao)
        session.add(questao_entity)
        session.commit()
        return questao_entity.to_model()
