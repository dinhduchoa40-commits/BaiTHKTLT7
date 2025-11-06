def find_longest_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            
            if not words:
                print("File trống")
                return
            
            max_length = max(len(word) for word in words)
            longest_words = [word for word in words if len(word) == max_length]
            
            print(f"Từ dài nhất ({max_length} ký tự): {longest_words}")
            
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
    except PermissionError:
        print(f"Không có quyền truy cập file: {filename}")
    except Exception as e:
        print(f"Lỗi: {e}")

# Sử dụng
find_longest_words('test.txt')
