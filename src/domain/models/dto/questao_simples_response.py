from src.domain.models.questao import Questao


class QuestaoSimplesResponse:

    def __init__(self, questao: Questao):
        self.codigo = questao.codigo
        self.tipo = {questao.tipo.name: questao.tipo.value}
        self.enunciado = questao.enunciado
        self.instituicao = questao.instituicao
        self.ano = questao.ano
        self.evento = questao.evento
        self.disciplina = {questao.disciplina.name: questao.disciplina.value}
        self.cadastrador = questao.cadastrador
        self.data_cadastro = questao.data_cadastro
        self.ativo = True