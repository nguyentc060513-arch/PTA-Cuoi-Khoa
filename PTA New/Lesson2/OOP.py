'''
    - Lập trình hướng đối tượng OOP (OOP: Object-oriented Programming):
Là một phương pháp lập trình trong đó mọi thứ được thể hiện dưới dạng
đối tượng. OOP chú trọng vào viêck tạo ra các đối tượng có khả năng
chứa dữ liệu (Thuộc tính) và các hành vi, hành động (Phương thức) liên
quan tới dữ liệu đó. Giúp quản lý các đoạn mã dễ dàng hơn và có thể
tái sử dụng
    - Đối tượng (Object): Đối tượng là thực thể cụ thể của 1 lớp (class)
Nó chứa dữ liệu thuộc tính (Acttribute) và có thể thực hiện các hành 
động thông qua phương thức (Method - def)
'''
class Dog: # Tạo 1 đối tượng (Object) Dog
    # Phương thức khởi tạo
    def __init__(self, name, age, color, talk): # Tham số 
        # Tạo thuộc tính (Acttribute)
        self.name = name
        self.age = age
        self.color = color
        self.talk = talk

    # Phương thức (Method)
    def new_dog(self):
        print(f"{self.name}, {self.age}, {self.color}")
    def Speak(self):
        print(f"{self.talk}")

# Truyền giá trị và gọi đối tượng 
my_dog = Dog("Chó cỏ", "1000", "red", "Go Go Go")

my_dog.new_dog()
my_dog.Speak()

'''
    - Thuộc tính (Attribute): Là dữ liệu mà đối tượng của lớp (class) 
chứa VD: self.name, self.age,...
    - Phương thức (Method): Phương thức là hàm định nghĩa đặc biệt 
của lớp (Class) VD: new_dog(), Speak() - tên phương thức không được
trung tên với tham số truyền vào
    - Phương thức khởi tạo (__init__): Là 1 phương thức đặc biệt 
được gọi tự động khi đối tượng mới được tạo ra. Được sử dụng để 
tạo các thuộc tính của đối tượng
    - Từ khóa "self": Là 1 tham số tham chiếu tới đối tượng hiện tại
(Luôn được sử dụng và khai báo trong các phương thức)
    - Tham số: Các biến số được khai báo để nhận dữ liệu từ bên ngoài,
Và truyền dữ liệu vào trong class đó. 
'''

'''
  Tạo ra 1 lớp Dien_thoai nêu ra các 
    - Attrbutes mau_sac, thuong_hieu, gia_ban, so_dien_thoai
    - Tạo 1 method hiển thị thông tin 
'''
class Dien_thoai():
    def __init__(self, mau_sac, thuong_hieu, gia_ban, so_dien_thoai):
        self.mau_sac = mau_sac
        self.thuong_hieu = thuong_hieu
        self.gia_ban = gia_ban
        self.so_dien_thoai = so_dien_thoai
    
    def hien_thi_thong_tin(self):
        print("Thông tin điện thoại: ")
        print(f"Màu sắc: {self.mau_sac}")
        print(f"Thương hiệu: {self.thuong_hieu}")
        print(f"Giá bán: {self.gia_ban}")
        print(f"SĐT: {self.so_dien_thoai}")

phone1 = Dien_thoai("Đen", "Sam sum", "1 Tỷ", "012345789")
phone2 = Dien_thoai("Trắng", "Ốp pồ", "2 Tỷ", "012345789")

phone1.hien_thi_thong_tin()
phone2.hien_thi_thong_tin()

'''
Tạo một lớp hoc_sinh gồm dia_chi, chieu_cao, can_nang, hoc_luc
Tạo các phương thức : Show()
                      Update_address()
                      Update_health()
'''
class hoc_sinh():
    def __init__(self, dia_chi, chieu_cao, can_nang, hoc_luc):
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc
    
    def Show(self):
        print("Hiển thị thông tin: ")
        print(f"Địa chỉ hs: {self.dia_chi}")
        print(f"Chiều Cao: {self.chieu_cao}")
        print(f"Cân nặng: {self.can_nang}")
        print(f"Học lực: {self.hoc_luc}")
    
    def  Update_address(self):
        self.dia_chi = input("Nhập địa chỉ mới: ")

    def Update_health(self):
        self.chieu_cao = float(input("Nhập chiều cao mới: "))
        self.can_nang = float(input("Nhập cân nặng mới: "))

Hoc_sinh = hoc_sinh("Hà Lội", "1,6m", "52kg", "Dốt")
Hoc_sinh.Show()
Hoc_sinh.Update_address()
Hoc_sinh.Update_health()