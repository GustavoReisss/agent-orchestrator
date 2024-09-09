from src.Services.execution_service import ExecutionService
from src.Entities.Models.execution_model import ExecutionStep, StepStatusEnum
from src.Services.agent_service import AgentService
from src.Utils.tradutor import apply_translation


class NoMoreStepsRemaningException(Exception):
    pass


FIELDS_TO_EXCLUDE = ["steps", "status", "created_on", "update_on"]


def get_current_step(steps: list[ExecutionStep]):
    current_step = next(
        (step for step in steps if step.status == StepStatusEnum.waiting), None
    )

    if current_step is None:
        raise NoMoreStepsRemaningException()

    return current_step


def make_next_step_payload(execution_id: str):
    execution_data = ExecutionService().get_execution_data(execution_id=execution_id)

    steps = execution_data.steps

    current_step = get_current_step(steps)
    # print(current_step)

    agent = AgentService().get_agent_data(agent_name=current_step.action)

    agent_payload = apply_translation(
        template=current_step.input_template,
        data=execution_data.model_dump(exclude=FIELDS_TO_EXCLUDE),
    )

    # print(agent_payload)

    return {
        "executionId": execution_id,
        "agentName": agent.agentName,
        "payload": agent_payload,
        "step_function_arn": agent.step_function_arn,
    }


def execute_step_and_get_response(step_payload: dict):
    mock_responses = {
        "agente_diagnostico": {
            "diagnose": f"Diagnóstico do problema: {step_payload['payload']['description']}"
        },
        "agente_automation": {"automation_name": "resolve-alerta-xpto"},
    }

    print(f"\nCurrent Step: {step_payload['agentName']}")

    return mock_responses[step_payload["agentName"]]


def execute_orchestration(execution_id: str):
    step_function_payload = make_next_step_payload(execution_id=execution_id)
    print(step_function_payload)

    step_response = execute_step_and_get_response(step_payload=step_function_payload)

    print(step_response)


def main():
    execution_id = "36833ea4-447b-4948-8e8f-37d0a02c5794"

    execute_orchestration(execution_id)


if __name__ == "__main__":
    main()
