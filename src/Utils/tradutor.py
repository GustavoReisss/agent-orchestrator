import jsonpath_ng


# Função que aplica a tradução dos parâmetros
def apply_translation(template, data):
    result = {}

    for key, expression in template.items():
        if type(expression) is dict:
            result[key] = apply_translation(expression, data)
            continue

        jsonpath_expr = jsonpath_ng.parse(expression)
        match = jsonpath_expr.find(data)

        result[key] = match[0].value if match else None

    return result
