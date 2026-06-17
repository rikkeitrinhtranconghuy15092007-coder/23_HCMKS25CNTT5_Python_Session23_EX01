import datetime
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta
from utils.file_helper import create_log_dir

# Dữ liệu giả lập các chuyến xe đẩy về từ tổng đài
shipments = [
    {
        "id": "TRK-001", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 10.8231, "to_lon": 106.6297, 
        "depart": "2026-06-10 08:00:00", 
        "deadline": "2026-06-11 12:00:00"
    }, 
    {
        "id": "TRK-002", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 16.0544, "to_lon": 108.2022, 
        "depart": "2026-06-10 09:30:00", 
        "deadline": "2026-06-10 15:00:00"
    }, 
]

def main():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")
    
    # Khởi tạo thư mục log an toàn
    create_log_dir("logs")
    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    print("-" * 75)
    
    for s in shipments:
        # 1. Tính toán khoảng cách chuẩn xác (Haversine)
        distance = calculate_distance(s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"])
        
        # 2. Dự đoán ETA
        eta = predict_eta(s["depart"], distance, speed=60.0)
        
        # 3. Kiểm tra tiến độ với Deadline
        deadline = datetime.datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")
        
        print(f"[CHUYẾN XE {s['id']}]")
        print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
        
        if eta <= deadline:
            print(" + Trạng thái: 🟢 AN TOÀN (Kịp tiến độ trước deadline)")
        else:
            deadline_str = deadline.strftime("%H:%M:%S")
            print(f" + Trạng thái: 🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline_str})")
        print()
        
    print("========================================================")

if __name__ == "__main__":
    main()