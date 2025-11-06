def read_entire_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("NỘI DUNG FILE:")
            print("-" * 30)
            print(content)
            print("-" * 30)
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
    except PermissionError:
        print(f"Không có quyền truy cập file: {filename}")
    except Exception as e:
        print(f"Lỗi: {e}")

# Sử dụng
read_entire_file('test.txt')
