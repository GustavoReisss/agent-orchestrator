from src.Services.execution_service import ExecutionService, ExecutionNotFoundException
from src.Entities.Models.execution_model import ExecutionStatusEnum
import json

execution_service = ExecutionService()


# Salva solicitação de execução no banco de dados
def post_execution(body: dict):
    new_execution = execution_service.create_execution(payload=body)
    return new_execution


def update_execution(execution_id: str, payload: dict):
    updated_execution = execution_service.update_execution(
        execution_id=execution_id, body=payload
    )

    print(updated_execution)

    return updated_execution


# Decide o próximo step
def orquestrador(execution_id: str):

    try:
        execution_data = execution_service.get_execution_data(execution_id=execution_id)

    except ExecutionNotFoundException:
        print(f"Execution Id '{execution_id}' not found on database")

    if "automation_name" in execution_data:
        return "finished"

    if "diagnose" in execution_data:
        return "agent-automation-identification"

    return "agent-diagnose-incident"


def call_next_step(execution_id: str, next_step: str = ""):
    agents = {
        "agent-automation-identification": {"automation_name": "Automation Name"},
        "agent-diagnose-incident": {"diagnose": "Diagnose"},
    }

    return agents.get(next_step, {})


def main():
    # Create execution

    incident = {
        "id": "INC123456789",
        "additional_information": json.dumps({"aws_account": "123456789012"}),
    }

    execution = post_execution(body=incident)

    print(execution)

    execution_id = execution["executionId"]

    while True:
        next_step = orquestrador(execution_id=execution_id)
        print("\nNext step: ", next_step, "\n")

        if next_step == "finished":
            update_execution(
                execution_id=execution_id,
                payload={"status": ExecutionStatusEnum.finished},
            )
            break

        result = call_next_step(execution_id=execution_id, next_step=next_step)
        update_execution(execution_id=execution_id, payload=result)


if __name__ == "__main__":
    main()
