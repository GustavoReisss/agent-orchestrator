from .base_table_model import TableModel
from enum import Enum


class ExecutionStatusEnum(str, Enum):
    in_progress = "Em Progresso"
    finished = "Finalizado"
    failed = "Falha"


class ExecutionModel(TableModel):
    executionId: str
    status: ExecutionStatusEnum
