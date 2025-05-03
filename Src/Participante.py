class Participante:
    def __init__(self, nome):
        self.nome = nome

    def votar(self):
        while True:
            voto = input(f"[{self.nome}] Você está pronto para COMMITAR? (sim/nao): ").strip().lower()
            if voto in ["sim", "nao"]:
                print(f"[{self.nome}] Enviou voto: {voto.upper()}")
                return voto
            else:
                print("Resposta inválida. Digite apenas 'sim' ou 'nao'.")
