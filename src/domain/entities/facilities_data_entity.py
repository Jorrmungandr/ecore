from schematics.types import IntType, FloatType

from src.domain.entities.base_entity import BaseEntity

class FacilitiesDataEntity(BaseEntity):
    id = IntType(required=True)
    consumo_mensal_de_energia_eletrica = FloatType(required=True)
    prop_energia_mercado_livre = FloatType(required=True)
    prop_energia_mercado_cativo = FloatType(required=True)
    peso_residuos_solidos = FloatType(required=True)
    gravimetria_residuo_organico = FloatType(required=True)
    gravimetria_residuo_papel = FloatType(required=True)
    gravimetria_residuo_plastico = FloatType(required=True)
    gravimetria_residuo_metais = FloatType(required=True)
    gravimetria_residuo_eletronicos = FloatType(required=True)
    gravimetria_residuo_pilhas = FloatType(required=True)
    prop_residuos_aterrados = FloatType(required=True)
    prop_residuos_reciclados = FloatType(required=True)
    consumo_agua_mes = FloatType(required=True)
    prop_agua_tratada_consumida = FloatType(required=True)
    consumo_combustivel_mes = FloatType(required=True)
    qualidade_ar_trabalho = FloatType(required=True)
    residuos_eletronicos = FloatType(required=True)
    pilhas = FloatType(required=True)
