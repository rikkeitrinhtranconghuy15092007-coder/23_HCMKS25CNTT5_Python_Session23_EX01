import datetime

def predict_eta(departure_str: str, distance_km: float, speed: float = 60.0) -> datetime.datetime:
    """
    Tính toán thời gian dự kiến đến nơi (ETA) dựa trên thời gian khởi hành, khoảng cách và vận tốc.
    """
    # Ép kiểu chuỗi (string) sang đối tượng datetime chuyên dụng
    dep_time = datetime.datetime.strptime(departure_str, "%Y-%m-%d %H:%M:%S")
    
    # Tính số giờ cần thiết
    hours_needed = distance_km / speed
    
    # Cộng thêm khoảng thời gian di chuyển vào thời gian khởi hành
    eta = dep_time + datetime.timedelta(hours=hours_needed)
    return eta