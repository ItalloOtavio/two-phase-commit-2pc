class Coordenador:
    def __init__(self, participantes):
        self.participantes = participantes

    def iniciar_votacao(self):
        print("\n[Coordenador] Enviando solicitação de preparação para COMMIT...\n")
        votos = {}

        for participante in self.participantes:
            voto = participante.votar()
            votos[participante.nome] = voto

        print("\n[Coordenador] Todos os votos foram recebidos.")
        return votos
