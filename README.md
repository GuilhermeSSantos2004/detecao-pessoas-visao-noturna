# Detecção Automática de Pessoas em Vídeos Noturnos

## 👥 Integrantes

- Laura Claro Mathias – RM98747
- Guilherme Silva Dos Santos – RM551168
  
## 🎯 Descrição do Problema
Encontrar pessoas em ambientes escuros é um grande desafio para equipes de busca e monitoramento. Em períodos noturnos, a falta de visibilidade dificulta a identificação rápida, aumentando o risco de pessoas serem deixadas para trás e não receberem socorro em tempo hábil.

## 💡 Visão Geral da Solução
Desenvolvemos um sistema em Python capaz de processar vídeos noturnos, identificar pessoas automaticamente usando IA (MediaPipe Pose) e destacar cada indivíduo com um quadro verde ao redor do corpo. O sistema também coleta as coordenadas das pessoas e marca suas localizações em um mapa. Caso haja mais de uma pessoa, o mapa exibe a quantidade total de pessoas detectadas no local.

O sistema grava o frame no momento da detecção, permitindo análises futuras. Dessa forma, é possível mapear o ambiente e quantificar, em tempo real, quantas pessoas estão presentes.

Além disso, ao mapear as pessoas, a câmera consegue criar um modelo 3D do ambiente. Assim, órgãos como Defesa Civil, ONGs e outras entidades podem visualizar o local em 3D, facilitando o planejamento de estratégias para o resgate de pessoas em situação de risco.


- Aplicação para drones, câmeras em geral.

  ====== Realizar ajustes **** 

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



   
