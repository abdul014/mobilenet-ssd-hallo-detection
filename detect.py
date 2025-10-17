# file: detect.py

import re
import cv2
import numpy as np

# Gunakan tflite_runtime kalau ada (Raspberry Pi), kalau tidak fallback ke TensorFlow Lite (PC/Laptop)
try:
    from tflite_runtime.interpreter import Interpreter
except ImportError:
    from tensorflow.lite.python.interpreter import Interpreter

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480


def load_labels(path: str = "labels.txt"):
    """Loads the labels file. Supports files with or without index numbers."""
    labels = {}
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for row_number, content in enumerate(lines):
            pair = re.split(r"[:\s]+", content.strip(), maxsplit=1)
            if len(pair) == 2 and pair[0].isdigit():
                labels[int(pair[0])] = pair[1].strip()
            else:
                labels[row_number] = pair[0].strip()
    return labels


def set_input_tensor(interpreter, image: np.ndarray) -> None:
    """Sets the input tensor."""
    tensor_index = interpreter.get_input_details()[0]["index"]
    input_tensor = interpreter.tensor(tensor_index)()[0]
    # normalisasi ke 0..1
    input_tensor[:, :] = np.expand_dims(image / 255.0, axis=0)


def get_output_tensor(interpreter, index: int) -> np.ndarray:
    """Returns the output tensor at the given index."""
    output_details = interpreter.get_output_details()[index]
    tensor = np.squeeze(interpreter.get_tensor(output_details["index"]))
    return tensor


def detect_objects(interpreter, image: np.ndarray, threshold: float):
    """Returns a list of detection results, each a dictionary of object info."""
    set_input_tensor(interpreter, image)
    interpreter.invoke()

    boxes = get_output_tensor(interpreter, 0)
    classes = get_output_tensor(interpreter, 1)
    scores = get_output_tensor(interpreter, 2)
    count = int(get_output_tensor(interpreter, 3))

    results = []
    for i in range(count):
        if scores[i] >= threshold:
            results.append(
                {
                    "bounding_box": boxes[i],
                    "class_id": int(classes[i]),
                    "score": float(scores[i]),
                }
            )
    return results


def main():
    labels = load_labels()
    interpreter = Interpreter(model_path="detect.tflite")
    interpreter.allocate_tensors()

    _, input_height, input_width, _ = interpreter.get_input_details()[0]["shape"]

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Kamera tidak bisa dibuka")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize ke ukuran input model
        img = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), (input_width, input_height))

        results = detect_objects(interpreter, img, threshold=0.8)
        print(results)

        for result in results:
            ymin, xmin, ymax, xmax = result["bounding_box"]
            xmin = int(max(1, xmin * CAMERA_WIDTH))
            xmax = int(min(CAMERA_WIDTH, xmax * CAMERA_WIDTH))
            ymin = int(max(1, ymin * CAMERA_HEIGHT))
            ymax = int(min(CAMERA_HEIGHT, ymax * CAMERA_HEIGHT))

            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)
            label_text = labels.get(result["class_id"], str(result["class_id"]))
            cv2.putText(
                frame,
                f"{label_text} {result['score']:.2f}",
                (xmin, min(ymax, CAMERA_HEIGHT - 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

        cv2.imshow("Detection", frame)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
