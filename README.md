# Global-Solution-PCP
- Pedro Henrique dos Santos Cardoso,RM563268
- Rafael do Nascimento Silva,RM566263

# Sistema de Orientação de Carreiras

Sistema desenvolvido em Python orientado a objetos para análise de perfis profissionais e recomendações de carreiras do futuro.

## Descrição do Projeto

O Sistema de Orientação de Carreiras é uma ferramenta inteligente que ajuda profissionais a se prepararem para o mercado de trabalho do futuro. O sistema analisa competências técnicas e comportamentais do usuário e gera recomendações personalizadas de carreiras, trilhas de aprendizado e áreas de desenvolvimento.

### Objetivo

Conectar lógica de programação e automação ao desenvolvimento humano e profissional, criando soluções que preparem pessoas para o trabalho do futuro através de:

- Análise automatizada de perfis profissionais
- Recomendações inteligentes de carreiras
- Identificação de competências em alta demanda
- Sugestões de desenvolvimento pessoal

## Funcionalidades

- **Criação de Perfil**: Cadastro de informações pessoais e profissionais
- **Gestão de Competências**: Adicionar e avaliar competências técnicas e comportamentais
- **Sistema de Recomendação**: Algoritmo que sugere carreiras baseado no perfil
- **Análise de Compatibilidade**: Cálculo de aderência entre perfil e carreiras
- **Identificação de Gaps**: Competências que precisam ser desenvolvidas
- **Interface CLI**: Interface de linha de comando intuitiva

## Estrutura do Projeto

```
sistema_orientacao_carreiras/
├── main.py                          # Arquivo principal para execução
├── README.md                        # Documentação do projeto
├── requirements.txt                 # Dependências (Python puro)
└── orientacao_carreiras/           # Módulo principal
    ├── __init__.py                 # Inicializador do módulo
    ├── perfil.py                   # Classe Perfil
    ├── competencia.py              # Classe Competencia
    ├── carreira.py                 # Classe Carreira
    ├── sistema_recomendacao.py     # Sistema de recomendações
    ├── dados_mock.py               # Dados simulados
    ├── cli.py                      # Interface de linha de comando
    └── validadores.py              # Funções de validação
```

## Como Executar

### Opção 1: Executar via Terminal/Prompt de Comando

#### Windows:
```cmd
# 1. Abrir Prompt de Comando (Windows + R, digite "cmd")
# 2. Navegar até a pasta do projeto
cd caminho\para\Global-Solution-PCP

# 3. Executar o programa
python main.py
```

#### Mac/Linux:
```bash
# 1. Abrir Terminal
# 2. Navegar até a pasta do projeto
cd caminho/para/Global-Solution-PCP

# 3. Executar o programa
python3 main.py
```

### Opção 2: Executar via Interface Gráfica das IDEs

#### PyCharm:
1. **Abrir projeto**: File → Open → Selecionar pasta `Global-Solution-PCP`
2. **Executar**: Clicar com botão direito no arquivo `main.py` → Run 'main'
3. **Ou usar atalho**: Ctrl + Shift + F10 (Windows/Linux) ou Cmd + Shift + R (Mac)

