from schematics.types import IntType, StringType, DateTimeType

from src.domain.entities.base_entity import BaseEntity

class CouncilDataEntity(BaseEntity):
    id = IntType(required=True)
    month = DateTimeType('%m/%Y', required=True)
    governanca_estrutura_composicao = StringType(required=True)
    presidente_conselho = StringType(required=True)
    papel_presidente_conselho_gestao_impacto = StringType(required=True)
    delegacao_responsabilidade_gestao_impacto = StringType(required=True)
