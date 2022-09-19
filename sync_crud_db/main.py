from flask import Request
from utilities.measure_time import measure_time

import logging

@measure_time("function-name")
def run_function(request:Request):
    try:
        logging.warning(f"All ok!")
        logging.warning(f"REQUEST: {request}")
    except Exception as e:
        logging.warning(f"ERROR {e}")
    finally:
        logging.warning(f"CLOSE FUNCTION")