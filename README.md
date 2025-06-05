# Detecção Automática de Pessoas em Vídeos Noturnos

## 👥 Integrantes

- Laura Claro Mathias – RM98747
- Guilherme Silva Dos Santos – RM551168
  
## 🎯 Descrição do Problema
Encontrar pessoas em ambientes escuros é um grande desafio para equipes de busca e monitoramento. Em períodos noturnos, a falta de visibilidade dificulta a identificação rápida, aumentando o risco de pessoas serem deixadas para trás e não receberem socorro em tempo hábil.

## 💡 Visão Geral da Solução
Desenvolvemos um sistema em Python capaz de processar vídeos noturnos, identificar pessoas automaticamente usando IA (MediaPipe Pose) e destacar cada indivíduo com um quadro verde ao redor do corpo. O sistema também coleta as coordenadas das pessoas e marca suas localizações em um mapa. Caso haja mais de uma pessoa, o mapa exibe a quantidade total de pessoas detectadas no local.

O sistema grava o frame no momento da detecção, permitindo análises futuras. Dessa forma, é possível mapear o ambiente e quantificar, em tempo real, quantas pessoas estão presentes.

Além disso, ao mapear as pessoas, criamos um algoritmo que gera uma rota otimizada, considerando o ponto de partida e a quantidade de pessoas presentes na região. Dessa forma, órgãos como Defesa Civil, ONGs e outras entidades podem planejar estratégias mais eficientes para o resgate de pessoas em situação de risco.

- Aplicação para drones, câmeras em geral.

  ====== Realizar ajustes **** 

## Como Funciona

1. O usuário executa o script com um vídeo noturno (por exemplo, `all.mp4`).
2. O sistema processa cada frame do vídeo.
3. Quando uma pessoa é detectada, o sistema desenha um quadro verde ao redor dela, mostra a mensagem "Pessoa detectada" e salva o frame.
4. O sistema pode gerar mapas e uma rota otimizada para resgate.

## 📽️ Demonstração

[**Assista ao vídeo explicativo**](https://youtu.be/WDeKiATP7fQ)


## 📷 Exemplo de Funcionamento

![image](https://github.com/user-attachments/assets/0cea236d-3736-4630-ae07-dafca37a02af)
![image](https://github.com/user-attachments/assets/784598f8-8d69-480b-ac4e-4d97541ec4aa)
![image](https://github.com/user-attachments/assets/e642898c-c8ca-4cf4-ba98-dd108009cb66)
![image](https://github.com/user-attachments/assets/4df8dae7-0903-4243-94fd-2ea234c7592e)


### Pré-requisitos

- Python 3.8+

### Dependências

O projeto depende de:

- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/project/mediapipe/)
- [NumPy](https://pypi.org/project/numpy/)

**Para instalar todas as dependências:**

```bash
pip install -r requirements.txt
```

### Passo a passo para rodar

```bash
git clone https://github.com/GuilhermeSSantos2004/detecao-pessoas-visao-noturna.git
cd detecao-pessoas-visao-noturna
```
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
# ou
venv\Scripts\activate      # Windows
```
### Instale as dependências:
```bash
pip install -r requirements.txt
```

### Execute o script principal:
```bash
python3 yolo_sort_track.py
```
E para gerar o mapa, executar:
```bash
python3 yolo_sort_track.py
```



