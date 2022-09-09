from typing import Optional, Union, Tuple
import logging

## Important prefix
UNIDADES = {
    "0": "",
    "1": "UN",
    "2": "DOS",
    "3": "TRES",
    "4": "CUATRO",
    "5": "CINCO",
    "6": "SEIS",
    "7": "SIETE",
    "8": "OCHO",
    "9": "NUEVE",
}

DECENAS = {
    "10": "DIEZ",
    "20": "VEINTE",
    "30": "TREINTA",
    "40": "CUARENTA",
    "50": "CINCUENTA",
    "60": "SESENTA",
    "70": "SETENTA",
    "80": "OCHENTA",
    "90": "NOVENTA",
}

CENTENAS = {
    "100": "CIENTO",
    "200": "DOSCIENTOS",
    "201": "DOSCIENTOS UN",
    "300": "TRESCIENTOS",
    "400": "CUATROCIENTOS",
    "500": "QUINIENTOS",
    "600": "SEISCIENTOS",
    "700": "SETECIENTOS",
    "800": "OCHOCIENTOS",
    "900": "NOVECIENTOS",
}

EXCEPTIONS = {
    "11": "ONCE",
    "12": "DOCE",
    "13": "TRECE",
    "14": "CATORCE",
    "15": "QUINCE",
    "16": "DIECISEIS",
    "17": "DIECISIETE",
    "18": "DIECIOCHO",
    "19": "DIECINUEVE",
    "21": "VEINTIUN",
    "22": "VEINTIDOS",
    "23": "VEINTITRES",
    "24": "VEINTICUATRO",
    "25": "VEINTICINCO",
    "26": "VEINTISEIS",
    "27": "VEINTISIETE",
    "28": "VEINTIOCHO",
    "29": "VEINTINUEVE",
    "31": "TREINTA Y UN",
    "41": "CUARENTA Y UN",
    "51": "CINCUENTA Y UN",
    "61": "SESENTA Y UN",
    "71": "SETENTA Y UN",
    "81": "OCHENTA Y UN",
    "91": "NOVENTA Y UN",
    "100": "CIEN",
    "101": "CIENTO UN",
}

INDICADOR = [
    ("", ""),
    ("MIL", "MIL"),
    ("MILLON", "MILLONES"),
    ("MIL MILLONES", "MIL MILLONES"),
    ("BILLON", "BILLONES"),
    ("MIL BILLONES", "MIL BILLONES"),
    ("TRILLON", "TRILLONES"),
    ("MIL TRILLONES", "MIL TRILLONES"),
]


def number_to_string(number: Optional[Union[int, float, str]]) -> Tuple:
    ## Evaluate if it is a number
    try:
        text = ""
        ## Only can convert with eval if is str
        if isinstance(number, str):
            number = eval(number)
        integer = int(number)  ## Integer part

        if not integer:
            text = text + "CERO "
        else:
            ## Here we check the number of digits in the integer part
            number_string = str(integer)
            index_indicador = 1
            while integer >= 1000**index_indicador:
                index_indicador = index_indicador + 1
            list_temporal = []
            for i in range(index_indicador):
                if i == 0:
                    list_item = number_string[-3 * (i + 1) :]
                else:
                    list_item = number_string[-3 * (i + 1) : -3 * (i)]
                list_temporal.append(list_item)
            iterations = len(list_temporal)
            current_indicador = INDICADOR[:index_indicador]

            while iterations > 0:
                text = text + _set_name(
                    list_temporal[iterations - 1], current_indicador[iterations - 1]
                )
                iterations = iterations - 1

        ## Decimal part
        decimal = int(round((number - integer) * 100))
        text = text + f"PESOS {decimal}/100 M.N."
        text = _delete_spaces_and_corrections(text)

        return (number, text)
    except Exception as e:
        logging.warning(f"ERROR IN NUMBER_TO_STRING {e}")


def _set_name(block: str, indicator: Tuple) -> str:

    string_back = ""
    if not int(block):
        return string_back

    ## Now check coincidence inside the set variables
    for array in [EXCEPTIONS, CENTENAS, DECENAS, UNIDADES]:
        for k, v in array.items():
            if block == k:
                return string_back + v + _get_indicator(block, indicator)

    ## Centenas
    check_centenas = str(int(block) - int(block) % 100)
    if check_centenas:
        string_back = _check_by_dict(CENTENAS, string_back, check_centenas)

    ## Decenas
    check_decenas = str(int(block) - int(check_centenas))
    exceptions = _check_exceptions(check_decenas, indicator)
    if exceptions:
        return string_back + exceptions

    check_decenas = str(int(check_decenas) - int(check_decenas) % 10)
    if check_decenas:
        string_back = _check_by_dict(DECENAS, string_back, check_decenas)

    ## Unidades
    check_unidades = str(int(block) - int(int(check_centenas) + int(check_decenas)))
    if check_unidades:
        for k, v in UNIDADES.items():
            if check_unidades == k and v:
                string_back = (
                    string_back + v
                    if int(check_decenas) < 10
                    else string_back + "Y " + v
                )

    return string_back + _get_indicator(block, indicator)


def _get_indicator(block: str, indicator: Tuple) -> str:
    if indicator[0] and block:
        return (
            "  " + indicator[0] + "  " if block == "1" else "  " + indicator[1] + "  "
        )
    return " "


def _delete_spaces_and_corrections(text: str) -> str:
    for i in range(2, 10):
        text = text.replace(" " * i, " ")
    # Another exceptions
    if "Y UN MIL" not in text:
        text = text.replace("UN MIL ", "MIL ")
    for i in range(2, 4):
        text = text.replace(" " * i, " ")
    return text


def _check_exceptions(block: str, indicator: Tuple) -> str:
    for k, v in EXCEPTIONS.items():
        if block == k:
            return v + _get_indicator(block, indicator)
    return ""


def _check_by_dict(array: dict, string_back: str, values: str) -> str:
    for k, v in array.items():
        if values == k and v:
            return string_back + v + " "
    return string_back


print(number_to_string(1))
print(number_to_string(10))
print(number_to_string(100))
print(number_to_string(1000))
print(number_to_string(10000))
print(number_to_string(100000))
print(number_to_string(1000000))
print(number_to_string(10000000))
print(number_to_string(100000000))
print(number_to_string(1000000000))
print(number_to_string(10000000000))
print(number_to_string(100000000000))
print(number_to_string(1000000000000))
print(number_to_string(10000000000000))
print(number_to_string(100000000000000))
print(number_to_string(1000000000000000))
print(number_to_string(10000000000000000))
print(number_to_string(100000000000000000))
print(number_to_string(1000000000000000000))
print(number_to_string(1000))
print(number_to_string(1001))
print(number_to_string(1002))
print(number_to_string(2000))
print(number_to_string(20000))
print(number_to_string(31000))
print(number_to_string(310000))
print(number_to_string(1000000))
# for i in range(10000, 20000):
#     print(number_to_string(i))
#     input()
