from .CrudBuilder import Builder
from sqlalchemy import Table
from sqlalchemy.orm.session import Session
from pydantic.main import ModelMetaclass
from typing import List, Any, Dict
import logging

class Operations(Builder):
    """This class is an instance from Builder and its basic methods for build a CRUD

    Args:
        Builder (Protocol): Inherits the bases from CRUD operations with the Protocol class
    """
    
    def __init__(self, table:Table, db:Session, schema:ModelMetaclass) -> None:
        self.table = table
        self.db = db
        self.schema = schema
    
    def _get_all_items(self) -> List:
        """Retrieve all items inside a Table 

        Returns:
            List: List of items inside some table
        """
        try:
            with self.db:
                return self.db.query(self.table).all()
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            return []
    
    def _get_item_by_pk(self, pk:str = '', payload: Dict = {}):
        try:
            with self.db:
                return self.db.query(self.table).filter(self.table.c[pk] == payload[pk]).first()
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            return []
    
    def _get_pk(self) -> str:
        for column in self.table.columns:
            if column.primary_key:
                return column.name
        return ""
    
    def _get_items_by_filter(self, payload:Dict = {}):
        try:
            with self.db:
                return self.db.query(self.table).filter_by(**payload).first()
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            return []
    
    def _get_mandatory_columns(self) -> List:
        mandatory_keys = []
        for c in self.table.columns:
            if c.primary_key or (not c.nullable) or c.foreign_keys:
                mandatory_keys.append(c.key)
        return mandatory_keys
    
    def _check_fk_dependences(self): 
        for c in self.table.columns:
            if c.foreign_keys:
                pass
        return True
    
    def _create_item(self, payload:Dict = {}):
        try:
            with self.db:
                self.db.execute(self.table.insert().values(**payload))
                self.db.commit()
            return True
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            return False
    
    def _update_item(self, pk:str = '', value:Any = None, payload:Dict = None):
        try:
            with self.db:
                self.db.execute(self.table.update().where(self.table.c[pk] == value).values(**payload))
                self.db.commit()
            return True
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            return False
    
    def _delete_item(self, pk:str = '', value:Any = None): 
        try:
            with self.db:
                self.db.execute(self.table.delete().where(self.table.c[pk] == value))
                self.db.commit()
            return True
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            return False