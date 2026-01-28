# PROMPT CHO NOTEBOOKLM - TẠO SLIDE THUYẾT TRÌNH

Hãy tạo bài thuyết trình PowerPoint/Google Slides cho dự án AIR GUARD với nội dung sau:

---

## THÔNG TIN CHUNG
- **Tên dự án**: AIR GUARD - PM2.5 Forecasting & AQI Alert System
- **Tagline**: "Bảo vệ sức khỏe cộng đồng bằng AI"
- **Nhóm**: Nhóm 7 - Data Mining Mini Project
- **Năm**: 2026

---

## CẤU TRÚC 12 SLIDES

### SLIDE 1: TITLE
- Tiêu đề: AIR GUARD
- Subtitle: PM2.5 Forecasting & AQI Alert System
- Tagline: Bảo vệ sức khỏe cộng đồng bằng AI
- Nhóm 7 | Data Mining | 2026

### SLIDE 2: VẤN ĐỀ (PROBLEM)
Tiêu đề: 🚨 Tại sao cần AIR GUARD?

Nội dung chính:
- Hook: "Mỗi ngày, một người trưởng thành hít thở 11,000 lít không khí"
- Thực trạng ô nhiễm không khí tại Châu Á nghiêm trọng
- PM2.5 trung bình tại Bắc Kinh: 82.6 µg/m³ (gấp 3 lần WHO khuyến cáo)
- Chi phí y tế do ô nhiễm: 5 tỷ USD/năm
- 7 triệu ca tử vong sớm mỗi năm do ô nhiễm không khí
- Thiếu hệ thống cảnh báo sớm cho người dân

### SLIDE 3: GIẢI PHÁP (SOLUTION)
Tiêu đề: 💡 AIR GUARD - Giải pháp AI

6 tính năng chính:
1. 🔮 Dự báo PM2.5 - ML dự đoán nồng độ bụi mịn trước 24-48 giờ
2. 🏷️ Phân loại AQI - 6 mức độ từ "Tốt" đến "Nguy hại" theo chuẩn EPA
3. ⚡ Cảnh báo Realtime - Thông báo khi AQI vượt ngưỡng an toàn
4. 📊 Dashboard Trực quan - Theo dõi 12 trạm quan trắc
5. 🧠 Semi-Supervised AI - Học từ dữ liệu không nhãn, tiết kiệm chi phí
6. 🗺️ Phân tích Địa lý - So sánh chất lượng không khí giữa các khu vực

### SLIDE 4: DỮ LIỆU (DATA)
Tiêu đề: 📂 Nguồn dữ liệu

