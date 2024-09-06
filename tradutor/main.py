from tradutor import make_agent_input
from config_agentes import CONFIG_AGENTES
import sys


def agent_call(agent_name: str, input_data: any):
    print(f"Agente {agent_name} recebeu: {input_data}")


def main():
    agent_name = sys.argv[1]

    print("Agent name: ", agent_name)

    if agent_name not in CONFIG_AGENTES:
        raise ValueError("Agente inválido")

    input_data = {
        "incident_id": "INC1234567890",
        "additional_information": {"KEY1": {"KEY2": "VALUE2"}},
        "severity": "HIGH",
        "list": [{"KEY1": {"KEY2": [{"KEY1": {"KEY2": "VALUE2"}}, "item index 1"]}}, "item index 1"]
    }

    agent_input = make_agent_input(
        input_data=input_data,
        config_mapeamento=CONFIG_AGENTES.get(agent_name),
    )

    agent_call(agent_name=agent_name, input_data=agent_input)


if __name__ == "__main__":
    main()
