import socket
from log import escrever_log

class Participante:
    def __init__(self, nome, host, port):
        self.nome = nome
        self.host = host
        self.port = port
        self.arquivo = f"participante_{nome}.txt"

    def votar(self):
        while True:
            simular_falha = input(f"[{self.nome}] Deseja simular falha antes de votar? (sim/nao): ").strip().lower()
            if simular_falha == 'sim':
                msg = f"{self.nome} falhou antes de votar!"
                print(f"[{self.nome}] Falhou antes de votar!")
                escrever_log(msg)
                return None

            voto = input(f"{self.nome}, deseja realizar a transação? (sim/nao): ").strip().lower()
            if voto in ['sim', 'nao']:
                escrever_log(f"{self.nome} votou: {voto}")
                return voto
            else:
                print("Entrada inválida. Digite 'sim' ou 'nao'.")

    def escrever_em_arquivo(self, mensagem):
        with open(self.arquivo, 'a') as arquivo:
            arquivo.write(mensagem + '\n')
        escrever_log(f"{self.nome} escreveu no arquivo: {mensagem}")

    def iniciar_servidor(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.bind((self.host, self.port))
            servidor.listen()
            print(f"[{self.nome}] Servidor iniciado em {self.host}:{self.port}. Aguardando coordenador...")

            while True:
                conn, addr = servidor.accept()
                with conn:
                    print(f"[{self.nome}] Conexão recebida de {addr}")
                    data = conn.recv(1024).decode()

                    if data == "prepare":
                        voto = self.votar()
                        if voto is None:
                            print(f"[{self.nome}] Não enviou voto por falha simulada.")
                            continue
                        else:
                            conn.sendall(voto.encode())

                    elif data.startswith("commit"):
                        mensagem = data[6:].strip() 
                        print(f"[{self.nome}] Commit recebido. Atualizando arquivo...")
                        self.escrever_em_arquivo(mensagem)
                        print(f"[{self.nome}] Commit finalizado.")
                    elif data == "abort":
                        print(f"[{self.nome}] Abort recebido. Transação cancelada.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uso: python participante.py <nome> <host> <porta>")
        sys.exit(1)

    nome = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])

    p = Participante(nome, host, port)
    p.iniciar_servidor()
