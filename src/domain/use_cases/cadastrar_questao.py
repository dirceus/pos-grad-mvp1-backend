from datetime import datetime

from src.domain.commons.use_case import UseCase
from src.domain.commons.usuario_logado import obter_usuario_logado
from src.domain.models.dto.cadastro_questao_request import CadastroQuestaoRequest
from src.domain.models.dto.questao_completa_response import QuestaoCompletaResponse
from src.domain.models.repositories.questao_repository import QuestaoRepository
from src.domain.validators.validador_questao import validador_questao


class CadastrarQuestao(UseCase):

    def __init__(self, repositorio: QuestaoRepository):
        self.__repositorio = repositorio

    def execute(self, request: CadastroQuestaoRequest):
        nome_cadastrador = obter_usuario_logado()
        questao = request.to_model()
        questao.cadastrador = nome_cadastrador
        questao.data_cadastro = datetime.now()
        validador_questao(questao)
        return QuestaoCompletaResponse(self.__repositorio.salvar(questao))
