def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = 0
            for line in file:
                line_count += 1
            print(f"Số dòng trong file: {line_count}")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
    except PermissionError:
        print(f"Không có quyền truy cập file: {filename}")
    except Exception as e:
        print(f"Lỗi: {e}")

# Sử dụng
count_lines('test.txt')
