import cv2
import numpy as np

# Webcam'ı başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Görüntüyü BGR'den HSV'ye dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını belirle
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # HSV görüntüsünü kırmızı renk aralığına göre filtrele
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Orijinal görüntüde sadece kırmızı olan yerleri siyah yap
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonuçları göster
    cv2.imshow('Original', frame)
    cv2.imshow('Only Red', result)

    # Çıkış için 'q' tuşuna basılmasını bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Webcam'ı serbest bırak
cap.release()

# Pencereyi kapat
cv2.destroyAllWindows()
