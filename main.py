
from orientacao_carreiras import CLI

def main():
    # Função principal que inicia o sistema.

    try:
        # Cria e executa a interface CLI
        interface = CLI()
        interface.executar()
        
    except KeyboardInterrupt:
        print("\n\nSistema encerrado pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        print("Por favor, reinicie o sistema.")

if __name__ == "__main__":
    main()
    