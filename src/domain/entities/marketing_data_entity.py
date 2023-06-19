from schematics.types import IntType, FloatType, StringType, DateTimeType

from src.domain.entities.base_entity import BaseEntity

class MarketingDataEntity(BaseEntity):
    id = IntType(required=True)
    month = DateTimeType('%m/%Y', required=True)
    quantidade_empresas = IntType(required=True)
    projetos_executados_por_ano = IntType(required=True)
    nota_glassdoor = FloatType(required=True)
    recomendam_cesar_amigo = FloatType(required=True)
    perspectiva_positiva_cesar = FloatType(required=True)
    indice_sistema_b = FloatType(required=True)
    comunicacao_questoes_chave = StringType(required=True)
    atividades = StringType(required=True)
