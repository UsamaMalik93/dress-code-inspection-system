from ultralytics import YOLO
import cv2
import math

def video_detection(path_x):
    video_capture = path_x
    # Create a Webcam Object
    cap = cv2.VideoCapture(video_capture)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    model = YOLO("best.pt")
    classNames = ["office_shirts_jacket_hoodie", "pants_jeans", "shoes", "polo", "ripped_jeans", "t_shirt", "shorts", "male_kameez_shalwar", "m_kheri_sendal", "bhurka_scarf", "f_sleeveless_kameez_shalwar", "dupata", "no_dupata", "f_kameez_shalwar"]
    while True:
        success, img = cap.read()
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                print(x1, y1, x2, y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]

                if class_name in ["office_shirts_jacket_hoodie", "pants_jeans", "shoes", "polo", "t_shirt", "male_kameez_shalwar", "m_kheri_sendal", "bhurka_scarf", "dupata", "f_kameez_shalwar"]:
                    label = "Valid"
                elif class_name in ["ripped_jeans", "shorts", "f_sleeveless_kameez_shalwar", "no_dupata"]:
                    label = "Invalid"
                else:
                    label = f'{class_name}{conf}'

                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                print(t_size)
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)  # filled
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
        yield img

cv2.destroyAllWindows()
