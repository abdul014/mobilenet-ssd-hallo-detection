<h1 align="center">🧠 MobileNet-SSD Object Detection — Label “Hallo”</h1>

<p align="center">
  <img src="https://github.com/abdul014/mobilenet-ssd-hallo-detection/blob/main/Object%20Detection%20Test.gif?raw=true" width="700" alt="MobileNet SSD Demo">
</p>

<p align="center">
  <b>Implementasi TensorFlow Object Detection menggunakan model MobileNet-SSD</b><br>
  Didesain agar berjalan ringan di <b>Windows</b> maupun <b>Raspberry Pi</b>, dengan label kustom <code>“hallo”</code>.
</p>

---

## 📑 Daftar Isi
<p align="center">
  <a href="#-tentang-proyek">🎯 Tentang Proyek</a> •
  <a href="#-arsitektur-dan-labeling">🧩 Arsitektur & Labeling</a> •
  <a href="#️-instalasi--konfigurasi">⚙️ Instalasi</a> •
  <a href="#-menjalankan-deteksi">🚀 Jalankan</a> •
  <a href="#-hasil-dan-demo">📸 Demo</a> •
  <a href="#-disusun-oleh">✍️ Penulis</a>
</p>

---

## 🎯 Tentang Proyek
Proyek ini menunjukkan penerapan **object detection real-time** menggunakan model **MobileNet-SSD** yang dikonversi ke format **TensorFlow Lite (.tflite)**.  
Model digunakan untuk mengenali objek khusus dengan label **“hallo”** dan divisualisasikan menggunakan **OpenCV**.

> 🧠 Model MobileNet-SSD dipilih karena ringan, cepat, dan cocok untuk deployment di edge device.

---

## 🧩 Arsitektur dan Labeling

### 🔹 Arsitektur Model
MobileNet-SSD (Single Shot Multibox Detector) menggabungkan kecepatan tinggi dengan akurasi yang memadai menggunakan backbone **MobileNet**.

---

### 🏷️ Labeling dengan LabelImg
Untuk membuat dataset kustom (misalnya label “hallo”), digunakan **[LabelImg](https://github.com/HumanSignal/labelImg)**.

<p align="center">
  <img src="https://github.com/HumanSignal/labelImg/raw/master/readme/images/label-studio-1-6-player-screenshot.png" width="750" alt="LabelImg Interface">
</p>

**Langkah singkat pelabelan:**
1. Instal `labelImg`  
   ```bash
   pip install labelImg
   ```
2. Jalankan aplikasi
   ```bash
   labelImg
   ```
3. Pilih folder dataset, beri label "hallo", lalu simpan anotasi (.xml atau .txt).
4. Ulangi proses untuk setiap gambar dalam dataset.  
5. Pastikan semua anotasi tersimpan dalam satu folder (contoh: `annotations/`) dan cocok dengan nama file gambar.  

> 💡 **Tips:** Gunakan format PascalVOC (`.xml`) jika kamu akan melakukan konversi ke TensorFlow Record, atau YOLO (`.txt`) untuk model ringan berbasis bounding box sederhana.

---

## ⚙️ Instalasi & Konfigurasi

Sebelum menjalankan proyek, pastikan Python telah terinstal dan versi TensorFlow Lite kompatibel dengan model MobileNet-SSD yang digunakan.

### 💻 Untuk Windows
```bash
pip install tensorflow opencv-python numpy
```

### 🍓 Untuk Raspberry Pi
```bash
pip3 install opencv-python
sudo apt-get install python3-tflite-runtime
```

💡 Jika kamu menggunakan **Raspberry Pi** dengan **Coral TPU**, pastikan juga menginstal `libedgetpu1-std` dan `pycoral` agar inference berjalan lebih cepat.

---

## ⚡ Struktur Folder Utama
```
mobilenet-ssd-hallo-detection/
├── detect.py
├── detect.tflite
├── labels.txt
├── images/
│   ├── dataset_samples.png
│   └── detection_demo.png
└── README.md
```
> Pastikan file `detect.tflite` dan `labels.txt` berada satu folder dengan `detect.py`.

---

## 🚀 Menjalankan Deteksi
Untuk menjalankan deteksi secara real-time, gunakan perintah berikut:
```bash
python detect.py
```
Script akan membuka kamera default (`cv2.VideoCapture(0)`) dan mulai mendeteksi objek dengan label **“hallo”**.

### 🎮 Kontrol
- Tekan **Q** → keluar dari jendela deteksi  
- Tekan **S** → menyimpan frame hasil deteksi *(opsional, bisa ditambahkan di script)*  

Jika kamera tidak terbaca, ubah indeks kamera dengan:
```python
cap = cv2.VideoCapture(1)
```
> 🔧 Gantilah angka `1` sesuai dengan perangkat kamera eksternal yang digunakan.

---

## 📸 Contoh Hasil Deteksi
<p align="center">
  <img src="https://i.imgur.com/BjYxjZc.png" width="700" alt="Detection Result Example">
</p>

Hasil deteksi akan menampilkan:
- **Bounding box hijau** di sekitar objek yang dikenali  
- **Label dan skor confidence** di atas bounding box  

**Contoh Output Log:**
```bash
[{'bounding_box': [0.18, 0.32, 0.67, 0.82],
  'class_id': 0,
  'score': 0.91}]
```

---

## 🧠 Penjelasan Inti Kode `detect.py`
Berikut cuplikan penting dari fungsi deteksi utama:
```python
def detect_objects(interpreter, image: np.ndarray, threshold: float):
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    boxes = get_output_tensor(interpreter, 0)
    classes = get_output_tensor(interpreter, 1)
    scores = get_output_tensor(interpreter, 2)
    count = int(get_output_tensor(interpreter, 3))
    results = []
    for i in range(count):
        if scores[i] >= threshold:
            results.append({
                "bounding_box": boxes[i],
                "class_id": int(classes[i]),
                "score": float(scores[i]),
            })
    return results
```

Kode di atas akan:
1. Mengirim citra (`image`) ke model TFLite.  
2. Menjalankan *inference*.  
3. Mengambil output berupa **bounding box**, **class ID**, dan **skor deteksi**.  
4. Mengembalikan daftar hasil deteksi untuk divisualisasikan oleh **OpenCV**.

---

## 🎬 Jalankan Proyek di Google Colab
Kamu bisa mencoba langsung proyek ini di **Google Colab** tanpa konfigurasi manual:
<p align="center">
  <a href="https://colab.research.google.com/github/abdul014/mobilenet-ssd-hallo-detection/blob/main/MobileNet_SSD_ObjectDetection.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
  </a>
</p>

---

## ✍️ Disusun Oleh
**Abd Rahman**  
_From Komunitas EraNusaData_  
Magister Statistika dan Sains Data, IPB University  

📧 [GitHub](https://github.com/abdul014) • [LinkedIn](https://linkedin.com/in/abd-rahman-ysf)

---

## 📄 Lisensi
Distribusi di bawah lisensi **MIT License**  
Gunakan, modifikasi, dan kembangkan proyek ini dengan tetap mencantumkan atribusi.
