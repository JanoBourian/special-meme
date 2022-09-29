from .CrudBuilder import Builder
from sqlalchemy import Table
from sqlalchemy.orm.session import Session
from typing import List, Any, Dict
import logging

class Operations(Builder):
    
    def __init__(self, table:Table, db:Session) -> None:
        self.table = table
        self.db = db
    
    def get_all_items(self) -> List:
        logging.warning(f"INSIDE get_all_items method")
        try:
            with self.db:
                return self.db.query(self.table).all()
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            return []
    
    def get_item_by_pk(self, payload: Dict):
        try:
            id_ = self._get_pk()
            with self.db:
                return self.db.query(self.table).filter(self.table.c[id_] == payload[id_]).first()
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            return []
    
    def _get_pk(self) -> str:
        for column in self.table.columns:
            if column.primary_key:
                return column.name
        return ""
    
    def get_items_by_filter(self):
        pass