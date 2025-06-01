import cv2
from ultralytics import YOLO
import numpy as np
import sys
import os


sys.path.append(os.path.abspath("sort"))
from sort import Sort

# salva os frames 
SAVE_DIR = "frames_novos_ids"
os.makedirs(SAVE_DIR, exist_ok=True)

# modelo YOLO
model = YOLO('yolov8n.pt')
tracker = Sort()


VIDEO_PATH = './videos/all.mp4'
 
cap = cv2.VideoCapture(VIDEO_PATH)
font = cv2.FONT_HERSHEY_SIMPLEX

frame_id = 0
ids_salvos = set()  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_id += 1

    results = model(frame)[0]
    dets = []
    for box in results.boxes:
        cls = int(box.cls[0])
        if cls == 0:  
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            dets.append([x1, y1, x2, y2, conf])


    dets = np.array(dets, dtype=float)
    if dets.size == 0:
        dets = np.empty((0, 5))
    elif dets.ndim == 1 and dets.shape[0] == 5:
        dets = dets.reshape(1, 5)
    elif dets.ndim == 2 and dets.shape[1] != 5:
        print("Shape inesperado em dets:", dets.shape)
        dets = np.empty((0, 5))

    # Atualiza o tracker com as detecções atuais
    tracks = tracker.update(dets)
    ids = [int(t[4]) for t in tracks]

    # check se apareceu algum novo ID (pessoa nova)
    novos_ids = [id_ for id_ in ids if id_ not in ids_salvos]
    if novos_ids:
        cv2.imwrite(f"{SAVE_DIR}/frame_{frame_id:05d}.jpg", frame)
        for novo_id in novos_ids:
            ids_salvos.add(novo_id)

    # caixas e os IDs na tela
    for track in tracks:
        x1, y1, x2, y2, track_id = map(int, track)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f'ID: {track_id}', (x1, y1-10), font, 0.8, (0,0,255), 2)

    # Mostra o total de pessoas que foi detectada 
    total_pessoas = len(set(ids))
    cv2.rectangle(frame, (10, 10), (300, 60), (255,255,255), -1)
    cv2.putText(frame, f'TOTAL PESSOAS AGORA: {total_pessoas}', (20, 45), font, 1, (0,0,0), 2)

    cv2.imshow("YOLO + SORT Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
