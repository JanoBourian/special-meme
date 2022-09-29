from typing import Protocol, List, Optional

class Builder(Protocol):
    
    ## get all items
    def get_all_items(self): ...
    
    # ## get item by pk
    def get_item_by_pk(self): ...
    
    ## get pk in Table
    def _get_pk(self): ...
    
    ## get item by some filter
    def get_items_by_filter(self): ...
    
    # ## create item
    # def create_item(self): ...
    
    # ## update some item (n parameters)
    # def update_item(self): ...
    
    # ## delete item 
    # def delete_item(self): ...