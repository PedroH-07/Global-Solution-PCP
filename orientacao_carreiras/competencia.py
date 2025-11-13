# Classe Competencia = uma competência técnica ou comportamental.

class Competencia:
    """
    Atributos:
        nome (str): Nome da competência
        categoria (str): 'tecnica' ou 'comportamental'
        descricao (str): Descrição da competência
        nivel_demanda_futuro (int): Nível de demanda previsto (1-5)
    """
    
    # Tupla com categorias 
    CATEGORIAS_VALIDAS = ('tecnica', 'comportamental', 'hibrida')
    
    def __init__(self, nome, categoria, descricao="", nivel_demanda_futuro=3):
        """
        Inicia uma competência.
        
        Args:
            nome (str): Nome da competência
            categoria (str): Categoria da competência
            descricao (str): Descrição opcional
            nivel_demanda_futuro (int): Demanda futura (1-5)
        """
        self.nome = nome
        self.categoria = self._validar_categoria(categoria)
        self.descricao = descricao
        self.nivel_demanda_futuro = self._validar_nivel(nivel_demanda_futuro)
    
    def _validar_categoria(self, categoria):
        """Valida se a categoria é válida."""
        if categoria not in self.CATEGORIAS_VALIDAS:
            raise ValueError(f"Categoria deve ser uma das: {self.CATEGORIAS_VALIDAS}")
        return categoria
    
    def _validar_nivel(self, nivel):
        """Valida se o nível está entre 1 e 5."""
        if not isinstance(nivel, int) or nivel < 1 or nivel > 5:
            raise ValueError("Nível deve ser um inteiro entre 1 e 5")
        return nivel
    
    def eh_tecnica(self):
        """Verifica se é uma competência técnica."""
        return self.categoria == 'tecnica'
    
    def eh_comportamental(self):
        """Verifica se é uma competência comportamental."""
        return self.categoria == 'comportamental'
    
    def eh_alta_demanda(self):
        """Verifica se tem alta demanda no futuro."""
        return self.nivel_demanda_futuro >= 4
    
    def __str__(self):
        return f"{self.nome} ({self.categoria})"
    
    def __repr__(self):
        return f"Competencia(nome='{self.nome}', categoria='{self.categoria}')"
    
    def to_dict(self):
        """Converte a competência para dicionário."""
        return {
            'nome': self.nome,
            'categoria': self.categoria,
            'descricao': self.descricao,
            'nivel_demanda_futuro': self.nivel_demanda_futuro
        }