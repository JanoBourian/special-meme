from typing import List, Any
import logging

def concatenate_strings(items:List) -> str:
    try:
        result = ''
        for item in items:
            result = result + convert_item(item)
        return clean_item(result)
    except Exception as e:
        logging.warnign(f"ERROR: {e}")
    
def verify_item(item:Any) -> str:
    """This functions convert a return strings
    Here you can write new or aditional validations

    Args:
        item (Any): item to convert

    Returns:
        str: item as string
    """
    return str(item)

def convert_item(item:Any) -> str:
    return verify_item(item) + ' '

def clean_item(item:str) -> str:
    return item.strip()