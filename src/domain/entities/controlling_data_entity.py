from schematics.types import IntType, FloatType, DateTimeType

from src.domain.entities.base_entity import BaseEntity

class ControllingDataEntity(BaseEntity):
    id = IntType(required=True)
    month = DateTimeType('%m/%Y', required=True)
    ebitda = FloatType(required=True)
    faturamento = FloatType(required=True)
