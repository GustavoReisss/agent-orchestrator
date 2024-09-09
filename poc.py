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


# Funções dos agentes
def agente_diagnostico(input_data):
    # Simulando um diagnóstico com base na descrição
    print(f"[agente_diagnostico] input: {input_data}")

    return {
        "diagnose": f"Problema relacionado a {input_data['description']} na conta AWS {input_data['additional_information']['account_id']}"
    }


def agente_identificacao(input_data):
    # Simulando uma identificação de automação
    print(f"[agente_identificacao] input: {input_data}")

    return {"automation_name": "resolve-alerta-xpto"}


# Função principal de orquestração
def executar_orquestracao(data_inicial, steps):
    dados_atualizados = {"input": data_inicial}

    actions = {
        "agente_diagnostico": agente_diagnostico,
        "agente_identificacao": agente_identificacao,
    }

    for step_info in steps:
        step_name = step_info["name"]

        print(f"Executando {step_name}...")

        # Aplicando a tradução de input para o agente
        input_traduzido = apply_translation(
            step_info["input_template"], dados_atualizados
        )

        # Executando o agente
        agente_func = actions[step_info["action"]]
        output_agente = agente_func(input_traduzido)

        # Atualizando os dados gerais com o output do agente
        dados_atualizados[f"agent_{step_name}"] = output_agente

        print(f"Resultado do {step_name}: {output_agente}\n")

    return dados_atualizados


# Exemplo de input inicial
input_inicial = {
    "incident_id": "INC123456789",
    "incident_description": "Alerta Monitoracao XPTO",
    "incident_additional_information": {
        "account_id": "123456789",
        "other_info": "other_info",
    },
}

# Definição dos steps e templates
steps = [
    {
        "name": "diagnostico de incidente",
        "action": "agente_diagnostico",
        "input_template": {
            "description": "$.input.incident_description",
            "additional_information": {
                "account_id": "$.input.incident_additional_information.account_id",
                "account_additional_info": {
                    "account_name": "$.input.incident_additional_information.account_name",
                    "account_type": "$.input.incident_additional_information.account_type",
                },
            },
        },
    },
    {
        "name": "identificacao de automacao",
        "action": "agente_identificacao",
        "input_template": {"problem_description": "$"},
    },
]

# Executando a orquestração
resultado_final = executar_orquestracao(input_inicial, steps)
print("Resultado Final:", resultado_final)