#### Visual Studio Code:
1. **Abrir projeto**: File → Open Folder → Selecionar pasta `Global-Solution-PCP`
2. **Selecionar arquivo a ser executado**: `main.py`
3. **Executar**: Clicar no botão de play no canto superior direito do editor
4. **Ou usar atalho**: Ctrl + F5 (executar sem debug) ou F5 (executar com debug)
5. **Ou via terminal integrado**: Ctrl + ` → `python main.py`


### Solução de Problemas Comuns

#### "No module named 'orientacao_carreiras'":
- Certifique-se de estar executando da pasta raiz do projeto
- Verifique se a pasta `orientacao_carreiras` existe
- Confirme que o arquivo `__init__.py` está presente

#### 1. **Perfil**
Representa o perfil profissional do usuário.
- **Atributos**: nome, idade, área de atuação, competências, objetivos
- **Métodos**: adicionar competências, calcular pontuações, análise de preparação

#### 2. **Competencia** 
Representa uma competência técnica ou comportamental.
- **Atributos**: nome, categoria, descrição, demanda futura
- **Métodos**: validações, verificações de categoria e demanda

#### 3. **Carreira**
Representa uma carreira profissional do futuro.
- **Atributos**: nome, descrição, requisitos, crescimento projetado, salário
- **Métodos**: gestão de competências necessárias, cálculo de atratividade

#### 4. **SistemaRecomendacao**
Engine principal que processa recomendações.
- **Métodos**: calcular compatibilidade, identificar gaps, gerar recomendações

### Estruturas de Dados Utilizadas

- **Listas**: Armazenamento de competências por categoria, objetivos profissionais
- **Tuplas**: Categorias válidas, níveis de competência (dados imutáveis)
- **Dicionários**: Mapeamento competência-nível, requisitos de carreiras

## Competências Disponíveis

### Técnicas
- **Programação**: Desenvolvimento de software
- **Análise de Dados**: Análise e interpretação de dados
- **Design**: Design gráfico e UX

### Comportamentais
- **Criatividade**: Pensamento criativo e inovador
- **Liderança**: Capacidade de liderar equipes
- **Comunicação**: Comunicação eficaz

### Híbridas
- **Adaptabilidade**: Flexibilidade para mudanças
- **Inovação**: Capacidade de inovar processos

## Carreiras do Futuro

O sistema inclui carreiras em alta demanda:

1. **Desenvolvedor de Software** (200% crescimento)
2. **Designer Digital** (150% crescimento)  
3. **Gerente de Projetos** (120% crescimento)
4. **Consultor de Inovação** (180% crescimento)

## Algoritmo de Recomendação

O sistema utiliza um algoritmo baseado em pontuação ponderada:

```python
# Pesos por categoria de competência
essenciais: peso 5
importantes: peso 3  
desejaveis: peso 1

# Cálculo de compatibilidade
compatibilidade = (pontos_usuario / pontos_maximos) * 100
```

### Critérios de Avaliação
- **Competências Essenciais**: Peso máximo na avaliação
- **Competências Importantes**: Peso médio 
- **Competências Desejáveis**: Peso mínimo
- **Crescimento da Carreira**: Fator de ordenação
- **Facilidade de Desenvolvimento**: Análise de gaps

## Conceitos Demonstrados

### Orientação a Objetos
- **Encapsulamento**: Atributos e métodos organizados
- **Abstração**: Classes representam conceitos do mundo real
- **Modularização**: Código organizado em módulos específicos

### Estruturas de Dados
- **Listas**: Competências por categoria, recomendações
- **Tuplas**: Dados imutáveis (categorias, níveis válidos)
- **Dicionários**: Mapeamentos eficientes (competência-nível)

### Algoritmos
- **Busca e Ordenação**: Recomendações ordenadas por score
- **Cálculos Matemáticos**: Percentuais de compatibilidade
- **Processamento de Dados**: Análise automatizada de perfis

### Demonstração de uso

## Tela Principal
![Tela Inicial do Sistema](https://github.com/PedroH-07/Global-Solution-PCP/blob/main/screenshots/tela_inicial.png?raw=true)

## Menu de Opções
![Menu Principal](https://github.com/PedroH-07/Global-Solution-PCP/blob/main/screenshots/menu-principal.png?raw=true)

## Criação de Perfil
![Criando Novo Perfil](https://github.com/PedroH-07/Global-Solution-PCP/blob/main/screenshots/criacao_de_perfil.png?raw=true)

## Competências Disponiveis
![Competências Disponiveis](https://github.com/PedroH-07/Global-Solution-PCP/blob/main/screenshots/competencias_disponiveis.png?raw=true)

## Adição de Competências
![Adicionando Competências](https://github.com/PedroH-07/Global-Solution-PCP/blob/main/screenshots/competencias.png?raw=true)

## Recomendações de Carreiras
![Recomendações Geradas](https://github.com/PedroH-07/Global-Solution-PCP/blob/main/screenshots/recomendacoes.png?raw=true)

**Sistema de Orientação de Carreiras** - Preparando profissionais para o futuro do trabalho!
