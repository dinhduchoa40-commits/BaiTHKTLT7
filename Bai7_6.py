def file_read_from_tail(filename, lines):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.readlines()
            last_lines = content[-lines:]
            
            print(f"{lines} DÒNG CUỐI CÙNG:")
            print("-" * 20)
            for line in last_lines:
                print(line.rstrip())
                
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
    except PermissionError:
        print(f"Không có quyền truy cập file: {filename}")
    except Exception as e:
        print(f"Lỗi: {e}")

# Sử dụng
file_read_from_tail('test.txt', 2)
