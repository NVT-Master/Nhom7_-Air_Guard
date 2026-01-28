# 🌬️ AIR GUARD – PM2.5 Forecasting & AQI Alerts using Semi-Supervised Learning

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.txt)

> **Mini Project - Data Mining Course**  
> Ứng dụng Semi-Supervised Learning (Self-Training & Co-Training) để dự báo chất lượng không khí và cảnh báo AQI.
- Nhóm 7:
- Bế Quang Hải - MSV: 1771040011
- Nguyễn Văn Tiến - MSV: 1771040025
- Nguyễn Duy Thuận - MSV: 1771040024

---

## 📋 Mục lục

- [Giới thiệu](#-giới-thiệu)
- [Dataset](#-dataset)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [Cài đặt](#️-cài-đặt)
- [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
- [Phương pháp](#-phương-pháp)
- [Kết quả](#-kết-quả)
- [Tài liệu tham khảo](#-tài-liệu-tham-khảo)

---

## 🎯 Giới thiệu

### Bối cảnh

Ô nhiễm không khí, đặc biệt là bụi mịn PM2.5, là vấn đề môi trường nghiêm trọng. Dự án xây dựng hệ thống:

1. **Dự báo PM2.5** (regression + ARIMA)
2. **Phân lớp AQI** để cảnh báo theo trạm
3. **Semi-Supervised Learning** khi thiếu nhãn AQI

### Tại sao Semi-Supervised Learning?

| Thách thức | Giải pháp |
|------------|-----------|
| Dữ liệu có nhãn khan hiếm | Tận dụng 95% dữ liệu không nhãn |
| Gắn nhãn thủ công tốn kém | Pseudo-labeling tự động |
| Class imbalance | Self-Training & Co-Training |

### Thiết kế

- **OOP**: Thư viện trong `src/`
- **Notebook-per-task**: Mỗi notebook làm 1 nhiệm vụ
- **Tutorial Notebooks**: Hướng dẫn chi tiết từng bước

---

## 📊 Dataset

### Beijing Multi-Site Air Quality Dataset

| Thông tin | Chi tiết |
|-----------|----------|
| **Nguồn** | [UCI ML Repository](https://archive.ics.uci.edu/dataset/501) |
| **Thời gian** | 01/03/2013 – 28/02/2017 |
| **Trạm** | 12 trạm tại Bắc Kinh |
| **Tần suất** | Hàng giờ (~420,000 records) |

### Các biến chính

| Biến | Mô tả | Đơn vị |
|------|-------|--------|
| PM2.5 | Nồng độ bụi mịn | μg/m³ |
| PM10, SO2, NO2, CO, O3 | Chất ô nhiễm khác | μg/m³ |
| TEMP, PRES, DEWP | Nhiệt độ, áp suất, điểm sương | °C, hPa |
| RAIN, WSPM | Lượng mưa, tốc độ gió | mm, m/s |

### AQI Classes (6 mức)

| Class | PM2.5 24h (μg/m³) | Mức độ |
|-------|-------------------|--------|
| 🟢 Good | 0 - 12 | Tốt |
| 🟡 Moderate | 12.1 - 35.4 | Trung bình |
| 🟠 Unhealthy_Sensitive | 35.5 - 55.4 | Không tốt cho nhóm nhạy cảm |
| 🔴 Unhealthy | 55.5 - 150.4 | Không tốt |
| 🟣 Very_Unhealthy | 150.5 - 250.4 | Rất không tốt |
| 🟤 Hazardous | > 250.4 | Nguy hiểm |

### Cách nạp dữ liệu

```python
# Cách 1: Dùng file ZIP local (khuyến nghị)
USE_UCIMLREPO = False
RAW_ZIP_PATH = "data/raw/PRSA2017_Data_20130301-20170228.zip"

# Cách 2: Tải từ UCI
USE_UCIMLREPO = True
```

> ⚠️ **Lưu ý leakage**: Không dùng `PM2.5` / `pm25_24h` làm feature cho mô hình phân lớp AQI.

---

## 📁 Cấu trúc dự án

```
air_guard/
├── 📄 README.md                    # File này
├── 📄 requirements.txt             # Dependencies
├── 📄 LICENSE.txt                  # MIT License
├── 📄 run_papermill.py             # Chạy pipeline tự động
│
├── 📂 data/
│   ├── raw/                        # ZIP dữ liệu gốc
│   └── processed/                  # Dữ liệu đã xử lý
│       └── dataset_semi_supervised.parquet
│
├── 📂 notebooks/
│   │
│   │   # === TUTORIAL NOTEBOOKS (Khuyến nghị cho sinh viên) ===
│   ├── 📓 air_guard_tutorial.ipynb          # Phần 1-5: EDA → Baseline
│   ├── 📓 air_guard_semi_supervised.ipynb   # Phần 6-9: Semi-Supervised
│   │
│   │   # === PIPELINE NOTEBOOKS ===
│   ├── preprocessing_and_eda.ipynb
│   ├── feature_preparation.ipynb
│   ├── classification_modelling.ipynb
│   ├── regression_modelling.ipynb
│   ├── arima_forecasting.ipynb
│   ├── semi_dataset_preparation.ipynb
│   ├── semi_self_training.ipynb
│   ├── semi_co_training.ipynb
│   ├── semi_supervised_report.ipynb
│   └── runs/                        # Output từ Papermill
│
└── 📂 src/
    ├── __init__.py
    ├── classification_library.py    # Hàm cho classification
    ├── regression_library.py        # Hàm cho regression
    ├── semi_supervised_library.py   # Self-Training, Co-Training
    └── timeseries_library.py        # Xử lý chuỗi thời gian
```

---

## ⚙️ Cài đặt

### Yêu cầu
- Python 3.10+
- 8GB RAM (khuyến nghị 16GB)

### Cài đặt

```bash
# Clone repository
git clone https://github.com/your-username/air_guard.git
cd air_guard

# Tạo môi trường Conda
conda create -n beijing_env python=3.11 -y
conda activate beijing_env

# Cài đặt packages
pip install -r requirements.txt

# Đăng ký kernel cho Jupyter
python -m ipykernel install --user --name beijing_env --display-name "beijing_env"
```

### Kiểm tra
```bash
python -c "import pandas, sklearn, numpy; print('OK')"
```

---

## 🚀 Hướng dẫn sử dụng

### 🎓 Cách 1: Tutorial Notebooks (Khuyến nghị)

**Bước 1**: Chạy Tutorial Part 1

```bash
jupyter notebook notebooks/air_guard_tutorial.ipynb
```

Nội dung:
- ✅ **Phần 1**: Load và khám phá dữ liệu
- ✅ **Phần 2**: Phân tích Missing Values
- ✅ **Phần 3**: Gắn nhãn AQI, chia Labeled/Unlabeled (5%/95%)
- ✅ **Phần 4**: Feature Engineering (Lag, Rolling, Time)
- ✅ **Phần 5**: Supervised Baseline

**Bước 2**: Chạy Tutorial Part 2

```bash
jupyter notebook notebooks/air_guard_semi_supervised.ipynb
```

Nội dung:
- ✅ **Phần 6**: Self-Training (Pseudo-labeling)
- ✅ **Phần 7**: Co-Training (Two-view learning)
- ✅ **Phần 8**: Thử nghiệm tham số (τ = 0.8, 0.9)
- ✅ **Phần 9**: Tổng kết và so sánh

### ⚡ Cách 2: Pipeline tự động (Papermill)

```bash
python run_papermill.py
```

Output:
- Notebooks: `notebooks/runs/*_run.ipynb`
- Artifacts: `data/processed/`

---

## 🔬 Phương pháp

### Pipeline tổng quan

```
┌─────────────────────────────────────────────────────────────────┐
│                     AIR GUARD Pipeline                          │
├─────────────────────────────────────────────────────────────────┤
│  1. Data Loading        → Tải từ UCI Repository                 │
│  2. EDA                 → Khám phá, phân tích missing           │
│  3. AQI Labeling        → Gắn nhãn 6 mức từ PM2.5 24h           │
│  4. Train/Test Split    → Theo thời gian (2017 = test)          │
│  5. Labeled/Unlabeled   → 5% labeled, 95% unlabeled             │
│  6. Feature Engineering → Lag, Rolling, Time features           │
│  7. Supervised Baseline → HistGradientBoosting (5% data)        │
│  8. Self-Training       → Pseudo-labeling iterative             │
│  9. Co-Training         → Two-view collaborative learning       │
│ 10. Evaluation          → Compare all methods                   │
└─────────────────────────────────────────────────────────────────┘
```

### 1️⃣ Self-Training

```
Algorithm Self-Training:
    Input: L (labeled), U (unlabeled), τ (threshold)
    
    1. Train model M on L
    2. Repeat until convergence:
        a. Predict probabilities for U
        b. Select samples with confidence >= τ
        c. Add pseudo-labeled samples to L
        d. Retrain M
    3. Return: Improved model M
```

**Tham số**: `τ ∈ {0.85, 0.90, 0.95}`, `max_iter = 10`

### 2️⃣ Co-Training

```
Algorithm Co-Training:
    Input: L, U, View1 (temporal), View2 (environmental)
    
    1. Train M1 on L[View1], M2 on L[View2]
    2. Repeat:
        a. M1 predicts → confident samples
        b. M2 predicts → confident samples
        c. Exchange pseudo-labels (consensus)
        d. Retrain both
    3. Return: Ensemble M1 + M2
```

**Chia View**:
- **View 1 (Temporal)**: hour, day, month, lag features
- **View 2 (Environmental)**: TEMP, PRES, WSPM, rolling features

---

## 📈 Kết quả

### So sánh các phương pháp

| Phương pháp | Accuracy | F1 Macro | F1 Weighted |
|-------------|----------|----------|-------------|
| Supervised Baseline (5% data) | ~0.65 | ~0.40 | ~0.63 |
| Self-Training (τ=0.9) | ~0.67 | ~0.42 | ~0.65 |
| Self-Training (τ=0.8) | ~0.66 | ~0.41 | ~0.64 |
| Co-Training | ~0.68 | ~0.43 | ~0.66 |

> **Lưu ý**: Kết quả thay đổi tùy random seed.

### 💡 Insights chính

1. **Semi-supervised cải thiện** ~2-5% khi chỉ có 5% labeled data
2. **Threshold τ quan trọng**: τ cao → pseudo-label chất lượng hơn
3. **Co-Training hiệu quả** khi hai view độc lập
4. **Class imbalance** vẫn là thách thức (lớp Hazardous khó dự đoán)

---

## 📚 Thư viện OOP (src/)

### `classification_library.py`
- `time_split(df, cutoff)`: Chia train/test theo thời gian
- `train_classifier(...)`: Train và evaluate model
- `AQI_CLASSES`: Danh sách 6 mức AQI

### `semi_supervised_library.py`
- `SelfTrainingAQIClassifier`: Self-training với pseudo-labeling
- `CoTrainingAQIClassifier`: Co-training với 2 views
- `mask_labels_time_aware(...)`: Giả lập thiếu nhãn
- `add_alert_columns(...)`: Tạo cột cảnh báo

---

## 📝 Tài liệu tham khảo

### Papers
1. Yarowsky, D. (1995). *Unsupervised Word Sense Disambiguation*
2. Blum & Mitchell (1998). *Combining Labeled and Unlabeled Data with Co-Training*

### Dataset
- Zhang, S., et al. (2017). *Cautionary Tales on Air-Quality Improvement in Beijing*
- [UCI ML Repository - Beijing Air Quality](https://archive.ics.uci.edu/dataset/501)

---

## 👤 Tác giả

- **Sinh viên**: Nhóm 7
- **Môn học**: Data Mining
- **Học kỳ**: HK2 - Năm 3

---

## 📄 License

MIT — Sử dụng tự do cho nghiên cứu, học thuật và ứng dụng nội bộ.

---

<p align="center">
  <b>⭐ Nếu dự án hữu ích, hãy cho một star! ⭐</b>
</p>
