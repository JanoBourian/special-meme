import google.auth.transport.requests
import google.oauth2.id_token
from config.config import env
import subprocess
from utilities.error_handlers import GCloudTokenError
import logging


class GCloudToken:
    endpoint = ""

    def get_token(self) -> str:
        # comentar para desarrollo local,  hasta que se solucione las keys
        try:
            enviroment = env("ENV")
            if enviroment != "local":
                auth_req = google.auth.transport.requests.Request()
                id_token = google.oauth2.id_token.fetch_id_token(
                    auth_req, self.endpoint
                )
            else:
                id_token = self.local_oauth2()
            return id_token
        except Exception as e:
            logging.warning(f"ERROR to GET TOKEN {e}")
            raise GCloudTokenError("No se pudo obtener el token")

    def local_oauth2(self) -> str:
        code = subprocess.run(
            "gcloud auth print-identity-token",
            stdout=subprocess.PIPE,
            check=True,
            shell=True,
        ).stdout
        head = code.decode("utf-8")
        head = head.replace("\r", "")
        head = head.replace("\n", "")
        return head
