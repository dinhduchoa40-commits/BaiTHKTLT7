import os

# KIỂM TRA VÀ TẠO FILE NẾU CHƯA TỒN TẠI
if not os.path.exists('Di'):
    os.makedirs('Di')
    print("Đã tạo thư mục 'Di'")

file_path = 'Di/a.txt'
if not os.path.exists(file_path):
    # Tạo file với nội dung mẫu
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("Hello World\nPython Programming\nReverse String Test\nĐảo ngược chuỗi tiếng Việt")
    print("Đã tạo file 'a.txt' với nội dung mẫu")

# CHƯƠNG TRÌNH CHÍNH - ĐỌC FILE VÀ ĐẢO NGƯỢC
try:
    input_file = open('Di/a.txt', 'r', encoding='utf-8')
    for line in input_file:
        line = line.rstrip('\n')
        l = len(line)
        s = ''
        while l >= 1:
            s = s + line[l-1]
            l = l - 1
        print(s)
    input_file.close()
    
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file Di/a.txt")
except Exception as e:
    print(f"Lỗi: {e}")
