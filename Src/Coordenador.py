import socket
from log import escrever_log

class Coordenador:
    def __init__(self, participantes, mensagem):
        self.participantes = participantes
        self.mensagem = mensagem

    def iniciar_votacao(self):
        votos = {}
        for nome, host, port in self.participantes:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    print(f"[Coordenador] Enviando pedido de voto para {nome} em {host}:{port}")
                    s.sendall(b"prepare")
                    voto = s.recv(1024).decode()
                    print(f"[Coordenador] Recebeu voto '{voto}' de {nome}")
                    votos[nome] = voto
                    escrever_log(f"[Coordenador] Recebeu voto '{voto}' de {nome}")
            except Exception as e:
                print(f"[Coordenador] Falha na comunicação com {nome}: {e}")
                escrever_log(f"[Coordenador] Falha na comunicação com {nome}: {e}")
                votos[nome] = "falha"
        return votos

    def decidir_transacao(self, votos):
        if all(voto == 'sim' for voto in votos.values()):
            print("\n[Coordenador] Todos votaram 'sim'. Enviando COMMIT...")
            escrever_log("[Coordenador] Todos votaram 'sim'. Commit sendo enviado.")
            for nome, host, port in self.participantes:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((host, port))
                        msg_commit = "commit " + self.mensagem
                        s.sendall(msg_commit.encode())
                except Exception as e:
                    print(f"[Coordenador] Falha ao enviar commit para {nome}: {e}")
                    escrever_log(f"[Coordenador] Falha ao enviar commit para {nome}: {e}")
            return "COMMIT - Todos os arquivos foram atualizados com a transação."
        else:
            print("\n[Coordenador] Pelo menos um voto foi 'não' ou houve falha. Enviando ABORT...")
            escrever_log("[Coordenador] Abortando transação devido a voto 'não' ou falha.")
            for nome, host, port in self.participantes:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((host, port))
                        s.sendall(b"abort")
                except Exception as e:
                    print(f"[Coordenador] Falha ao enviar abort para {nome}: {e}")
                    escrever_log(f"[Coordenador] Falha ao enviar abort para {nome}: {e}")
            return "ABORT - Transação cancelada, nenhum arquivo foi alterado."
