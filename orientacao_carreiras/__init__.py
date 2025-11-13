"""
Sistema de Orientação de Carreiras
Análise de perfis profissionais e recomendações para o futuro do trabalho.
"""

from .perfil import Perfil
from .competencia import Competencia
from .carreira import Carreira
from .sistema_recomendacao import SistemaRecomendacao
from .dados_mock import obter_competencias_base, obter_carreiras_futuro
from .cli import CLI
from .validadores import validar_idade, validar_nivel, validar_nome

__all__ = [
    'Perfil',
    'Competencia', 
    'Carreira',
    'SistemaRecomendacao',
    'obter_competencias_base',
    'obter_carreiras_futuro',
    'CLI',
    'validar_idade',
    'validar_nivel',
    'validar_nome'
]