from src.Services.agent_service import AgentService


def create_agent(payload):
    new_agent = AgentService().create_agent(payload=payload)
    print(new_agent["agentName"])

    return new_agent


if __name__ == "__main__":
    create_agent(
        {
            "agentName": "agente_diagnostico",
            "description": "Realiza Diagnóstico de incidentes de monitoraçao",
            "payload_template": {
                "description": "Descrição do Incidente",
                "additional_information": {"info_extra_1": "informação complementar"},
            },
            "output_template": {"diagnose": "Diagnóstico do incidente"},
            "step_function_arn": "stf_arn_agent_diagnostico",
        }
    )

    create_agent(
        {
            "agentName": "agente_diagnostico",
            "description": "Retorno o nome da automação que mais tem potencial para resolver um determinado problema",
            "payload_template": {
                "problem_description": "Detalhamento do problema enfrentado",
            },
            "output_template": {"automation_name": "Nome-da-Automação"},
            "step_function_arn": "stf_arn_agent_identificacao",
        }
    )
