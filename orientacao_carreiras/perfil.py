# Classe Perfil = o perfil profissional de um usuário.

from datetime import datetime

class Perfil:
    """
    Representa o perfil profissional de um usuário.
    
    Atributos:
        nome (str): Nome do usuário
        idade (int): Idade do usuário
        area_atuacao (str): Área atual de atuação
        competencias (dict): Dicionário com competências e seus níveis
        objetivos (list): Lista de objetivos profissionais
        data_criacao (datetime): Data de criação do perfil
    """
    
    # Tupla com níveis válidos
    NIVEIS_VALIDOS = (1, 2, 3, 4, 5)
    
    def __init__(self, nome, idade=0, area_atuacao=""):
        """
        Inicializa um perfil.
        
        Args:
            nome (str): Nome do usuário
            idade (int): Idade do usuário
            area_atuacao (str): Área atual de atuação
        """
        self.nome = nome
        self.idade = idade
        self.area_atuacao = area_atuacao
        self.competencias = {}  # Dicionário: {nome_competencia: nivel}
        self.objetivos = []     # Lista de objetivos
        self.data_criacao = datetime.now()
    
    def adicionar_competencia(self, nome_competencia, nivel):
        """
        Adiciona ou atualiza uma competência no perfil.
        
        Args:
            nome_competencia (str): Nome da competência
            nivel (int): Nível da competência (1-5)
        """
        if nivel not in self.NIVEIS_VALIDOS:
            raise ValueError(f"Nível deve ser um dos: {self.NIVEIS_VALIDOS}")
        
        self.competencias[nome_competencia] = nivel
    
    def remover_competencia(self, nome_competencia):
        """Remove uma competência do perfil."""
        if nome_competencia in self.competencias:
            del self.competencias[nome_competencia]
    
    def obter_nivel_competencia(self, nome_competencia):
        """
        Obtém o nível de uma competência.
        
        Args:
            nome_competencia (str): Nome da competência
            
        Returns:
            int: Nível da competência (0 se não possuir)
        """
        return self.competencias.get(nome_competencia, 0)
    
    def adicionar_objetivo(self, objetivo):
        """Adiciona um objetivo profissional."""
        if objetivo not in self.objetivos:
            self.objetivos.append(objetivo)
    
    def obter_competencias_nivel(self, nivel_minimo):
        """
        Retorna competências com nível igual ou superior ao mínimo.
        
        Args:
            nivel_minimo (int): Nível mínimo desejado
            
        Returns:
            dict: Dicionário com competências filtradas
        """
        return {comp: nivel for comp, nivel in self.competencias.items() 
                if nivel >= nivel_minimo}
    
    def obter_pontos_fortes(self):
        """Retorna competências com nível 4 ou 5."""
        return self.obter_competencias_nivel(4)
    
    def obter_areas_desenvolvimento(self):
        """Retorna competências com nível 1, 2 ou 3."""
        return {comp: nivel for comp, nivel in self.competencias.items() 
                if nivel <= 3}
    
    def calcular_score_total(self):
        """Calcula score total somando todos os níveis."""
        return sum(self.competencias.values())
    
    def calcular_media_competencias(self):
        """Calcula média dos níveis das competências."""
        if not self.competencias:
            return 0
        return sum(self.competencias.values()) / len(self.competencias)
    
    def tem_competencia(self, nome_competencia):
        """Verifica se possui uma competência específica."""
        return nome_competencia in self.competencias
    
    def nivel_preparacao_futuro(self):
        """
        Calcula nível de preparação para o futuro baseado nas competências.
        
        Returns:
            tuple: (percentual, classificacao)
        """
        competencias_futuro = [
            'programacao', 'analise_dados', 'criatividade', 
            'adaptabilidade', 'lideranca', 'comunicacao'
        ]
        
        total_possivel = len(competencias_futuro) * 5
        total_atual = sum(self.obter_nivel_competencia(comp) 
                         for comp in competencias_futuro)
        
        percentual = (total_atual / total_possivel) * 100
        
        if percentual >= 80:
            classificacao = "Muito Preparado"
        elif percentual >= 60:
            classificacao = "Preparado"
        elif percentual >= 40:
            classificacao = "Em Desenvolvimento"
        else:
            classificacao = "Precisa Desenvolver"
        
        return percentual, classificacao
    
    def __str__(self):
        return f"{self.nome} - {len(self.competencias)} competências"
    
    def __repr__(self):
        return f"Perfil(nome='{self.nome}', competencias={len(self.competencias)})"
    
    def to_dict(self):
        """Converte o perfil para dicionário."""
        percentual, classificacao = self.nivel_preparacao_futuro()
        
        return {
            'nome': self.nome,
            'idade': self.idade,
            'area_atuacao': self.area_atuacao,
            'competencias': self.competencias,
            'objetivos': self.objetivos,
            'data_criacao': self.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
            'total_competencias': len(self.competencias),
            'score_total': self.calcular_score_total(),
            'media_competencias': round(self.calcular_media_competencias(), 2),
            'preparacao_futuro': {
                'percentual': round(percentual, 1),
                'classificacao': classificacao
            }
        }