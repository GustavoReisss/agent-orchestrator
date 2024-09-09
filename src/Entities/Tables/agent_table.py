from .base_table import Table
from ..Models.agent_model import AgentModel, TableModel


class AgentTable(Table):
    name: str = "Agent"
    partition_key: str = "agentName"
    model: TableModel = AgentModel
