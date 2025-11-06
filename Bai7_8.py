def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"Đã ghi {len(data_list)} phần tử vào file: {filename}")
        
        # Hiển thị nội dung đã ghi
        with open(filename, 'r', encoding='utf-8') as file:
            print("NỘI DUNG ĐÃ GHI:")
            print("-" * 20)
            print(file.read())
            
    except PermissionError:
        print(f"Không có quyền ghi file: {filename}")
    except Exception as e:
        print(f"Lỗi: {e}")

# Sử dụng
data = ["Python", "Java", "C++", "JavaScript", "Bài tập Python"]
write_list_to_file('list.txt', data)
