from os import access
from environs import Env
from google.cloud import secretmanager

def get_secrets(env: Env):
    '''
    Función que obtiene los secrets desde GCP para cualquier entorno
    '''
    PROJECT_ID = env('PROJECT_ID')
    SECRET_ID = env('EXPEDIENTE_DB_PASSWORD')
    SECRET_USER = env('EXPEDIENTE_DB_USER')
    # Create the Secret Manager client
    client = secretmanager.SecretManagerServiceClient()
    # Build the resource name of the secret version
    name = f"projects/{PROJECT_ID}/secrets/{SECRET_ID}/versions/latest"
    access = f"projects/{PROJECT_ID}/secrets/{SECRET_USER}/versions/latest"
    # Access the secret version
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")

    resp = client.access_secret_version(request={"name": access})
    resp_acces = resp.payload.data.decode("UTF-8")
    return {'contrasena': payload, 'user': resp_acces}