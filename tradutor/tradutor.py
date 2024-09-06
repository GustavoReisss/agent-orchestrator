import re

# KEY_WITH_INDEX_REGEX = r"\[\d+\]" # verifica se o digito dentro do colchete é númerico
KEY_WITH_INDEX_REGEX = r"\[.*?\]" # libera qualquer caracter dentro dos colchetes


def get_input_value(input_data: dict, caminho: str):
    if caminho == "$":
        return input_data

    value = input_data
    path = caminho.strip("$.").split(".")
    

    for key in path:
        index = None

        if re.search(KEY_WITH_INDEX_REGEX, key):
            key_splitted: list[str] = key.split("[")
            key = key_splitted[0]

            index = key_splitted[1].replace("]", "")

            if index.isdigit():
                index = int(index)
            else:
                raise ValueError(f"Só é possível ler números inteiros como index para listas e não '{index}'")


        if key in value:
            value = value[key]
                          
            if index is not None:
                value = value[index]

            continue

        value = None
        break

    return value


def make_agent_input(input_data: dict, config_mapeamento: str | dict):
    if type(config_mapeamento) not in [str, dict]:
        raise TypeError(
            f"parâmetro 'config_mapeamento' deve ser uma string ou json/dict válido e não {type(config_mapeamento)}"
        )

    if isinstance(config_mapeamento, str):
        return get_input_value(input_data=input_data, caminho=config_mapeamento)

    novo_input = {}

    for chave_nova, caminho in config_mapeamento.items():
        if type(caminho) == dict:
            novo_input[chave_nova] = make_agent_input(
                input_data=input_data, config_mapeamento=caminho
            )
            continue

        novo_input[chave_nova] = get_input_value(input_data=input_data, caminho=caminho)

    return novo_input
