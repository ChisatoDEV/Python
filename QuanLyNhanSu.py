# quản lý nhân sự project
import time, os
# data containing data


data_nhansu = []

data_chucvu = [
    {
        "id": 1,
        "chucvu": "Nhân viên",
        "luong": 1000000
    },
    {
        "id": 2,
        "chucvu": "Trưởng Phòng",
        "luong": 1500000
    },
    {
        "id": 3,
        "chucvu": "Quản lý",
        "luong": 2000000
    }
]

data_phongban = ['Phòng công nghệ', 'Phòng thông tin', 'Phòng Quản lý'];

# choice chuc vu
def choice_chucvu():
    for x in data_chucvu:
        for key, value in x.items():
            if key == "id": print(value, end=" ")
            if key == "chucvu": print('=>', value)
    choice = int(input("Nhập số: "))
    if(str(choice).isnumeric()):
        return choice
    else:
        return False

# choice phong ban
def choice_phongban():
    i = 0
    while (i < len(data_phongban)):
        print(i + 1 ,'=>', data_phongban[i])
        i += 1
    choice = int(input("Nhập số: "))
    if(str(choice).isnumeric()):
        return choice
    else:
        return False
# function to show menu
def show_menu ():
    Menu = {
        1: "Thêm nhân sự",
        2: "Xem danh sách nhân sự",
        3: "Sửa thông tin nhân sự",
        4: "Tính lượng"
    }
    for x, y in Menu.items():
        print(x, '=>', y)
    
    # input choice
    try:
        choice = int(input("Nhập lựa chọn của bạn: "))
        return choice
    except:
        return False

# function return the nhansu
def get_nhansu ():
    check_rule = False
    check_length = lambda str, num: len(str) > num

    ho = input("Nhập họ: ")
    ten = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    gioitinh = input("Nhập giới tính (nam/nu): ").upper()

    if gioitinh == "NAM":
        gt = 1
    else:
        gt = 2

    chucvu = choice_chucvu()
    phongban = choice_phongban()

    if(check_length(ho, 2) == False):
        print("Họ phải có độ dài lớn hơn 10 ký tự")
        check_rule = True
    if(check_length(ten, 5) == False):
        print("Tên phải có độ dài lớn hơn 10 ký tự")
        check_rule = True
    if(str(age).isnumeric() == False):
        print("Tuổi phải là số")
        check_rule = True
    if(str(gt).isnumeric() == False):
        print("Lỗi đặt giới tính cho bạn")
        check_rule = True
    if(chucvu == False):
        print("Lỗi chọn chức vụ")
        check_rule = True
    if(phongban == False):
        print("Lỗi chọn phòng ban")
        check_rule = True
    
    if(check_rule):
        return False
    else:
        return {
            "ho": ho,
            "ten": ten,
            "hovaten": ho + ' ' + ten,
            "age": age,
            "gioitinh": gt,
            "chucvu": chucvu-1,
            "phongban": phongban-1
        }

# print a data nhansu
def print_nhansu(data_nhansu, hideluong=False):
    os.system('cls')
    print('='*30)
    i = 0
    while i < len(data_nhansu):
        nhansu = data_nhansu[i]
        if nhansu['gioitinh'] == 1: gt = 'Nam' 
        else: gt = 'Nữ'
        if hideluong:
            print(i + 1, '=>',
                'Họ:', nhansu['ho'], '|',
                'Tên:', nhansu['ten'], '|',
                'Họ và tên:', nhansu['hovaten'], '|',
                'Tuổi:', nhansu['age'], '|',
                'Giới tính:', gt, '|',
                'Chức vụ:', data_chucvu[nhansu['chucvu']]['chucvu'], '|',
                'Phòng ban:', data_phongban[nhansu['phongban']],
                'Lương: ', nhansu['luong']
            )
        else:
            print(i + 1, '=>',
                'Họ:', nhansu['ho'], '|',
                'Tên:', nhansu['ten'], '|',
                'Họ và tên:', nhansu['hovaten'], '|',
                'Tuổi:', nhansu['age'], '|',
                'Giới tính:', gt, '|',
                'Chức vụ:', data_chucvu[nhansu['chucvu']]['chucvu'], '|',
                'Phòng ban:', data_phongban[nhansu['phongban']]
            )
        i += 1
    print('='*30)

# print the sort function
def print_sort():
    MenuSort = {
                    1: 'Nhỏ đến lớn',
                    2: 'Lớn đến nhỏ'
                }
    for x, y in MenuSort.items():
        print(x, '=>', y)

