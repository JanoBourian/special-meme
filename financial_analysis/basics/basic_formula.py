### Present to future Delayed

def present_to_future(value:float, periods:int, rate:float) -> float:
    ## Some validations
    return round(value*((1+rate)**periods), 2)