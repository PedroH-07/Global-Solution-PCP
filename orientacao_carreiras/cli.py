# Interface de linha de comando (CLI) para o Sistema de Orientação de Carreiras.

import os
from .perfil import Perfil
from .sistema_recomendacao import SistemaRecomendacao
from .dados_mock import obter_carreiras_futuro, obter_competencias_base
from .validadores import validar_nome, validar_idade, validar_nivel

class CLI:
    # Interface de linha de comando para interação com o usuário.
    
    def __init__(self):
        # Inicia a interface CLI.
        self.sistema = SistemaRecomendacao(obter_carreiras_futuro())
        self.competencias_disponiveis = obter_competencias_base()
        self.perfil_atual = None
    
    def limpar_tela(self):
        # Limpa a tela do terminal.
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_cabecalho(self):
        # Exibe o cabeçalho do sistema.
        print("=" * 60)
        print("    SISTEMA DE ORIENTACAO DE CARREIRAS")
        print("    Prepare-se para o Futuro do Trabalho!")
        print("=" * 60)
        print()
    
    def mostrar_menu_principal(self):
        # Exibe o menu principal.
        print("\nMENU PRINCIPAL")
        print("-" * 30)
        print("1. Criar Novo Perfil")
        print("2. Ver Perfil Atual")
        print("3. Adicionar Competencias")
        print("4. Obter Recomendacoes")
        print("5. Ver Competencias Disponiveis")
        print("0. Sair")
        print("-" * 30)
    
    def obter_opcao_menu(self):
        # Obtém opção do usuário no menu.
        try:
            opcao = int(input("Escolha uma opcao: "))
            return opcao
        except ValueError:
            print("ERRO: Por favor, digite apenas numeros!")
            return -1
    
    def criar_perfil(self):
        # Cria um novo perfil do usuário.
        print("\nCRIAR NOVO PERFIL")
        print("-" * 25)
        
        # Solicita nome
        while True:
            nome = input("Digite seu nome: ").strip()
            valido, mensagem = validar_nome(nome)
            if valido:
                break
            print(f"ERRO: {mensagem}")
        
        # Solicita idade
        while True:
            try:
                idade = int(input("Digite sua idade: "))
                valido, mensagem = validar_idade(idade)
                if valido:
                    break
                print(f"ERRO: {mensagem}")
            except ValueError:
                print("ERRO: Digite apenas numeros para a idade!")
        
        # Solicita área de atuação
        area = input("Area atual de atuacao (opcional): ").strip()
        
        # Cria o perfil
        self.perfil_atual = Perfil(nome, idade, area)
        
        print(f"\nSUCESSO: Perfil criado com sucesso!")
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        if area:
            print(f"Area: {area}")
    
    def mostrar_perfil(self):
        # Exibe informações do perfil atual.
        if not self.perfil_atual:
            print("\nERRO: Nenhum perfil criado ainda!")
            return
        
        print(f"\nPERFIL: {self.perfil_atual.nome}")
        print("-" * 30)
        print(f"Idade: {self.perfil_atual.idade} anos")
        if self.perfil_atual.area_atuacao:
            print(f"Area: {self.perfil_atual.area_atuacao}")
        
        print(f"\nCOMPETENCIAS ({len(self.perfil_atual.competencias)}):")
        if self.perfil_atual.competencias:
            for comp, nivel in self.perfil_atual.competencias.items():
                print(f"  - {comp}: Nivel {nivel}")
        else:
            print("  Nenhuma competencia cadastrada ainda.")
        
        # Mostra preparação para o futuro
        percentual, classificacao = self.perfil_atual.nivel_preparacao_futuro()
        print(f"\nPREPARACAO FUTURO: {percentual:.1f}% - {classificacao}")
    
    def adicionar_competencias(self):
        # Permite adicionar competências ao perfil.
        if not self.perfil_atual:
            print("\nERRO: Crie um perfil primeiro!")
            return
        
        print(f"\nADICIONAR COMPETENCIAS")
        print("-" * 30)
        
        while True:
            print("\nCompetencias disponiveis:")
            competencias_lista = list(self.competencias_disponiveis.keys())
            
            for i, comp in enumerate(competencias_lista, 1):
                categoria = self.competencias_disponiveis[comp].categoria
                print(f"{i:2}. {comp} ({categoria})")
            
            try:
                escolha = int(input("\nEscolha uma competencia (numero) ou 0 para voltar: "))
                
                if escolha == 0:
                    break
                
                if 1 <= escolha <= len(competencias_lista):
                    competencia = competencias_lista[escolha - 1]
                    
                    # Solicita nível
                    while True:
                        try:
                            print(f"\nNiveis: 1-Iniciante, 2-Basico, 3-Intermediario, 4-Avancado, 5-Expert")
                            nivel = int(input(f"Seu nivel em {competencia} (1-5): "))
                            valido, mensagem = validar_nivel(nivel)
                            
                            if valido:
                                self.perfil_atual.adicionar_competencia(competencia, nivel)
                                print(f"SUCESSO: Competencia '{competencia}' adicionada com nivel {nivel}!")
                                break
                            else:
                                print(f"ERRO: {mensagem}")
                        except ValueError:
                            print("ERRO: Digite apenas numeros de 1 a 5!")
                else:
                    print("ERRO: Opcao invalida!")
                    
            except ValueError:
                print("ERRO: Digite apenas numeros!")
    
    def mostrar_competencias_disponiveis(self):
        # Mostra todas as competências disponíveis no sistema.
        print(f"\nCOMPETENCIAS DISPONIVEIS")
        print("-" * 35)
        
        # Organiza por categoria
        por_categoria = {}
        for nome, competencia in self.competencias_disponiveis.items():
            categoria = competencia.categoria
            if categoria not in por_categoria:
                por_categoria[categoria] = []
            por_categoria[categoria].append(competencia)
        
        # Exibe por categoria
        for categoria, competencias in por_categoria.items():
            print(f"\n{categoria.upper()}:")
            for comp in competencias:
                print(f"  - {comp.nome}: {comp.descricao}")
    
    def obter_recomendacoes(self):
        # Gera e exibe recomendações de carreiras.
        if not self.perfil_atual:
            print("\nERRO: Crie um perfil primeiro!")
            return
        
        if not self.perfil_atual.competencias:
            print("\nERRO: Adicione algumas competencias primeiro!")
            return
        
        print(f"\nRECOMENDACOES PARA {self.perfil_atual.nome}")
        print("-" * 40)
        
        # Gera recomendações
        recomendacoes = self.sistema.recomendar_carreiras(self.perfil_atual)
        
        if not recomendacoes:
            print("ERRO: Nenhuma carreira encontrada!")
            return
        
        print("TOP 3 CARREIRAS RECOMENDADAS:")
        for i, (carreira, compatibilidade) in enumerate(recomendacoes, 1):
            print(f"\n{i}. {carreira.nome}")
            print(f"   Compatibilidade: {compatibilidade}%")
            print(f"   Crescimento: {carreira.crescimento_projetado}%")
            print(f"   Salario medio: R$ {carreira.salario_medio:,.2f}")
            print(f"   Descricao: {carreira.descricao}")
        
        # Mostra gaps da melhor recomendação
        melhor_carreira = recomendacoes[0][0]
        gaps = self.sistema.identificar_gaps(self.perfil_atual, melhor_carreira)
        
        if gaps:
            print(f"\nCOMPETENCIAS PARA DESENVOLVER ({melhor_carreira.nome}):")
            for gap in gaps:
                print(f"  - {gap}")
        else:
            print(f"\nSUCESSO: Voce ja possui as competencias principais para {melhor_carreira.nome}!")
    
    def executar(self):
        # Executa o loop principal da interface.
        self.limpar_tela()
        self.mostrar_cabecalho()
        
        print("Bem-vindo! Este sistema ajuda voce a descobrir carreiras do futuro.")
        input("Pressione ENTER para continuar...")
        
        while True:
            self.limpar_tela()
            self.mostrar_cabecalho()
            self.mostrar_menu_principal()
            
            opcao = self.obter_opcao_menu()
            
            if opcao == 1:
                self.criar_perfil()
            elif opcao == 2:
                self.mostrar_perfil()
            elif opcao == 3:
                self.adicionar_competencias()
            elif opcao == 4:
                self.obter_recomendacoes()
            elif opcao == 5:
                self.mostrar_competencias_disponiveis()
            elif opcao == 0:
                print("\nObrigado por usar o Sistema de Orientacao de Carreiras!")
                print("Prepare-se para o futuro!")
                break
            else:
                print("\nERRO: Opcao invalida! Tente novamente.")
            
            if opcao != 0:
                input("\nPressione ENTER para continuar...")