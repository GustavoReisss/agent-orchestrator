from pydantic import BaseModel
from src.Repositories.base_table_repository import TableRepository
from src.Entities.Tables.agent_table import AgentTable
from src.Entities.Models.agent_model import AgentModel


class AgentNotFoundException(Exception):
    pass


class AgentService(BaseModel):
    _agent_repository: TableRepository

    def model_post_init(self, __context):
        self._agent_repository = TableRepository(table=AgentTable())

    def get_agent_data(self, agent_name: str) -> AgentModel:
        agent_data = self._agent_repository.get_by_pk(pk=agent_name)

        if len(agent_data) == 0:
            raise AgentNotFoundException()

        return AgentModel(**agent_data[0])

    def create_agent(self, payload: dict) -> AgentModel:
        new_agent = self._agent_repository.create_item(body=payload)[0]

        return new_agent
