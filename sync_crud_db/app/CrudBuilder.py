from typing import Protocol, List, Optional

class Builder(Protocol):
    """This class is the Base for type the different methods in CRUD operations

    Args:
        Protocol (Protocol): Protocol from typing
    """
    
    ## get all items
    def _get_all_items(self): ...
    
    # ## get item by pk
    def _get_item_by_pk(self): ...
    
    ## get pk in Table
    def _get_pk(self): ...
    
    ## get item by some filter
    def _get_items_by_filter(self): ...
    
    ## get necessary columns
    def _get_mandatory_columns(self): ...
    
    ## check if fk exists in the other tables
    def _check_fk_dependences(self): ...
    
    ## create item
    def _create_item(self): ...
    
    ## update some item (n parameters)
    def _update_item(self): ...
    
    ## delete item 
    def _delete_item(self): ...