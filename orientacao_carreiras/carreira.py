# Classe Carreira = uma carreira profissional do futuro.

class Carreira:
    """
    Representa uma carreira profissional.
    
    Atributos:
        nome (str): Nome da carreira
        descricao (str): Descrição da carreira
        competencias_essenciais (list): Lista de competências essenciais
        competencias_importantes (list): Lista de competências importantes
        competencias_desejaveis (list): Lista de competências desejáveis
        crescimento_projetado (int): Crescimento esperado em % (2025-2030)
        salario_medio (float): Salário médio estimado
    """
    
    def __init__(self, nome, descricao="", crescimento_projetado=0, salario_medio=0.0):
        """
        Inicializa uma carreira.
        
        Args:
            nome (str): Nome da carreira
            descricao (str): Descrição da carreira
            crescimento_projetado (int): Crescimento esperado em %
            salario_medio (float): Salário médio estimado
        """
        self.nome = nome
        self.descricao = descricao
        self.crescimento_projetado = crescimento_projetado
        self.salario_medio = salario_medio
        
        # Dicionário com listas de competências por nível de importância
        self.requisitos = {
            'essenciais': [],      # Lista de competências essenciais
            'importantes': [],     # Lista de competências importantes  
            'desejaveis': []       # Lista de competências desejáveis
        }
    
    def adicionar_competencia_essencial(self, competencia):
        """Adiciona uma competência essencial."""
        if competencia not in self.requisitos['essenciais']:
            self.requisitos['essenciais'].append(competencia)
    
    def adicionar_competencia_importante(self, competencia):
        """Adiciona uma competência importante."""
        if competencia not in self.requisitos['importantes']:
            self.requisitos['importantes'].append(competencia)
    
    def adicionar_competencia_desejavel(self, competencia):
        """Adiciona uma competência desejável."""
        if competencia not in self.requisitos['desejaveis']:
            self.requisitos['desejaveis'].append(competencia)
    
    def obter_todas_competencias(self):
        """Retorna lista com todas as competências necessárias."""
        todas = []
        todas.extend(self.requisitos['essenciais'])
        todas.extend(self.requisitos['importantes'])
        todas.extend(self.requisitos['desejaveis'])
        return todas
    
    def obter_competencias_por_categoria(self, categoria):
        """
        Retorna competências de uma categoria específica.
        
        Args:
            categoria (str): 'essenciais', 'importantes' ou 'desejaveis'
        
        Returns:
            list: Lista de competências da categoria
        """
        return self.requisitos.get(categoria, [])
    
    def eh_carreira_futuro(self):
        """Verifica se é uma carreira em alta para o futuro."""
        return self.crescimento_projetado >= 150  # 150% ou mais de crescimento
    
    def nivel_atratividade(self):
        """
        Calcula nível de atratividade da carreira.
        
        Returns:
            str: 'Alta', 'Média' ou 'Baixa'
        """
        if self.crescimento_projetado >= 200:
            return 'Alta'
        elif self.crescimento_projetado >= 100:
            return 'Média'
        else:
            return 'Baixa'
    
    def __str__(self):
        return f"{self.nome} (Crescimento: {self.crescimento_projetado}%)"
    
    def __repr__(self):
        return f"Carreira(nome='{self.nome}', crescimento={self.crescimento_projetado}%)"
    
    def to_dict(self):
        """Converte a carreira para dicionário."""
        return {
            'nome': self.nome,
            'descricao': self.descricao,
            'crescimento_projetado': self.crescimento_projetado,
            'salario_medio': self.salario_medio,
            'requisitos': self.requisitos,
            'atratividade': self.nivel_atratividade()
        }