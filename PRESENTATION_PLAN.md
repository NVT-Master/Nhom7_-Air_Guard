# 📋 KẾ HOẠCH THUYẾT TRÌNH
## AIR GUARD - Hệ thống dự báo PM2.5 và cảnh báo chất lượng không khí

---

## 🎯 MỤC TIÊU THUYẾT TRÌNH

| Mục tiêu | Chi tiết |
|----------|----------|
| **Đối tượng** | Ban lãnh đạo / Sếp |
| **Thời lượng** | 15-20 phút |
| **Mục đích** | Báo cáo kết quả dự án, đề xuất triển khai |
| **Kết quả mong đợi** | Được approve để phát triển tiếp |

---

## 📊 CẤU TRÚC SLIDE (12 slides)

### **PHẦN 1: MỞ ĐẦU (3 slides, ~3 phút)**

#### Slide 1: Title Slide
- Tên dự án: AIR GUARD
- Tagline: "Bảo vệ sức khỏe cộng đồng bằng AI"
- Tên nhóm, ngày trình bày

#### Slide 2: Vấn đề kinh doanh (Problem Statement)
- Ô nhiễm không khí tại Việt Nam/Châu Á nghiêm trọng
- Chi phí y tế do ô nhiễm: X tỷ USD/năm
- Nhu cầu dự báo và cảnh báo sớm
- **Hook**: "Mỗi ngày chúng ta hít thở 11,000 lít không khí..."

#### Slide 3: Giải pháp đề xuất
- Hệ thống AI dự báo PM2.5 và AQI
- Cảnh báo realtime cho người dùng
- Dashboard theo dõi cho cơ quan quản lý

---

### **PHẦN 2: DỮ LIỆU & PHƯƠNG PHÁP (3 slides, ~4 phút)**

#### Slide 4: Tổng quan dữ liệu
- Nguồn: UCI - Beijing Air Quality (uy tín)
- Quy mô: 420,768 records, 12 trạm, 4 năm
- Minh họa bản đồ các trạm

#### Slide 5: Phương pháp tiếp cận
- Pipeline: Raw → Clean → Features → Models → Dashboard
- Điểm đặc biệt: Semi-Supervised Learning
- Tại sao Semi-Supervised? → Tiết kiệm chi phí gán nhãn

#### Slide 6: Kỹ thuật Semi-Supervised Learning
- Self-Training: Học từ dữ liệu tự gán nhãn
- Co-Training: 2 models học lẫn nhau
- Diagram minh họa đơn giản

---

### **PHẦN 3: KẾT QUẢ (3 slides, ~5 phút)**

#### Slide 7: Kết quả chính (KEY SLIDE ⭐)
- Bảng so sánh 3 models
- **Highlight**: Self-Training cải thiện 6.2% F1-Score
- Biểu đồ cột trực quan

#### Slide 8: Demo Dashboard
- Screenshot dashboard
- Các tính năng chính
- QR code để sếp xem live demo

#### Slide 9: Phân tích chi tiết
- Classification report theo từng AQI class
- Nhận xét điểm mạnh/yếu
- So sánh với các nghiên cứu khác

---

### **PHẦN 4: KẾT LUẬN & ĐỀ XUẤT (3 slides, ~5 phút)**

#### Slide 10: Kết luận
- ✅ Những gì đã đạt được
- ⚠️ Hạn chế hiện tại
- 💡 Bài học kinh nghiệm

#### Slide 11: Đề xuất phát triển
- **Phase 2**: Tích hợp realtime API
- **Phase 3**: Mobile app cảnh báo
- **ROI dự kiến**: Tiết kiệm X% chi phí y tế

#### Slide 12: Q&A
- Cảm ơn
- Thông tin liên hệ
- GitHub link

---

## 🎤 SCRIPT THUYẾT TRÌNH

### Opening (30 giây)
> "Kính chào anh/chị. Hôm nay em xin trình bày dự án AIR GUARD - một giải pháp AI giúp dự báo ô nhiễm không khí và bảo vệ sức khỏe cộng đồng."

### Problem Hook (1 phút)
> "Mỗi ngày, một người trưởng thành hít thở khoảng 11,000 lít không khí. Tại Hà Nội, có những ngày chỉ số AQI vượt ngưỡng 300 - mức nguy hại. Câu hỏi đặt ra: Làm sao để dự báo trước và cảnh báo người dân?"






### Solution (1 phút)
> "AIR GUARD sử dụng Machine Learning để phân tích dữ liệu từ các trạm quan trắc, dự đoán nồng độ PM2.5 và phân loại chất lượng không khí thành 6 mức độ từ Tốt đến Nguy hại."

### Key Results (2 phút)
> "Điểm nổi bật của dự án là áp dụng Semi-Supervised Learning - kỹ thuật cho phép học từ cả dữ liệu có nhãn và không nhãn. Kết quả cho thấy Self-Training cải thiện F1-Score lên 53.4%, tăng 6.2% so với phương pháp truyền thống. Điều này có nghĩa là mô hình dự đoán chính xác hơn ở tất cả các mức độ ô nhiễm."

### Demo (2 phút)
> "Đây là dashboard của hệ thống. Anh/chị có thể thấy biểu đồ AQI realtime, thống kê theo từng trạm, và so sánh hiệu suất các models..."

### Closing (1 phút)
> "Tóm lại, AIR GUARD đã chứng minh tiềm năng của Semi-Supervised Learning trong bài toán dự báo môi trường. Em đề xuất phát triển tiếp Phase 2 với tích hợp API realtime. Xin cảm ơn anh/chị đã lắng nghe."

---

## 💡 TIPS THUYẾT TRÌNH

### DO ✅
- Bắt đầu bằng vấn đề thực tế (số liệu, câu chuyện)
- Nhấn mạnh **Business Value** hơn là kỹ thuật
- Dùng biểu đồ đơn giản, dễ hiểu
- Chuẩn bị sẵn demo backup (video/screenshot)
- Eye contact, giọng nói rõ ràng

### DON'T ❌
- Không đọc slide
- Không dùng quá nhiều thuật ngữ kỹ thuật
- Không để slide quá nhiều chữ
- Không nói quá nhanh
- Không quên cảm ơn và Q&A

---

## 📁 CHECKLIST TRƯỚC KHI THUYẾT TRÌNH

- [ ] Test slide trên máy trình chiếu
- [ ] Backup slide lên USB và cloud
- [ ] Chạy thử dashboard, đảm bảo hoạt động
- [ ] Chuẩn bị nước uống
- [ ] Đến sớm 10 phút để setup
- [ ] Tập thuyết trình ít nhất 2 lần
