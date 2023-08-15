from flask import request as FlaskRequest

from src.domain.models.alternativa import Alternativa
from src.domain.models.assunto import Assunto
from src.domain.models.dto.alternativa_response import AlternativaResponse
from src.domain.models.dto.cadastro_questao_request import CadastroQuestaoRequest
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum


def deserialize_cadastro_questao_request(request: FlaskRequest) -> CadastroQuestaoRequest:
    tipo = TipoQuestaoEnum[request.json["tipo"]]
    enunciado = request.json["enunciado"]
    alternativas = request.json["alternativas"]
    alternativas_dto = list(map(lambda it: AlternativaResponse(Alternativa(None, it["descricao"], it["is_correta"])), alternativas))
    instituicao = request.json["instituicao"]
    ano = request.json["ano"]
    evento = request.json["evento"]
    disciplina = DisciplinaEnum[request.json["disciplina"]]
    codigos_assunto = request.json["assuntos"]
    assuntos = list(map(lambda it: Assunto(it, disciplina, None), codigos_assunto))

    return CadastroQuestaoRequest(tipo, enunciado, alternativas_dto, instituicao, ano, evento, disciplina, assuntos)
