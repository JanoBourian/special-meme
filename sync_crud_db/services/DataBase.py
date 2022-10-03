from sqlalchemy import Table
from sqlalchemy.orm.session import Session
from pydantic.main import ModelMetaclass
from utilities.error_handlers import PKNotFound, ItemNotExists, ItemAlreadyExists, KeyNotFound, FKNotExists, CreationError, UpdatedError, DeletedError
from app.CrudOperations import Operations
from typing import Dict

class DataBase(Operations):
    
    def __init__(self, table:Table, db:Session, schema:ModelMetaclass) -> None:
       Operations.__init__(self, table, db, schema)
    
    def _get(self):
        data = self._get_all_items()
        info_return = [self.schema(**item).dict() for item in data]
        response = { 'codigo_ejecucion': 200, 'mensaje_ejecucion': "OK", 'data': info_return}
        return response
    
    def _post(self, payload:Dict):
        pk = self._get_pk()
        value = payload.get(pk, "")
        if not value:
            raise PKNotFound(pk)
        data = self._get_item_by_pk(pk, payload)
        if data:
            raise ItemAlreadyExists(pk, value)
        
        ## Check necessary keys
        columns = self._get_mandatory_columns()
        for c in columns:
            if not payload.get(c, ""):
                raise KeyNotFound(c)
        
        ## Check that fk items exists
        fk_exists = self._check_fk_dependences()
        if not fk_exists:
            raise FKNotExists(fk_exists)
        
        created_item = self._create_item(payload)
        if not created_item:
            raise CreationError()
        
        info_return = self.schema(**payload).dict()
        response = {'codigo_ejecucion': 201, 'mensaje_ejecucion': "OK", 'data': [info_return]}
        return response
    
    def _patch(self, payload:Dict = {}):
        # check if pk exists
        pk = self._get_pk()
        value = payload.get(pk, "")
        if not value:
            raise PKNotFound(pk)
        data = self._get_item_by_pk(pk, payload)
        if not data:
            raise ItemNotExists(pk, value)
        
        updated = self._update_item(pk, value, payload)
        if not updated:
            raise UpdatedError()
        
        info_return = self.schema(**payload).dict()
        response = { 'codigo_ejecucion': 201, 'mensaje_ejecucion': "OK", 'data': [info_return]}
        return response
    
    def _delete(self, payload):
        # check if pk exists
        pk = self._get_pk()
        value = payload.get(pk, "")
        if not value:
            raise PKNotFound(pk)
        data = self._get_item_by_pk(pk, payload)
        if not data:
            raise ItemNotExists(pk, value)
        
        deleted = self._delete_item(pk, value)
        if not deleted:
            raise DeletedError()
        
        info_return = self.schema(**payload).dict()
        response = { 'codigo_ejecucion': 200, 'mensaje_ejecucion': "OK", 'data': [info_return]}
        return response
