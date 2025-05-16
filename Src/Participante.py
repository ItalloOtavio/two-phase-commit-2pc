class Participante:
    def __init__(self, nome):
        self.nome = nome
        self.arquivo = f"participante_{nome}.txt"

    def votar(self):
        while True:
            voto = input(f"{self.nome}, deseja realizar a transação? (sim/nao): ").strip().lower()
            if voto in ['sim', 'nao']:
                return voto
            else:
                print("Entrada inválida. Digite 'sim' ou 'nao'.")

    def escrever_em_arquivo(self, mensagem):
        with open(self.arquivo, 'a') as arquivo: 
            arquivo.write(mensagem + '\n')
