def count_file_stats(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            char_count = 0
            word_count = 0
            line_count = 0
            
            for line in file:
                line_count += 1
                char_count += len(line)
                word_count += len(line.split())
            
            print(f"Số ký tự: {char_count}")
            print(f"Số từ: {word_count}")
            print(f"Số dòng: {line_count}")
            
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
    except PermissionError:
        print(f"Không có quyền truy cập file: {filename}")
        print("Hãy đặt file trong thư mục dự án của bạn")
    except Exception as e:
        print(f"Lỗi: {e}")

# Tạo file test.txt trong thư mục hiện tại để demo
def create_sample_file():
    try:
        with open('test.txt', 'w', encoding='utf-8') as f:
            f.write("Hello world\n")
            f.write("Python programming\n")
            f.write("Đây là bài tập Python\n")
            f.write("Count characters, words and lines")
        print("Đã tạo file test.txt mẫu")
    except:
        pass

# Sử dụng
create_sample_file()  # Tạo file mẫu nếu chưa có
print("=== KẾT QUẢ ĐẾM FILE ===")
count_file_stats('test.txt')  # Dùng file trong thư mục hiện tại
