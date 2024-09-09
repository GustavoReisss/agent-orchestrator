from src.Services.execution_service import ExecutionService


def create_execution(payload):
    new_execution = ExecutionService().create_execution(payload=payload)
    print(new_execution["executionId"])
    return new_execution


if __name__ == "__main__":
    create_execution(
        payload={
            "incidentId": "INC1234567890",
            "input": {
                "incident_description": "Alerta Monitoracao XPTO",
                "incident_additional_information": {
                    "account_id": "123456789",
                    "other_info": "other_info",
                },
            },
            "steps": [
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
            ],
        }
    )
