# Módulo de validadores e funções auxiliares.

import re
from datetime import datetime

def validar_nome(nome):
    # Valida se o nome é válido.
   
    if not nome or not isinstance(nome, str):
        return False, "Nome não pode ser vazio"
    
    nome = nome.strip()
    
    if len(nome) < 2:
        return False, "Nome deve ter pelo menos 2 caracteres"
    
    if len(nome) > 50:
        return False, "Nome deve ter no máximo 50 caracteres"
    
    # Regex para permitir apenas letras, espaços e acentos
    if not re.match(r'^[a-zA-ZÀ-ÿ\s]+$', nome):
        return False, "Nome deve conter apenas letras e espaços"
    
    return True, "Nome válido"

def validar_idade(idade):
    # Valida se a idade é válida.
    if not isinstance(idade, int):
        return False, "Idade deve ser um número inteiro"
    
    if idade < 14:
        return False, "Idade mínima é 14 anos"
    
    if idade > 100:
        return False, "Idade máxima é 100 anos"
    
    return True, "Idade válida"

def validar_nivel(nivel):
    # Valida se o nível de competência é válido.
    if not isinstance(nivel, int):
        return False, "Nível deve ser um número inteiro"
    
    if nivel < 1 or nivel > 5:
        return False, "Nível deve ser entre 1 e 5"
    
    return True, "Nível válido"

def validar_area_atuacao(area):
    # Valida se a área de atuação é válida.
   
    if not area or not isinstance(area, str):
        return False, "Área de atuação não pode ser vazia"
    
    area = area.strip()
    
    if len(area) < 3:
        return False, "Área deve ter pelo menos 3 caracteres"
    
    if len(area) > 100:
        return False, "Área deve ter no máximo 100 caracteres"
    
    return True, "Área válida"

def normalizar_nome_competencia(nome):
    # Normaliza nome de competência (minúsculo, sem espaços extras).
   
    if not nome:
        return ""
    
    return nome.strip().lower().replace(' ', '_')

def formatar_nivel_texto(nivel):
    # Converte nível numérico para texto descritivo.
    niveis_texto = {
        1: "Iniciante",
        2: "Básico",
        3: "Intermediário", 
        4: "Avançado",
        5: "Expert"
    }
    
    return niveis_texto.get(nivel, "Não definido")

def calcular_percentual_compatibilidade(score_atual, score_maximo):
    # Calcula percentual de compatibilidade.
    if score_maximo == 0:
        return 0
    
    percentual = (score_atual / score_maximo) * 100
    return round(percentual, 1)

def obter_timestamp():
    # Obtém timestamp atual formatado.
    
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def formatar_salario(valor):
    # Formata valor de salário para exibição.
   
    if valor <= 0:
        return "Não informado"
    
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def obter_cores_nivel():
    # Retorna dicionário com cores para cada nível (para futuras implementações).

    return {
        1: "🔴",  # Vermelho - Iniciante
        2: "🟠",  # Laranja - Básico
        3: "🟡",  # Amarelo - Intermediário
        4: "🟢",  # Verde - Avançado
        5: "🔵"   # Azul - Expert
    }

def gerar_codigo_perfil(nome):
    # Gera código único para o perfil.
    
    nome_limpo = re.sub(r'[^a-zA-Z]', '', nome)[:3].upper()
    timestamp = datetime.now().strftime("%m%d%H%M")
    return f"{nome_limpo}{timestamp}"

# Constantes úteis (tuplas e listas)
COMPETENCIAS_FUTURO = (
    'programacao', 'analise_dados', 'adaptabilidade', 'criatividade',
    'colaboracao_virtual', 'lideranca', 'pensamento_critico',
    'inteligencia_emocional', 'sustentabilidade'
)

AREAS_ATUACAO_COMUNS = [
    'Tecnologia da Informação',
    'Engenharia',
    'Administração',
    'Marketing',
    'Design',
    'Educação',
    'Saúde',
    'Finanças',
    'Recursos Humanos',
    'Consultoria',
    'Vendas',
    'Jurídico',
    'Outro'
]

OBJETIVOS_PROFISSIONAIS_SUGERIDOS = [
    'Mudar de carreira',
    'Promoção na empresa atual',
    'Aumentar salário',
    'Trabalhar remotamente',
    'Empreender',
    'Especializar-se em tecnologia',
    'Desenvolver liderança',
    'Trabalhar no exterior',
    'Melhorar work-life balance',
    'Impactar positivamente a sociedade'
]