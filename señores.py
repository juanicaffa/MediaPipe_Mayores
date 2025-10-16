import cv2
import mediapipe as mp
import numpy as np

# Inicializamos MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Abrir cámara
cap = cv2.VideoCapture(0)

# Umbrales de detección
UMBRAL_ANGULO = 60     # Ángulo de inclinación para considerar caída
UMBRAL_ALTURA = 0.4    # Relación de altura de cadera respecto al frame

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convertimos a RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)

        # Volvemos a BGR para OpenCV
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            h, w, _ = image.shape

            # Coordenadas principales (cadera y hombros)
            cadera = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            hombro = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]

            # Altura relativa de la cadera
            altura_cadera = cadera.y

            # Vector hombro-cadera
            dx = hombro.x - cadera.x
            dy = hombro.y - cadera.y
            angulo = np.degrees(np.arctan2(dy, dx))

            # Normalizamos ángulo
            if angulo < 0:
                angulo += 180

            # Condición de caída: muy inclinado y cadera baja
            if angulo < UMBRAL_ANGULO and altura_cadera > UMBRAL_ALTURA:
                cv2.putText(image, "Persona aterrizo", (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

            # Dibujamos pose
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow("Deteccion de caidas", image)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
