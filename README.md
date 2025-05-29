# Detecção Automática de Pessoas em Vídeos Noturnos

## 👥 Integrantes

- Laura Claro Mathias – RM98747
- Guilherme Silva Dos Santos – RM551168
  
## 🎯 Descrição do Problema
Encontrar pessoas em ambientes escuros é um grande desafio para equipes de busca e monitoramento. Em períodos noturnos, a falta de visibilidade dificulta a identificação rápida, aumentando o risco de pessoas serem deixadas para trás e não receberem socorro em tempo hábil.

## 💡 Visão Geral da Solução
Desenvolvemos um sistema em Python capaz de processar vídeos noturnos, identificar automaticamente pessoas usando IA (MediaPipe Pose) e destacar cada pessoa encontrada com um quadro verde ao redor do corpo.

- Não precisa de hardware especial: apenas Python, OpenCV e MediaPipe.
- Aplicação para drones, câmeras de segurança 

## Como Funciona

1. O usuário executa o script com um vídeo noturno (ex: `luneta.mp4`).
2. O sistema processa cada frame do vídeo.
3. Ao detectar uma pessoa, desenha um quadro verde ao redor dela e mostra a mensagem "Pessoa detectada".

## 📽️ Demonstração

> [**Assista ao vídeo explicativo**](LINK)

## 📷 Exemplo de Funcionamento

[Exemplo](exemplo1.png)

### Pré-requisitos

- Python 3.8+
- OpenCV (`pip install opencv-python`)
- MediaPipe (`pip install mediapipe`)
- NumPy (`pip install numpy`)

1. Clone este repositório.
2. Adicione seu vídeo noturno à pasta do projeto (ex: `luneta.mp4`).
3. Execute o comando:

    ```bash
    python  detectar-pessoas.py
    ```
4. Aperte `q` para fechar a janela ao final.

## ⚙️ Código Fonte



   
