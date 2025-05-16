from Participante import Participante
from Coordenador import Coordenador

def main():
    print("==== SIMULADOR 2PC - Protocolo Two Phase Commit ====\n")

    nomes_participantes = ["Participante 1", "Participante 2", "Participante 3"]
    participantes = [Participante(nome) for nome in nomes_participantes]

    coordenador = Coordenador(participantes)


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
