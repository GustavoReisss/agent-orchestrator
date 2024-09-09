from src.Entities.Models.base_table_model import TableModel, BaseModel
from enum import Enum


class ExecutionStatusEnum(str, Enum):
    in_progress = "Em Progresso"
    finished = "Finalizado"
    failed = "Falha"


class StepStatusEnum(str, Enum):
    waiting = "Aguardando"
    finished = "Finalizado"
    failed = "Falha"


class ExecutionStep(BaseModel):
    name: str
    action: str
    input_template: str | dict
    status: StepStatusEnum = StepStatusEnum.waiting


class ExecutionModel(TableModel):
    executionId: str
    status: ExecutionStatusEnum
    input: str | dict
    steps: list[ExecutionStep]
    created_on: str
    updated_on: str
    incidentId: str
