def paginate_list(list: list, current_page: int, elements_per_page: int):
    inicio = (current_page - 1) * elements_per_page
    fin = inicio + elements_per_page
    page = list[inicio:fin]
    return page

def filter_dictionary(original_dictionary: dict, keys: list):
    return {key: original_dictionary[key] for key in keys}
