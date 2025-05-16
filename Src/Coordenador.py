class Coordenador:
    def __init__(self, participantes):
        self.participantes = participantes

    def iniciar_votacao(self):
        votos = {}
        for participante in self.participantes:
            voto = participante.votar()
            votos[participante.nome] = voto
        return votos

    def decidir_transacao(self, votos, mensagem):
        if all(voto == 'sim' for voto in votos.values()):
            for participante in self.participantes:
                participante.escrever_em_arquivo(mensagem)
            return "COMMIT - Todos os arquivos foram atualizados com a transação."
        else:
            return "ABORT - Pelo menos um voto foi 'nao', nenhum arquivo foi alterado."
