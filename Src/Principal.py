from Participante import Participante
from Coordenador import Coordenador

def cadastrar_participantes():
    participantes = []
    quantidade_valida = False

    while not quantidade_valida:
        entrada = input("Quantos participantes deseja cadastrar? ")
        if entrada.isdigit():
            quantidade = int(entrada)
            if quantidade > 0:
                quantidade_valida = True
            else:
                print("Por favor, digite um número maior que zero.")
        else:
            print("Entrada inválida. Digite apenas números inteiros.")

    for i in range(quantidade):
        nome = input(f"Digite o nome do participante {i + 1}: ")
        participantes.append(Participante(nome))

    return participantes

def main():
    print("==== FASE 1 - Votação (Two Phase Commit) ====")
    participantes = cadastrar_participantes()
    coordenador = Coordenador(participantes)
    votos = coordenador.iniciar_votacao()

    print("\n===== RESUMO DOS VOTOS =====")
    for nome, voto in votos.items():
        print(f"{nome} votou: {voto.upper()}")

    print("\n[Fim da Fase de Votação] Iniciando Fase de Decisão...")
    decisao_final = coordenador.decidir_transacao(votos)
    print(f"\nResultado da transação: {decisao_final}")

if __name__ == "__main__":
    main()
