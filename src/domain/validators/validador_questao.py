from src.domain.models.questao import Questao
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum


def validador_questao(questao: Questao):
    lista_erros = []
    if not questao.enunciado:
        lista_erros.append("O enunciado é obrigatório.")
    if not questao.disciplina:
        lista_erros.append("A disciplina é obrigatória.")
    if not questao.tipo:
        lista_erros.append("O tipo de questão é obrigatório.")
    if not questao.cadastrador:
        lista_erros.append("O nome do cadastrador da questão precisa ser informado.")
    if not questao.instituicao:
        lista_erros.append("O nome da instituição é obrigatório.")
    if not questao.ano:
        lista_erros.append("O ano da questão é obrigatório.")
    if not questao.ano:
        lista_erros.append("O ano da questão é obrigatório.")
    if not questao.data_cadastro:
        lista_erros.append("A questão precisa de uma data de cadastro.")
    quantidade_alternativas = len(questao.alternativas)
    if quantidade_alternativas < 3 or quantidade_alternativas > 5:
        lista_erros.append("A questão precisa ter no minímo 3 e no máximo 5 alternativas.")
    if (questao.tipo == TipoQuestaoEnum.MULTIPLA_ESCOLHA
            and len(list(filter(lambda it: it.is_correta == True, questao.alternativas))) != 1):
        lista_erros.append("Questões de múltipla escolha deve possuir uma e apenas uma alternativa correta.")

    if len(lista_erros) > 0:
        raise Exception(lista_erros)
