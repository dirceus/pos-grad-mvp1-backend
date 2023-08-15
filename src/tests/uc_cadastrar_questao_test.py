import unittest

from src.domain.models.alternativa import Alternativa
from src.domain.models.dto.alternativa_response import AlternativaResponse
from src.domain.models.dto.cadastro_questao_request import CadastroQuestaoRequest
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum
from src.domain.use_cases.cadastrar_questao import CadastrarQuestao
from src.infrastructure.memory.repositories_impl.alternativa_repository_mem_impl import AlternativaRepositoryMemImpl
from src.infrastructure.memory.repositories_impl.questao_repository_mem_impl import QuestaoRepositoryMemImpl


class UcCadastrarQuestaoTest(unittest.TestCase):
    def test_cadastra_questao_na_base_em_memoria(self):
        alternativa_repository = AlternativaRepositoryMemImpl()
        questao_repostository = QuestaoRepositoryMemImpl(alternativa_repository)

        uc_cadastro_questao = CadastrarQuestao(questao_repostository)
        lista_alternativas = [
            AlternativaResponse(Alternativa(None, "Alternativa 1", True)),
            AlternativaResponse(Alternativa(None, "Alternativa 2", False)),
            AlternativaResponse(Alternativa(None, "Alternativa 3", False)),
            AlternativaResponse(Alternativa(None, "Alternativa 4", False)),
            AlternativaResponse(Alternativa(None, "Alternativa 5", False))]

        request_cadastro_questao = CadastroQuestaoRequest(TipoQuestaoEnum.MULTIPLA_ESCOLHA,
                                                          "Enunciado da questão: ",
                                                          lista_alternativas,
                                                          "PUC-RIO",
                                                          2023,
                                                          "MVP Sprint 1 - Pós-Eng Sw",
                                                          DisciplinaEnum.INFORMATICA,
                                                          [])

        questao_salva = uc_cadastro_questao.execute(request_cadastro_questao)

        self.assertEqual(1, questao_salva.codigo)


if __name__ == '__main__':
    unittest.main()