# function return list nhansu
def get_list_nhansu():
    check_close = False
    while True:
        clonenhansu = data_nhansu.copy()
        while True:
            print_nhansu(clonenhansu)
            listMenu = {
                    1: "Sắp xếp tên",
                    2: "Sắp xếp tuổi",
                    3: "Sắp xếp giới tính",
                    4: "Sắp xếp chức vụ"
                }
            for x, y in listMenu.items():
                print('','|',x,':',y,end='')
            print(' | ')
            choice = int(input("Nhập lựa chọn của bạn (nhập 0 để thoát): "))
            if (choice == 0):
                check_close = True
                break
            elif (choice == 1):
                print_sort()
                choice = int(input("Nhập số: "))
                if choice == 1:
                    clonenhansu.sort(key=lambda x: x['hovaten'])
                else:
                    clonenhansu.sort(reverse=True,key=lambda x: x['hovaten'])
            elif (choice == 2):
                print_sort()
                choice = int(input("Nhập số: "))
                if choice == 1:
                    clonenhansu.sort(key=lambda x: x['age'])
                else:
                    clonenhansu.sort(reverse=True, key=lambda x: x['age'])
            elif (choice == 3):
                print_sort()
                choice = int(input("Nhập số: "))
                if choice == 1:
                    clonenhansu.sort(key=lambda x: x['gioitinh'])
                else:
                    clonenhansu.sort(reverse=True, key=lambda x: x['gioitinh'])
            elif (choice == 4):
                print_sort()
                choice = int(input('Nhập số: '))
                if choice == 1:
                    clonenhansu.sort(key=lambda x: data_chucvu[x['chucvu']]['id'])
                else:
                    clonenhansu.sort(reverse=True, key=lambda x: data_chucvu[x['chucvu']]['id'])
            else:
                print("Bạn nhập gì thế?")
                time.sleep(2000)
            
        if check_close:
            break
# edit profile nhansu
def edit_profile():
    while True:
        checkActive = False
        while True:
            print_nhansu(data_nhansu)
            stt = int(input("Nhập stt nhân sự cần sửa ( nhap 0 nếu muốn thoát): ")) - 1
            if stt < 0: checkActive = True; break
            nhansu = data_nhansu[stt]
            print('='*30)
            print('Tên nhân sự đang sử:', nhansu['hovaten'])
            print('='*30)
            MenuEdit = {
                1: 'Họ',
                2: 'Tên',
                3: 'Tuổi',
                4: 'Giới tính',
                5: 'Chức vụ',
                6: 'Phòng ban'
            }
            for x, y in MenuEdit.items():
                print(x, '=>', y)
            choice = int(input("Nhập lựa chọn của bạn (nhập 0 để thoát): "))
            if (choice == 0):
                checkActive = True
                break
            elif (choice == 1):
                ho = input("Nhập họ: ")
                nhansu['ho'] = ho
            elif (choice == 2):
                ten = input("Nhập tên: ")
                nhansu['ten'] = ten
            elif (choice == 3):
                age = int(input("Nhập tuổi: "))
                nhansu['age'] = age
            elif (choice == 4):
                gioitinh = int(input("Nhập giới tính (1=nam, 2=nu): "))
                nhansu['gioitinh'] = gioitinh
            elif (choice == 5):
                chucvu = choice_chucvu()
                nhansu['chucvu'] = chucvu
            elif (choice == 6):
                phongban = choice_phongban()
                nhansu['phongban'] = phongban
            else:
                print('Không tồn tại!')
            data_nhansu[stt] = nhansu
        if (checkActive):
                break

# tinh luong can ban
def tinh_luong_canhan(days, onlyPhongBan = 'all'):
    tongluong = 0
    nhansu_clone = []
    for x in data_nhansu:
        luong_goc = data_chucvu[nhansu['chucvu']]['luong']
        luong_1_ngay = luong_goc / 30
        luong_tinh = round(luong_1_ngay * days)
        if (onlyPhongBan == 'all'):
            x['luong'] = luong_tinh
            tongluong += luong_tinh
            nhansu_clone.append(x)
        else:
            if data_phongban[x['phongban']] == onlyPhongBan:
                x['luong'] = luong_tinh
                tongluong += luong_tinh
                nhansu_clone.append(x)
    print_nhansu(nhansu_clone,True)
    print('Tổng lương của các nhân sự: ', tongluong)
    input('Nhấn enter để tiếp tục...')

# tính lương phòng ban
def tinh_luong_phongban(days):
    i = 0
    while i < len(data_phongban):
        print(i+1, '=>', data_phongban[i])
        i += 1
    choice = int(input('Nhập số phòng ban cần tính lương: '))
    phongban = data_phongban[choice-1]
    tinh_luong_canhan(days, phongban)

# tinh luong
def tinh_luong():
    while True:
        checkActive = False
        while True:
            os.system('cls')
            days = int(input('Bạn muốn tính lương của bao nhiêu ngày?: '))
            if (days > 0):

                MenuTinhLuong = {
                    1: 'Tính lương cá nhân',
                    2: 'Tính lương phòng ban'
                }

                for x, y in MenuTinhLuong.items():
                    print(x, '=>', y)
                choice = int(input("Nhập lựa chọn của bạn (nhập 0 để thoát): "))
                if choice == 0: checkActive = True; break
                else:
                    if choice == 1:
                        tinh_luong_canhan(days)
                    elif choice == 2:
                        tinh_luong_phongban(days)
            else:
                print('Không được nhỏ hơn 0')
        if checkActive:
            break



# start program
while True:
    os.system('cls')
    # show the menu
    choice = show_menu()
    if str(choice).isnumeric() == True:
        if (choice == 1):
            nhansu = get_nhansu()
            if (nhansu == False):
                print("Lỗi nhập thông tin")
            else:
                data_nhansu.append(nhansu)
                print("Thêm thành công")
                time.sleep(2)
        elif (choice == 2):
            get_list_nhansu()
        elif (choice == 3):
            edit_profile()
        elif (choice == 4):
            tinh_luong()
    else:
        print("Không hợp lệ")
