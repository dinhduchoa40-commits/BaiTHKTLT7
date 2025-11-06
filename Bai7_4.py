def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"{n} DÒNG ĐẦU TIÊN:")
            print("-" * 20)
            for i, line in enumerate(file):
                if i < n:
                    print(f"{i+1}: {line.rstrip()}")
                else:
                    break
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
    except PermissionError:
        print(f"Không có quyền truy cập file: {filename}")
    except Exception as e:
        print(f"Lỗi: {e}")

# Sử dụng
read_first_n_lines('test.txt', 3)
