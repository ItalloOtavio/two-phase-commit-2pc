import datetime

def escrever_log(mensagem):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log_2pc.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {mensagem}\n")
