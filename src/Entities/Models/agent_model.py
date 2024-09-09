from .base_table_model import TableModel


class AgentModel(TableModel):
    agentName: str
    description: str
    payload_template: str | dict
    output_template: str | dict
    step_function_arn: str = ""
