from flask import Request, make_response
from utilities.measure_time import measure_time
from services.DataBase import DataBase
from connection.connection import db
from connection.models import CatTipoCatalogo, VariableDocumentacion
from schemas import schemas 
from utilities.error_handlers import PKNotFound, ItemNotExists, ItemAlreadyExists, KeyNotFound, FKNotExists, CreationError, UpdatedError
import logging

@measure_time("services-general-crud")
def run_function(request:Request):
    try:
        database = DataBase(CatTipoCatalogo, db, schemas.CatTipoCatalogo)
        logging.warning(f"You are checking {database.table.name}")
        logging.warning(f"METHOD: {request.method}")
        if request.method == "GET":    
            result = database._get()
            return make_response(schemas.SuccessResponse(**result).dict()), result.get("codigo_ejecucion")
        elif request.method == "POST":
            data = request.json
            logging.warning(f"DATA: {data}")
            result = database._post(data)
            return make_response(schemas.SuccessResponse(**result).dict()), result.get("codigo_ejecucion")
        elif request.method == "PATCH":
            data = request.json
            logging.warning(f"DATA: {data}")
            result = database._patch(data)
            return make_response(schemas.SuccessResponse(**result).dict()), result.get("codigo_ejecucion")
        elif request.method == "DELETE":
            data = request.json
            logging.warning(f"DATA: {data}")
            result = database._delete(data)
            return make_response(schemas.SuccessResponse(**result).dict()), result.get("codigo_ejecucion")
        else:
            logging.warning(f"Method Not Allowed")
            logging.warning(f"REQUEST: {request}")
            return make_response({"method": f"{request.method}"})
    except PKNotFound as e:
        logging.warning(f"ERROR: {e}")
        return make_response({"error": f"{e}"}), e.status_code
    except ItemNotExists as e:
        logging.warning(f"ERROR: {e}")
        return make_response({"error": f"{e}"}), e.status_code
    except ItemAlreadyExists as e:
        logging.warning(f"ERROR: {e}")
        return make_response({"error": f"{e}"}), e.status_code
    except KeyNotFound as e:
        logging.warning(f"ERROR: {e}")
        return make_response({"error": f"{e}"}), e.status_code
    except FKNotExists as e:
        logging.warning(f"ERROR: {e}")
        return make_response({"error": f"{e}"}), e.status_code
    except CreationError as e:
        logging.warning(f"ERROR: {e}")
        return make_response({"error": f"{e}"}), e.status_code
    except UpdatedError as e:
        logging.warning(f"ERROR: {e}")
        return make_response({"error": f"{e}"}), e.status_code
    except Exception as e:
        logging.warning(f"ERROR {e}")
        return make_response({"error": f"{e}"}), 500