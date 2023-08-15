from flask import Blueprint, request, make_response

from src.domain.use_cases.cadastrar_questao import CadastrarQuestao
from src.domain.use_cases.exibir_questao import ExibirQuestao
from src.domain.use_cases.listar_questoes_ativas import ListarQuestoesAtivas
from src.infrastructure.db.repositories_impl.questao_repository_db_impl import QuestaoRepositoryDbImpl
from src.presentation.utils.deserializers import deserialize_cadastro_questao_request
from src.presentation.utils.handle_errors import handle_errors
from src.presentation.utils.serializer import get_json
from src.infrastructure.db.connection import Session

questao_router_bp = Blueprint("questao_router", __name__)

# alternativa_repository = AlternativaRepositoryMemImpl()
# questao_repository = QuestaoRepositoryMemImpl(alternativa_repository)

questao_repository = QuestaoRepositoryDbImpl()


@questao_router_bp.route("/questao/listar", methods=["GET"])
def listar_todas():
    try:
        use_case = ListarQuestoesAtivas(questao_repository)
        resultado = use_case.execute(None)
        return make_response(get_json(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@questao_router_bp.route("/questao/exibir/<int:codigo>", methods=["GET"])
def exibir(codigo: int):
    try:
        use_case = ExibirQuestao(questao_repository)
        resultado = use_case.execute(codigo)
        return make_response(get_json(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@questao_router_bp.route("/questao/cadastrar", methods=["POST"])
def cadastrar():
    try:
        cadastro_questao_request = deserialize_cadastro_questao_request(request)
        use_case_cadastrar_questao = CadastrarQuestao(questao_repository)
        resultado = use_case_cadastrar_questao.execute(cadastro_questao_request)
        return make_response(get_json(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@questao_router_bp.route("/questao/buscar", methods=["GET"])
def buscar():
    try:
        return ListarQuestoesAtivas(questao_repository)
    except Exception as ex:
        return handle_errors(ex)
