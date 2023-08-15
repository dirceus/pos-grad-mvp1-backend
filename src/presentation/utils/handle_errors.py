from flask import make_response

from src.domain.commons.exceptions import *


def handle_errors(exception: Exception):
    print(exception.with_traceback(None))
    # status 400
    if isinstance(exception, (InvalidInputException, InvalidStateException)):
        return make_response(str(exception), 400)
    # status 404
    if isinstance(exception, QuestaoNotFoundException):
        return make_response(str(exception), 404)
    # status: erro 500
    if isinstance(exception, (BusinessException, InternalErrorException)):
        return make_response(str(exception), 500)
    # demias excecoes
    return make_response("Erro inesperado", 500)
