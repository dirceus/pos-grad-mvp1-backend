from flask import redirect, make_response
from flask_cors import CORS
from flask_openapi3 import Tag, Info, OpenAPI

from src.domain.use_cases.buscar_questoes_por_filtro import BuscarQuestoesPorFiltro
from src.domain.use_cases.cadastrar_questao import CadastrarQuestao
from src.domain.use_cases.exibir_questao import ExibirQuestao
from src.domain.use_cases.listar_questoes_ativas import ListarQuestoesAtivas
from src.infrastructure.db.repositories_impl.questao_repository_db_impl import QuestaoRepositoryDbImpl
from src.presentation.schemas.error import ErrorSchema
from src.presentation.schemas.questao_schemas import QuestaoSchema, CadastrarQuestaoSchema, QuestaoPath, \
    FiltroQuestaoSchema, QuestaoSimplesSchema
from src.presentation.utils.handle_errors import handle_errors
from src.presentation.utils.serializer import serializa_dto

info = Info(title="Base de Questões API", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

questao_repository = QuestaoRepositoryDbImpl()

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
questao_tag = Tag(name="Questão", description="Adição, consulta, visualização e desativação de questões na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/api/questao/listar', tags=[questao_tag])
def listar_todas():
    """ Obtêm todas as questões cadastradas com o estado ativo

    Retorna todas as questões ativas.
    """
    try:
        use_case = ListarQuestoesAtivas(questao_repository)
        resultado = use_case.execute(None)
        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@app.get('/api/questao/exibir/<int:codigo>')
def exibir(path: QuestaoPath):
    """Obtêm uma questão pelo código

    :param path: Identificador da questão
    :return: Retorna uma representação de questão de acordo com código.
    """
    try:
        use_case = ExibirQuestao(questao_repository)
        resultado = use_case.execute(path.codigo)
        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@app.post('/api/questao/cadastrar', tags=[questao_tag],
          responses={"200": QuestaoSchema}, )
def cadastrar(body: CadastrarQuestaoSchema):
    """Adiciona uma nova questão na base de dados

    Retorna a representação da questão cadastrada.
    """
    try:
        cadastro_questao_request = body.to_dto()
        use_case_cadastrar_questao = CadastrarQuestao(questao_repository)
        resultado = use_case_cadastrar_questao.execute(cadastro_questao_request)

        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@app.get('/api/questao/buscar', tags=[questao_tag],
         responses={"200": QuestaoSimplesSchema, "400": ErrorSchema, "500": ErrorSchema})
def buscar(body: FiltroQuestaoSchema):
    """Faz uma busca de acordo com filtro de pesquisa
       Retorna as questões que atende ao filtro de pesquisa
    """
    try:
        filtro_request = body.to_dto()
        use_case_buscar_questoes_por_filtro = BuscarQuestoesPorFiltro(questao_repository)
        resultado = use_case_buscar_questoes_por_filtro.execute(filtro_request)
        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)
