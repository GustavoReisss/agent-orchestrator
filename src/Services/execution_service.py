from pydantic import BaseModel
from src.Repositories.base_table_repository import TableRepository
from src.Entities.Tables.execution_table import ExecutionTable
from ..Entities.Models.execution_model import ExecutionStatusEnum, ExecutionModel
import uuid
from datetime import datetime


class ExecutionNotFoundException(Exception):
    pass


class ExecutionAlreadyExistsException(Exception):
    pass


class ExecutionPayload(BaseModel):
    incidentId: str
    steps: list[dict]
    input: str | dict


class ExecutionService(BaseModel):
    _execution_repository: TableRepository

    def model_post_init(self, __context):
        self._execution_repository = TableRepository(table=ExecutionTable())

    def get_execution_data(self, execution_id: str) -> ExecutionModel:
        execution_data = self._execution_repository.get_by_pk(pk=execution_id)

        if len(execution_data) == 0:
            raise ExecutionNotFoundException()

        return ExecutionModel(**execution_data[0])

    def update_execution(self, execution_id: str, body: dict):
        body["updated_on"] = str(datetime.now())

        updated_execution = self._execution_repository.update_item(
            pk=execution_id, new_values=body
        )[0]

        return updated_execution

    def create_execution(self, payload) -> dict:
        execution_payload = ExecutionPayload(**payload)

        timestamp = str(datetime.now())
        execution_id = str(uuid.uuid4())

        new_execution = {
            "executionId": execution_id,
            "status": ExecutionStatusEnum.in_progress,
            "created_on": timestamp,
            "updated_on": timestamp,
            **execution_payload.model_dump(),
        }

        result = self._execution_repository.create_item(body=new_execution)[0]

        return result
