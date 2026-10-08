import os
import shutil
import sys

def main():
    print("="*60)
    print("        CHƯƠNG TRÌNH TỰ ĐỘNG LỌC VÀ COPY ẢNH THEO DANH SÁCH")
    print("="*60)

    # --- 1. NHẬP DỮ LIỆU ĐẦU VÀO ---
    source_dir = input("1. Nhập đường dẫn thư mục chứa ảnh gốc: ").strip().strip('"')
    target_dir = input("2. Nhập đường dẫn thư mục đích muốn lưu ảnh: ").strip().strip('"')
    list_file_path = input("3. Nhập đường dẫn file text chứa danh sách tên ảnh: ").strip().strip('"')
    print("-" * 60)

    # --- 2. KIỂM TRA ĐIỀU KIỆN BAN ĐẦU ---
    if not os.path.exists(source_dir):
        print(f"[LỖI] Thư mục gốc không tồn tại: {source_dir}")
        return

    if not os.path.exists(list_file_path):
        print(f"[LỖI] File danh sách text không tồn tại: {list_file_path}")
        return

    # --- 3. ĐỌC DANH SÁCH TÊN ẢNH ---
    try:
        with open(list_file_path, "r", encoding="utf-8") as f:
            photo_names = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[LỖI] Không thể đọc file danh sách: {e}")
        return

    if not photo_names:
        print("[CẢNH BÁO] File danh sách trống. Không có ảnh nào để copy.")
        return

    # --- 4. TẠO THƯ MỤC ĐÍCH ---
    try:
        os.makedirs(target_dir, exist_ok=True)
    except Exception as e:
        print(f"[LỖI] Không thể tạo thư mục đích: {e}")
        return

    # --- 5. TIẾN HÀNH TÌM VÀ COPY (CÓ BẪY LỖI TRONG QUÁ TRÌNH CHẠY) ---
    print(f"Bắt đầu xử lý {len(photo_names)} file...")
    copied_count = 0
    error_count = 0

    for name in photo_names:
        source_path = os.path.join(source_dir, name)

        if os.path.exists(source_path):
            try:
                # Tiến hành copy đè nếu file đã tồn tại ở thư mục đích
                shutil.copy(source_path, target_dir)
                copied_count += 1
                print(f"[{copied_count}] Successfully copied: {name}")
            except PermissionError:
                print(f"[THẤT BẠI] Từ chối quyền truy cập (Permission Denied): {name}")
                error_count += 1
            except Exception as e:
                print(f"[THẤT BẠI] Lỗi không xác định khi copy file {name}: {e}")
                error_count += 1
        else:
            print(f"[BỎ QUA] File không tồn tại (File not found): {name}")

    # --- 6. XUẤT BÁO CÁO KẾT QUẢ ---
    print("-" * 60)
    print(f"--- HOÀN THÀNH! ---")
    print(f"• Tổng số lượng trong danh sách: {len(photo_names)} file.")
    print(f"• Đã copy thành công: {copied_count} file.")
    if error_count > 0:
        print(f"• Gặp sự cố hệ thống: {error_count} file.")
    print("="*60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[THÔNG BÁO] Chương trình bị người dùng hủy bỏ bằng tổ hợp phím tắt.")
    except Exception as e:
        print(f"\n[LỖI HỆ THỐNG CRITICAL]: {e}")
    finally:
        input("\nNhấn Enter để thoát chương trình...")