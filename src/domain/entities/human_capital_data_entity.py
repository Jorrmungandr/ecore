from schematics.types import IntType, FloatType, DateTimeType

from src.domain.entities.base_entity import BaseEntity

class HumanCapitalDataEntity(BaseEntity):
    id = IntType(required=True)
    month = DateTimeType('%m/%Y', required=True)
    colaboradores_lgbtqia = IntType(required=True)
    colaboradores_negros = IntType(required=True)
    colaboradoras_mulheres = IntType(required=True)
    idade_media_colaboradores = IntType(required=True)
    colaboradores_pcd = IntType(required=True)
    colaboradores_minorizados = IntType(required=True)
    mulheres_lideranca_tecnica = IntType(required=True)
    mulheres_media_lideranca = IntType(required=True)
    mulheres_alta_lideranca = IntType(required=True)
    pessoas_negras_lideranca_tecnica = IntType(required=True)
    pessoas_negras_media_lideranca = IntType(required=True)
    pessoas_negras_alta_lideranca = IntType(required=True)
    total_colaboradores = IntType(required=True)
    total_estagiarios = IntType(required=True)
    pcds = IntType(required=True)
    pessoas_pardas = IntType(required=True)
    pessoas_pretas = IntType(required=True)
    mulheres = IntType(required=True)
    cinquenta_mais = IntType(required=True)
    e_nps = FloatType(required=True)
    turnover_ate_julho_2022 = FloatType(required=True)
    indice_recrutamento_interno = FloatType(required=True)
    vagas_recrutamento_interno = FloatType(required=True)
    detalhes_organizacionais = FloatType(required=True)
    periodo_frequencia_relatorio = FloatType(required=True)
