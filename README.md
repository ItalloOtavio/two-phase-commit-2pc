# Two Phase Commit (2PC)

## 📌 Tecnologias Utilizadas

- Python 3.12+
- Socket (comunicação local)
- Threads
- Leitura/Escrita em arquivos `.txt`

## ⚙️ Funcionalidades

- Simulação de transações distribuídas com o protocolo 2PC (Two Phase Commit)
- Escrita consistente em múltiplos arquivos locais
- Votação e decisão baseadas no consenso entre participantes
- Registro de logs de transações
- Escolha dinâmica da mensagem a ser escrita

## 🏗 Arquitetura do Sistema

O sistema é composto por:

- **Coordenador**: responsável por iniciar a transação e coordenar a votação e decisão.
- **Participantes**: recebem a solicitação e votam "sim" ou "não" para a transação.
- **Logs**: cada ação é registrada para rastreabilidade.
- **Arquivos locais**: cada participante escreve em um arquivo separado.

Todos os participantes estão simulados localmente via diferentes portas (ex: 5001, 5002, 5003).

## ▶️ Como Executar

### 1. Pré-requisitos

- Python 3 instalado
- Terminal ou console

### 2. Passos para Executar

1. **Abra 3 terminais** para iniciar os participantes:
   ```bash
   python Src/Participante.py Participante1 5001
   python Src/Participante.py Participante2 5002
   python Src/Participante.py Participante3 5003
2. Em outro terminal, execute o coordenador:
   ```bash   
   python Src/Principal.py
3. Digite a mensagem da transação quando solicitado.
4. Verifique os arquivos dos participantes e os logs.

📄 Licença

Este código foi desenvolvido para fins acadêmicos.
