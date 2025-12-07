from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt6 import uic #Sử dụng để tải giao diện
from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl # Lấy đường dẫn
from PyQt6.QtGui import QDesktopServices # Mở trang web
import sys # Mở Terminal
import json
import os
ACCOUNT_FILE = "app_account.json"

def load_accounts():
    # Tạo file nếu chưa có
    if not os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, "w", encoding="utf-8") as f:
            json.dump({"users": {}}, f, indent=4)
    
    with open(ACCOUNT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Nếu file không có "users" thì tự chuyển đổi
    if "users" not in data:
        # Chuyển toàn bộ cặp key:value thành users
        new_data = {"users": data}
        save_accounts(new_data)
        return new_data

    return data


def save_accounts(data):
    with open(ACCOUNT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# Tạo biến số global
register_users = {}

# Tạo giao diện Login 
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./Lesson3/UI/Login.ui", self)

        # Tạo sự kiện nhấn nút bt_createAccount
        self.bt_SignUp.clicked.connect(self.ShowRegister)
        # Tạo sự kiện nhấn nut bt_Login
        self.bt_Login.clicked.connect(self.CheckLogin)

    # Phương thức hành động của ShowRegister
    def ShowRegister(self):
        RegisterPage.show() # Hiển thị page 
        self.close() # Câu lệnh đóng page

    # Phương thức hành động kiểm tra đăng nhập (CheckLogin)
    def CheckLogin(self):
        data = load_accounts()
        users = data["users"]

        userName = self.le_Lg_email.text().strip()
        password = self.le_Lg_password.text().strip()
        msgBox = QMessageBox()

        if not userName or not password:
            msgBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin")
            return

        if userName in users and users[userName] == password:
            msgBox.information(self, "Thông báo", "Đăng nhập thành công")
            MenuPage.show()
            self.close()
            return

        # Tài khoản mặc định
        if userName == "1" and password == "1":
            msgBox.information(self, "Thông báo", "Đăng nhập thành công")
            MenuPage.show()
            self.close()
            return

        msgBox.warning(self, "Lỗi", "Sai tài khoản hoặc mật khẩu!")

    
    # Tài khoản mặc định
        if userName == "1" and password == "1":
            msgBox.information(self, "Thông báo", "Đăng nhập thành công")
            MenuPage.show()
            self.close()
            return
        msgBox.warning(self, "Lỗi", "Sai tài khoản hoặc mật khẩu!")


# Tạo giao diện Register
class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./Lesson3/UI/SignUp.ui", self)

        self.data = load_accounts()
        self.users = self.data["users"]

        self.bt_SignUp.clicked.connect(self.CheckRegister)
        self.bt_Login.clicked.connect(self.OpenLogin)

        # Kiểm tra mật khẩu realtime
        self.le_password.textChanged.connect(self.checkPasswordStrength)
        

    def OpenLogin(self):
        LoginPage.show()
        self.close()

    def checkPasswordStrength(self):
        password = self.le_password.text()

        # Điều kiện để tính độ mạnh
        length_ok = len(password) >= 8
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit  = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()-_=+[]{};:,<.>/?|" for c in password)

        strength = 0
        for cond in [length_ok, has_upper, has_lower, has_digit, has_special]:
            if cond:
                strength += 1

        # Hiển thị trạng thái
        if len(password) == 0:
            self.lb_passwordStatus.setText("")

        elif strength <= 2:
            self.lb_passwordStatus.setText("Mật khẩu yếu")
            self.lb_passwordStatus.setStyleSheet("color: red;")

        elif strength == 3 or strength == 4:
            self.lb_passwordStatus.setText("Mật khẩu trung bình")
            self.lb_passwordStatus.setStyleSheet("color: orange;")

        else:
            self.lb_passwordStatus.setText("Mật khẩu mạnh")
            self.lb_passwordStatus.setStyleSheet("color: green;")

    def get_strength(self, pw):
        """Trả về mức độ mạnh của mật khẩu"""
        length = len(pw)
        has_upper = any(c.isupper() for c in pw)
        has_lower = any(c.islower() for c in pw)
        has_digit = any(c.isdigit() for c in pw)
        has_special = any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for c in pw)

        # Yếu: < 6 ký tự hoặc chỉ toàn chữ
        if length < 6:
            return "weak"

        # Trung bình: có chữ + số nhưng chưa đủ mạnh
        if (has_lower or has_upper) and has_digit and not has_special:
            return "medium"

        # Mạnh: có đầy đủ chữ hoa + chữ thường + số + kí tự đặc biệt
        if has_upper and has_lower and has_digit and has_special and length >= 8:
            return "strong"

        return "medium"

    # ------------------------------
    # CHECK REGISTER
    # ------------------------------
    def CheckRegister(self):
        userName = self.le_email.text().strip()
        password = self.le_password.text()
        RePass  = self.le_retypePassword.text()
        msgBox = QMessageBox()

        # Kiểm tra đầy đủ
        if not userName or not password or not RePass:
            msgBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return

        # Tài khoản tồn tại
        if userName in self.users:
            msgBox.warning(self, "Lỗi", "Tài khoản đã được sử dụng!")
            return

        # Kiểm tra trùng mật khẩu
        if password != RePass:
            msgBox.warning(self, "Lỗi", "Mật khẩu không trùng!")
            return

        # Lấy cấp độ mật khẩu
        strength = self.get_strength(password)

        if strength == "weak":
            msgBox.warning(self, "Lỗi", "Mật khẩu quá yếu! (Tối thiểu 6 ký tự)")
            return

        if strength == "medium":
            msgBox.warning(self, "Lỗi", "Mật khẩu trung bình – hãy thêm ký tự đặc biệt để mạnh hơn.")
            return

        # Lưu tài khoản
        self.users[userName] = password
        save_accounts(self.data)

        msgBox.information(self, "Thành công", "Đăng ký thành công!")

class Article1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./Lesson3/UI/Firstarticle.ui", self)
        self.pb_menu.clicked.connect(self.OpenMenu)
        self.pb_logout.clicked.connect(self.Logout)
        self.pb_contact.clicked.connect(self.OpenContact)
        self.pb_back.clicked.connect(self.Back)
        self.pb_buy1.clicked.connect(self.Buy1)
        self.pb_buy2.clicked.connect(self.Buy2)
        self.pb_buy3.clicked.connect(self.Buy3)
    def OpenContact(self):
        ContactPage.show()
        self.close()
    def OpenMenu(self):
        MenuPage.show()
        self.close()
    def Logout(self):
        LoginPage.show()
        self.close()
    def Back(self):
        MenuPage.show()
        self.close()
    def Buy1(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab sản phẩm")
        url = "https://shopee.vn/search?keyword=gi%E1%BA%A5y%20vi%E1%BA%BFt%20th%C6%B0%20cho%20%C3%B4ng%20gi%C3%A0%20noel%2C%20gi%C3%A1ng%20sinh" 
        QDesktopServices.openUrl(QUrl(url))
    def Buy2(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab sản phẩm")
        url = "https://shopee.vn/search?keyword=thi%E1%BB%87p%20gi%C3%A1ng%20sinh%20tu%E1%BA%A7n%20l%E1%BB%99c" 
        QDesktopServices.openUrl(QUrl(url))
    def Buy3(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab sản phẩm")
        url = "https://shopee.vn/search?keyword=thi%E1%BB%87p%20gi%C3%A1ng%20sinh%20%C3%B4ng%20gi%C3%A0%20noel" 
        QDesktopServices.openUrl(QUrl(url))
class Contact(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./Lesson3/UI/Contact.ui", self)
        self.pb_menu.clicked.connect(self.OpenMenu)
        self.pb_logout.clicked.connect(self.Logout)
        self.pb_show_web.clicked.connect(self.ShowChannel)
    def ShowChannel(self):
        url = "https://www.youtube.com/@PokoTryHard"
        QDesktopServices.openUrl(QUrl(url))
    def OpenMenu(self):
        MenuPage.show()
        self.close()
    def Logout(self):
        LoginPage.show()
        self.close()
class Article2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./Lesson3/UI/Secondarticle.ui", self)
        self.pb_menu.clicked.connect(self.OpenMenu)
        self.pb_logout.clicked.connect(self.Logout)
        self.pb_contact.clicked.connect(self.OpenContact)
        self.pb_back.clicked.connect(self.Back)
    def OpenContact(self):
        ContactPage.show()
        self.close()
    def OpenMenu(self):
        MenuPage.show()
        self.close()
    def Logout(self):
        LoginPage.show()
        self.close()
    def Back(self):
        MenuPage.show()
        self.close()
class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./Lesson3/UI/Menu.ui", self)
        self.pb_contact.clicked.connect(self.Contact)
        self.pb_logout.clicked.connect(self.Logout)
        self.pb_buy1.clicked.connect(self.Buy1)
        self.pb_buy2.clicked.connect(self.Buy2)
        self.pb_buy3.clicked.connect(self.Buy3)
        self.pb_watch1.clicked.connect(self.Watch1)
        self.pb_watch2.clicked.connect(self.Watch2)
        self.pb_watch3.clicked.connect(self.Watch3)
        self.pb_watch4.clicked.connect(self.Watch4)
        self.pb_watch5.clicked.connect(self.Watch5)
        self.pb_watch6.clicked.connect(self.Watch6)
    def Logout(self):
        LoginPage.show()
        self.close()
    def Contact(self):
        ContactPage.show()
        self.close()
    def Buy1(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab sản phẩm")
        url = "https://shopee.vn/search?keyword=gi%E1%BA%A5y%20vi%E1%BA%BFt%20th%C6%B0%20cho%20%C3%B4ng%20gi%C3%A0%20noel%2C%20gi%C3%A1ng%20sinh" 
        QDesktopServices.openUrl(QUrl(url))
    def Buy2(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab sản phẩm")
        url = "https://shopee.vn/search?keyword=thi%E1%BB%87p%20gi%C3%A1ng%20sinh%20tu%E1%BA%A7n%20l%E1%BB%99c" 
        QDesktopServices.openUrl(QUrl(url))
    def Buy3(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab sản phẩm")
        url = "https://shopee.vn/search?keyword=thi%E1%BB%87p%20gi%C3%A1ng%20sinh%20%C3%B4ng%20gi%C3%A0%20noel" 
        QDesktopServices.openUrl(QUrl(url))
    def Watch1(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab bộ phim")
        url = "https://www.rophim.li/xem-phim/o-nha-mot-minh.OG1Hi1?ver=1" 
        QDesktopServices.openUrl(QUrl(url))
    def Watch2(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab bộ phim")
        url = "https://www.phimconggiao.com/do-la-mot-cuoc-song-ky-dieu/xem-phim/10186" 
        QDesktopServices.openUrl(QUrl(url))
    def Watch3(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab bộ phim")
        url = "https://www.rophim.li/xem-phim/giang-sinh-cua-cau-chuyen-giang-sinh.GtkoM1?ver=1" 
        QDesktopServices.openUrl(QUrl(url))
    def Watch4(self):
        msgBox = QMessageBox()
        msgBox.information(self, "Lỗi", f"Đang di chuyển đến tab bộ phim")
        url = "https://www.youtube.com/watch?v=Xr_U0ZorJ74" 
        QDesktopServices.openUrl(QUrl(url))
    def Watch5(self):
        FirstA.show()
        self.close()
    def Watch6(self):
        SecondA.show()
        self.close()
# Gọi giao diện 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    LoginPage = Login()
    RegisterPage = Register()
    MenuPage = Menu()
    FirstA = Article1()
    SecondA = Article2()
    ContactPage = Contact()
    LoginPage.show()
    sys.exit(app.exec())