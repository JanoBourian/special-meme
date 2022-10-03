class HTTPCustomExceptions(Exception):
    pass

## GENERAL ERRORS 

class HTTPInvalidMethod(HTTPCustomExceptions):
    def __init__(self, method: str):
        self.method = method

    def __str__(self):
        return f"Method {self.method} is not allowed"


class HTTPInteralRequestFailled(HTTPCustomExceptions):
    def __init__(self, request):
        self.request = request

    def __str__(self):
        return f"Internal Request Failled: {self.request}"


class HTTPMissedInfo(HTTPCustomExceptions):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return f"Info Missed: {self.info}"


class GCloudTokenError(HTTPCustomExceptions):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"GCloudToken: {self.message}"
    
## CRUD ERRORS

class PKNotFound(HTTPCustomExceptions):
    def __init__(self, pk:str) -> None:
        self.pk = pk
        self.status_code = 404
    
    def __str__(self):
        return f"{self.pk} not found inside the table or your payload"

class ItemNotExists(HTTPCustomExceptions):
    def __init__(self, pk:str, item:str) -> None:
        self.pk = pk
        self.item = item
        self.status_code = 404
    
    def __str__(self):
        return f"Item with primary key {self.pk} and value {self.item} does not exists"

class ItemAlreadyExists(HTTPCustomExceptions):
    def __init__(self, pk:str, item:str) -> None:
        self.pk = pk
        self.item = item
        self.status_code = 404
    
    def __str__(self):
        return f"Item with primary key {self.pk} and value {self.item} already exists"

class KeyNotFound(HTTPCustomExceptions):
    def __init__(self, pk:str) -> None:
        self.pk = pk
        self.status_code = 404
    
    def __str__(self):
        return f"The key {self.pk} is necessary"
    
class FKNotExists(HTTPCustomExceptions):
    def __init__(self, pk:str) -> None:
        self.pk = pk
        self.status_code = 404
    
    def __str__(self):
        return f"The foreign key {self.pk} does not exists"
    
class CreationError(HTTPCustomExceptions):
    def __init__(self) -> None:
        self.status_code = 404
    
    def __str__(self):
        return f"The items was not created! Please check the fk dependencies or values in your payload"

class UpdatedError(HTTPCustomExceptions):
    def __init__(self) -> None:
        self.status_code = 404
    
    def __str__(self):
        return f"The items was not updated! Please check the fk dependencies or values in your payload"

class DeletedError(HTTPCustomExceptions):
    def __init__(self) -> None:
        self.status_code = 404
    
    def __str__(self):
        return f"The items was not deleted! Please check the fk dependencies or values in your payload"