import os

def create_log_dir(dir_name: str) -> bool:
    """
    Kiểm tra an toàn và tạo thư mục lưu trữ log nếu chưa tồn tại.
    Tránh lỗi FileExistsError.
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        return True
    return False