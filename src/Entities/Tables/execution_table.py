from .base_table import Table
from ..Models.execution_model import ExecutionModel, TableModel


class ExecutionTable(Table):
    name: str = "Execution"
    partition_key: str = "executionId"
    # sort_key: str = "despesaId"
    model: TableModel = ExecutionModel
