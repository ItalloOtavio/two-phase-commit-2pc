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

### 2. Passos para Executar em localhost

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

### 3. Passos para Executar em infraestrutura física distribuída

1. identificar o IP local de cada máquina participante.
2. Ao iniciar o programa participante em cada máquina, deve-se passar o **IP real** daquela máquina e a **porta** na qual o participante irá escutar as conexões do coordenador:
   ```bash
   python participante.py <nome> <ip_da_maquina> <porta>
3. No arquivo do coordenador **(principal.py)**, altere a lista de participantes para usar os IPs reais das máquinas:
   ```bash
   participantes = [
    ("Participante1", "IP DA MAQUINA 1", 5001),
    ("Participante2", "IP DA MAQUINA 2", 5002),
    ("Participante3", "IP DA MAQUINA 3", 5003),
   ]
4. Execute o coordenador numa das máquinas com:
   ```bash
   python principal.py
5. Garanta que as portas usadas estejam liberadas no firewall das máquinas para permitir a comunicação.
6. A partir daí, o coordenador vai se comunicar com os participantes nos IPs e portas configurados, iniciando a votação e a transação.

📄 Licença

Este código foi desenvolvido para fins acadêmicos.
