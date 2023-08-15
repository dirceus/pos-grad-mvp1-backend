from src.domain.models.dto.assunto_response import AssuntoResponse
from src.domain.models.questao import Questao


class QuestaoCompletaResponse:

    def __init__(self, questao: Questao):
        self.codigo = questao.codigo
        self.tipo = {questao.tipo.name: questao.tipo.value}
        self.enunciado = questao.enunciado
        self.alternativas = questao.alternativas
        self.instituicao = questao.instituicao
        self.ano = questao.ano
        self.evento = questao.evento
        self.disciplina = {questao.disciplina.name: questao.disciplina.value}
        self.assuntos = list(map(lambda a: AssuntoResponse(a),questao.assuntos))
        self.cadastrador = questao.cadastrador
        self.data_cadastro = questao.data_cadastro
        self.ativo = True