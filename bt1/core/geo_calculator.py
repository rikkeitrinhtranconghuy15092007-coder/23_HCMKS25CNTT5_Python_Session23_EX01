import math

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Tính khoảng cách đường chim bay giữa 2 điểm dựa trên Kinh/Vĩ độ sử dụng công thức Haversine.
    Đơn vị trả về: km
    """
    # Chuyển đổi từ độ sang radian
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Công thức Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    r = 6371 # Bán kính Trái Đất theo km
    return c * r