from Coordenador import Coordenador
from log import escrever_log

def main():
    print("==== SIMULADOR 2PC DISTRIBUÍDO ====\n")

    participantes = [
        ("Participante1", "localhost", 5001),
        ("Participante2", "localhost", 5002),
        ("Participante3", "localhost", 5003),
    ]

    mensagem = input("Digite a mensagem da transação que deseja realizar: ").strip()

    coordenador = Coordenador(participantes, mensagem)

    print("==== INÍCIO DA VOTAÇÃO ====\n")
    escrever_log(f"[Coordenador] Iniciando votação para a transação: {mensagem}")

    votos = coordenador.iniciar_votacao()

    print("\n===== RESUMO DOS VOTOS =====")
    for nome, voto in votos.items():
        print(f"{nome} votou: {voto.upper()}")

    print("\n[Fim da Fase de Votação] Iniciando Fase de Decisão...")
    resultado = coordenador.decidir_transacao(votos)
    print(f"\nResultado da transação: {resultado}")
    escrever_log(f"Resultado da transação: {resultado}")

if __name__ == "__main__":
    main()
