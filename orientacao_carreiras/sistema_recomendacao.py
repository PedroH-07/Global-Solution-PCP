# Sistema de Recomendação de Carreiras

class SistemaRecomendacao:
    # Sistema simples para recomendar carreiras baseado no perfil do usuário.
    
    def __init__(self, carreiras_disponiveis):
        """
        Inicia o sistema de recomendação.
        
        Args:
            carreiras_disponiveis (list): Lista de objetos Carreira
        """
        self.carreiras = carreiras_disponiveis
    
    def calcular_compatibilidade(self, perfil_usuario, carreira):
        """
        Calcula compatibilidade entre perfil e carreira.
        
        Args:
            perfil_usuario (Perfil): Perfil do usuário
            carreira (Carreira): Carreira a ser analisada
            
        Returns:
            float: Percentual de compatibilidade (0-100)
        """
        pontos_usuario = 0
        pontos_maximos = 0
        
        # Verifica competências essenciais (peso 3)
        for competencia in carreira.requisitos['essenciais']:
            nivel_usuario = perfil_usuario.obter_nivel_competencia(competencia)
            pontos_usuario += nivel_usuario * 3
            pontos_maximos += 5 * 3  # Nível máximo * peso
        
        # Verifica competências importantes (peso 2)
        for competencia in carreira.requisitos['importantes']:
            nivel_usuario = perfil_usuario.obter_nivel_competencia(competencia)
            pontos_usuario += nivel_usuario * 2
            pontos_maximos += 5 * 2
        
        # Verifica competências desejáveis (peso 1)
        for competencia in carreira.requisitos['desejaveis']:
            nivel_usuario = perfil_usuario.obter_nivel_competencia(competencia)
            pontos_usuario += nivel_usuario * 1
            pontos_maximos += 5 * 1
        
        # Calcula percentual
        if pontos_maximos == 0:
            return 0
        
        compatibilidade = (pontos_usuario / pontos_maximos) * 100
        return round(compatibilidade, 1)
    
    def recomendar_carreiras(self, perfil_usuario, limite=3):
        """
        Gera lista simples de recomendações.
        
        Args:
            perfil_usuario (Perfil): Perfil do usuário
            limite (int): Número de recomendações
            
        Returns:
            list: Lista de tuplas (carreira, compatibilidade)
        """
        recomendacoes = []
        
        # Calcula compatibilidade para cada carreira
        for carreira in self.carreiras:
            compatibilidade = self.calcular_compatibilidade(perfil_usuario, carreira)
            recomendacoes.append((carreira, compatibilidade))
        
        # Ordena por compatibilidade (maior para menor)
        recomendacoes.sort(key=lambda x: x[1], reverse=True)
        
        # Retorna apenas o limite solicitado
        return recomendacoes[:limite]
    
    def identificar_gaps(self, perfil_usuario, carreira):
        """
        Identifica competências que o usuário precisa desenvolver.
        
        Args:
            perfil_usuario (Perfil): Perfil do usuário
            carreira (Carreira): Carreira analisada
            
        Returns:
            list: Lista de competências a desenvolver
        """
        gaps = []
        
        # Verifica todas as competências da carreira
        todas_competencias = carreira.obter_todas_competencias()
        
        for competencia in todas_competencias:
            nivel_atual = perfil_usuario.obter_nivel_competencia(competencia)
            
            # Se não tem a competência ou está abaixo do ideal
            if nivel_atual < 3:  # Considera 3 como nível mínimo adequado
                gaps.append(competencia)
        
        return gaps
    
    def gerar_relatorio_simples(self, perfil_usuario):
        """
        Gera relatório simples de recomendações.
        
        Args:
            perfil_usuario (Perfil): Perfil do usuário
            
        Returns:
            dict: Relatório com recomendações e análises
        """
        recomendacoes = self.recomendar_carreiras(perfil_usuario)
        
        # Pega a melhor recomendação para análise de gaps
        if recomendacoes:
            melhor_carreira = recomendacoes[0][0]
            gaps = self.identificar_gaps(perfil_usuario, melhor_carreira)
        else:
            melhor_carreira = None
            gaps = []
        
        relatorio = {
            'perfil': perfil_usuario.nome,
            'total_competencias': len(perfil_usuario.competencias),
            'recomendacoes': recomendacoes,
            'areas_desenvolver': gaps,
            'preparacao_futuro': perfil_usuario.nivel_preparacao_futuro()
        }
        
        return relatorio