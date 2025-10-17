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
