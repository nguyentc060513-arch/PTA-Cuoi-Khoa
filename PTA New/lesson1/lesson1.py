'''
     1. Biến số
       - Sử dụng lưu trữ giá trị dữ liệu 
       - Quy tắc đặt tên: Tên không bắt đầu bằng số, không đặt trùng với câu lệnh của
       ngôn ngữ, không có ký tự đặc biệt. 
       Vd: isName = "Hưng"
     2. Kiểu dữ liệu (Nguyên thủy)
        - integer - int: Số Nguyên 
        - float: Số thực 
        - Boolean: Logic
        - String-str: Kiểu chuỗi 
        - type(): Kiểu tra kiểu dữ liệu
     3. Đầu ra - đầu vào 
        - print(): Đầu ra
        - input(): Đầu vào
     4. Toán tử 
        - Toán tử số học (+, -, *, /, %, //)
        - Toán tử gán (=, +=, -=, *=, /=, %=, //=)
        - Toán tử Logic (and, or, not)
        - Toán tử so sánh (<, >, <=, >=, ==, !=)
     5. Câu lệnh điều kiện rẽ nhánh 
        Th1: 1 điều kiện : if
        Th2: 1 điều kiện và phần còn lại: if else
        Th3: Nhiều điều kiện và phần còn lại 
     6. Vòng lặp 
        - Vòng lặp for: Lặp qua danh sách để lấy giá trị 
        - Vòng while: Lặp qua các chương trình
     7. Hàm 
        - Tạo ra khối chức năng có thể tái sử dụng bằng cách gọi tên 
     8. List 
        - index: Xác định vị trí và thứ tự, bắt đầu từ 0
        -item: Phần tử được khai báo trong list,có thể là bất cứ kiểu dữ liệu nào
     9. String
'''
'''
   - Nhập 3 cạnh a, b, c 
   - Tạo hàm kiểm tra tam giác 
        + Cân
        + Vuông
        + Đều
        + Tam giác thường
        + Không phải tam giác 
'''
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

def check(a, b, c):
    if a >= b+ c or b >= a +c or c >= a + b:
        print("Không phải tam giác")
    elif a == b or a == c or c == b:
        print("Tam giác cân")
    elif a == b == c:
        print("Tam giác đều")
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
check(a, b,c)