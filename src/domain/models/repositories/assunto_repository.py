from abc import ABC, abstractmethod


from src.domain.models.enum.disciplina_enum import DisciplinaEnum


class AssuntoRepository(ABC):

    @abstractmethod
    def buscar_por_disciplina(self, disciplina: DisciplinaEnum):
        pass

    @abstractmethod
    def obter_por_codigo(self, codigo: int):
        pass

