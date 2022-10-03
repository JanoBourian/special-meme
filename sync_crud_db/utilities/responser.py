from flask import make_response
from schemas.schemas import ResponseModel
from typing import List
import logging


def create_response(**kwargs):
    resp = ResponseModel(**kwargs).dict()
    logging.warning(f"RESPONSE ROUTINE: {resp}")
    return make_response(resp), resp.get("codigo_ejecucion", 200)


def error_response(error: str, **kwargs):
    logging.warning(f"ERROR ROUTINE: {str(error)}")
    resp = ResponseModel(**kwargs).dict()
    resp["error"] = True
    resp["mensaje_ejecucion"] = str(error)
    logging.warning(f"RESPONSE ROUTINE: {resp}")
    return make_response(resp), resp.get("codigo_ejecucion", 500)