def file_read(filename):
    try:
        # Ghi vào file
        with open(filename, 'w', encoding='utf-8') as myfile:
            myfile.write("Python Exercises\n")
            myfile.write("Java Exercises\n")
            myfile.write("Bài tập Python")
        
        # Đọc file
        with open(filename, 'r', encoding='utf-8') as txt:
            print("NỘI DUNG ĐÃ GHI:")
            print("-" * 20)
            print(txt.read())
            
    except PermissionError:
        print(f"Không có quyền ghi file: {filename}")
    except Exception as e:
        print(f"Lỗi: {e}")

# Sử dụng
file_read('abc.txt')