Dataset: Beijing Multi-Site Air Quality Dataset
- Nguồn: UCI Machine Learning Repository (#501)
- Quy mô: 420,768 records
- Thời gian: 03/2013 - 02/2017 (4 năm)
- Số trạm: 12 trạm quan trắc
- Tần suất: Hourly (mỗi giờ)
- Features: 18 (PM2.5, PM10, SO2, NO2, CO, O3, Temperature, Pressure, Humidity, Wind...)
- Missing rate: 2.4%

Phân loại trạm:
- Urban (7): Aotizhongxin, Dongsi, Guanyuan, Nongzhanguan, Tiantan, Wanliu, Wanshouxigong
- Suburban (2): Changping, Shunyi
- Rural (2): Dingling, Huairou
- Industrial (1): Gucheng

### SLIDE 5: PHƯƠNG PHÁP (METHODOLOGY)
Tiêu đề: ⚙️ Pipeline xử lý

Pipeline 5 bước:
Raw Data → Preprocessing → Feature Engineering → Model Training → Dashboard

Feature Engineering:
- Temporal: hour, day_of_week, month, is_weekend
- Rolling: PM2.5 trung bình 24h, standard deviation
- Lag: PM2.5 tại t-1h, t-6h, t-12h, t-24h
- AQI Class: Phân loại 6 mức độ

Models sử dụng:
- Supervised: HistGradientBoostingClassifier
- Self-Training: Pseudo-labeling iterative
- Co-Training: Multi-view learning
- Time Series: ARIMA forecasting

### SLIDE 6: SEMI-SUPERVISED LEARNING
Tiêu đề: 🧠 Semi-Supervised Learning

Tại sao Semi-Supervised?
- Labeled data đắt đỏ (cần chuyên gia gán nhãn)
- Unlabeled data dồi dào và miễn phí
- Tiết kiệm 80%+ chi phí gán nhãn
- Tận dụng 383,000+ unlabeled samples

Self-Training:
1. Train với labeled data
2. Predict trên unlabeled data
3. Chọn samples confidence > 90%
4. Thêm vào training set
5. Lặp lại 10 iterations

Co-Training:
- View 1: Temporal Features (hour, day, month...)
- View 2: Meteorological Features (temp, humidity...)
- 2 models học lẫn nhau từ 2 views độc lập

### SLIDE 7: KẾT QUẢ CHÍNH (KEY RESULTS) ⭐
Tiêu đề: 🏆 Kết quả chính

Bảng so sánh 3 models:
| Model | Accuracy | F1-Score |
|-------|----------|----------|
| Supervised (Baseline) | 60.2% | 47.2% |
| Self-Training ⭐ | 58.9% | 53.4% |
| Co-Training | 53.4% | 40.4% |

Key Finding:
✨ Self-Training cải thiện F1-Score +6.2% so với baseline
→ Chứng minh hiệu quả của Semi-Supervised Learning

Thêm biểu đồ cột so sánh F1-Score của 3 models

### SLIDE 8: PHÂN TÍCH CHI TIẾT
Tiêu đề: 📊 Phân tích theo AQI Class

Classification Report (Self-Training):
| AQI Class | Precision | Recall | F1-Score | Support |
|-----------|-----------|--------|----------|---------|
| 🟢 Good | 65.4% | 39.1% | 49.0% | 1,032 |
| 🟡 Moderate | 60.6% | 84.1% | 70.4% | 4,833 |
| 🟠 USG | 26.6% | 13.5% | 17.9% | 2,166 |
| 🔴 Unhealthy | 59.6% | 57.9% | 58.8% | 4,286 |
| 🟣 Very Unhealthy | 55.1% | 58.8% | 56.9% | 2,499 |
| 🟤 Hazardous | 78.0% | 59.7% | 67.6% | 1,855 |

Điểm mạnh:
- Hazardous: Precision 78% - phát hiện chính xác mức nguy hiểm
- Moderate: Recall 84% - ít bỏ sót trường hợp

Cần cải thiện:
- USG class: F1 chỉ 17.9% do class imbalance

### SLIDE 9: DEMO DASHBOARD
Tiêu đề: 🖥️ Dashboard Demo

Tính năng Dashboard:
- 🏠 Dashboard: Tổng quan AQI, trend chart
- 🔮 Predictions: Kết quả từ 3 models
- 📊 Comparison: So sánh hiệu suất
- 🗺️ Stations: Bản đồ 12 trạm
- ℹ️ About: Thông tin dự án

Công nghệ:
- Streamlit (Python Web Framework)
- Plotly (Interactive Charts)
- Custom CSS (Glassmorphism Design)

Link demo: http://localhost:8501
Command: streamlit run app.py

### SLIDE 10: KẾT LUẬN
Tiêu đề: ✅ Tổng kết

Đạt được:
✅ Pipeline hoàn chỉnh từ raw data → dashboard
✅ So sánh 3 phương pháp ML
✅ Self-Training cải thiện F1 +6.2%
✅ Tận dụng 383K+ unlabeled samples
✅ Dashboard production-ready

Hạn chế:
⚠️ Class imbalance ảnh hưởng Recall
⚠️ Co-Training hiệu quả thấp hơn mong đợi
⚠️ Chưa có realtime data integration

Bài học:
💡 Semi-Supervised Learning hiệu quả với dữ liệu lớn
💡 Feature engineering quan trọng hơn model complexity
💡 Dashboard cần thiết để stakeholders hiểu kết quả

### SLIDE 11: ĐỀ XUẤT PHÁT TRIỂN
Tiêu đề: 🚀 Hướng phát triển

Roadmap:
- Phase 1 (DONE ✓): ML Pipeline + Dashboard
- Phase 2 (Q2 2026): Realtime API Integration
- Phase 3 (Q4 2026): Mobile App + Push Alerts
- Phase 4 (2027): Multi-city Expansion

ROI Dự kiến:
- Giảm 15% chi phí y tế do cảnh báo sớm
- Tiết kiệm 80% chi phí gán nhãn với Semi-SSL
- Revenue từ B2B API cho doanh nghiệp

Đề xuất ngay:
- Phê duyệt Phase 2: API integration
- Budget: Thêm 2 Data Engineers
- Timeline: 3 tháng development

### SLIDE 12: CẢM ƠN & Q&A
Tiêu đề: 🙏 Cảm ơn đã lắng nghe!

Q&A Session

Contact:
- 📧 Email: nhom7@email.com
- 🔗 GitHub: github.com/NVT-Master/Nhom7_-Air_Guard

Footer: AIR GUARD - Bảo vệ sức khỏe cộng đồng bằng AI | Data Mining Mini Project | Nhóm 7 | 2026

---

## YÊU CẦU THIẾT KẾ

1. **Màu sắc**: Tone xanh dương/tím gradient (#667eea → #764ba2), nền tối (#1a1a2e)
2. **Font**: Sans-serif hiện đại (Montserrat, Open Sans)
3. **Style**: Professional, modern, clean
4. **Icons**: Sử dụng emoji để minh họa
5. **Charts**: Biểu đồ cột cho slide 7, bảng cho slide 8
6. **Animation**: Subtle fade-in effects

---

## GHI CHÚ

- Slide 7 là KEY SLIDE quan trọng nhất - cần highlight rõ ràng
- Mỗi slide không quá 6-7 bullet points
- Sử dụng visual nhiều hơn text
- Thời lượng: 15-20 phút thuyết trình
