
# Dados simulados para o Sistema de Orientação de Carreiras.

from .competencia import Competencia
from .carreira import Carreira

def obter_competencias_base():
    """
    Retorna dicionário com competências do sistema.
    
    Returns:
        dict: Dicionário {nome_competencia: objeto_Competencia}
    """
    
    competencias = {
        # Técnicas
        'programacao': Competencia("programacao", "tecnica", "Desenvolvimento de software", 5),
        'analise_dados': Competencia("analise_dados", "tecnica", "Análise de dados", 4),
        'design': Competencia("design", "tecnica", "Design gráfico e UX", 3),
        
        # Comportamentais  
        'criatividade': Competencia("criatividade", "comportamental", "Pensamento criativo", 4),
        'lideranca': Competencia("lideranca", "comportamental", "Liderar equipes", 4),
        'comunicacao': Competencia("comunicacao", "comportamental", "Comunicação eficaz", 4),
        
        # Híbridas
        'adaptabilidade': Competencia("adaptabilidade", "hibrida", "Flexibilidade a mudanças", 5),
        'inovacao': Competencia("inovacao", "hibrida", "Capacidade de inovar", 4)
    }
    
    return competencias

def obter_carreiras_futuro():
    """
    Retorna lista com carreiras do futuro.
    
    Returns:
        list: Lista de objetos Carreira
    """
    
    carreiras = []
    
    # Desenvolvedor de Software
    dev_software = Carreira(
        nome="Desenvolvedor de Software",
        descricao="Desenvolvimento de aplicações e sistemas",
        crescimento_projetado=200,
        salario_medio=8000.0
    )
    dev_software.adicionar_competencia_essencial("programacao")
    dev_software.adicionar_competencia_importante("analise_dados")
    dev_software.adicionar_competencia_desejavel("criatividade")
    carreiras.append(dev_software)
    
    # Designer Digital
    designer = Carreira(
        nome="Designer Digital", 
        descricao="Criação de interfaces e experiências digitais",
        crescimento_projetado=150,
        salario_medio=6000.0
    )
    designer.adicionar_competencia_essencial("design")
    designer.adicionar_competencia_essencial("criatividade")
    designer.adicionar_competencia_importante("comunicacao")
    carreiras.append(designer)
    
    # Gerente de Projetos
    gerente = Carreira(
        nome="Gerente de Projetos",
        descricao="Gestão de projetos e equipes",
        crescimento_projetado=120,
        salario_medio=7000.0
    )
    gerente.adicionar_competencia_essencial("lideranca")
    gerente.adicionar_competencia_essencial("comunicacao")
    gerente.adicionar_competencia_importante("adaptabilidade")
    carreiras.append(gerente)
    
    # Consultor de Inovação
    consultor = Carreira(
        nome="Consultor de Inovação",
        descricao="Consultoria em processos inovadores",
        crescimento_projetado=180,
        salario_medio=9000.0
    )
    consultor.adicionar_competencia_essencial("inovacao")
    consultor.adicionar_competencia_essencial("adaptabilidade")
    consultor.adicionar_competencia_importante("lideranca")
    carreiras.append(consultor)
    
    return carreiras

# Tupla com competências em alta
COMPETENCIAS_FUTURO = (
    'programacao', 'adaptabilidade', 'criatividade', 'lideranca'
)

# Lista de áreas em crescimento
AREAS_CRESCIMENTO = [
    'Tecnologia',
    'Design',
    'Gestão',
    'Consultoria'
]