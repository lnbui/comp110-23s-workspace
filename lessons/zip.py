"""CQ04: Zip"""

def zip(input_key: list[str], input_value: list[int]) -> dict[str,int]:
    i = 0
    new_dict: dict = {}
    if len(input_key) != len(input_value):
        return new_dict
    elif input_key == {}: 
        return new_dict
    elif input_value == {}:
        return new_dict
    while i < len(input_key):
        new_dict.update({input_key[i]:input_value[i]})
        i += 1
    return new_dict
