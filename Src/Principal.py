from Participante import Participante
from Coordenador import Coordenador

def main():
    print("==== SIMULADOR 2PC - Protocolo Two Phase Commit ====\n")

    coordenador_participante = Participante("Coordenador")
    outros_participantes = [Participante("Participante 1"), Participante("Participante 2"), Participante("Participante 3")]

    todos_participantes = [coordenador_participante] + outros_participantes
    coordenador = Coordenador(todos_participantes)


    mensagem = input("Digite a mensagem da transação que deseja realizar: ").strip()

    print("==== INÍCIO DA VOTAÇÃO ====\n")
    print("[Coordenador] Enviando solicitação de preparação para commit aos participantes...\n")

    votos = coordenador.iniciar_votacao()

    print("\n===== RESUMO DOS VOTOS =====")
    for nome, voto in votos.items():
        print(f"{nome} votou: {voto.upper()}")

    print("\n[Fim da Fase de Votação] Iniciando Fase de Decisão...")
    resultado = coordenador.decidir_transacao(votos, mensagem)
    print(f"\nResultado da transação: {resultado}")

if __name__ == "__main__":
    main()
