raw_input = "   nGuyen vaN aN  ;  2004   "

while True:
    print("\n===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if not choice.isdigit() or int(choice) not in range(1, 5):
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    if choice == 1:
        print("\nChuỗi dữ liệu gốc hiện tại:")
        print(raw_input)

    elif choice == 2:
        data = raw_input.split(";")

        full_name = data[0].strip().title()
        birth_year = data[1].strip()

        current_year = 2026
        age = current_year - int(birth_year)

        print("\n[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]:")
        print(f"- Họ và tên: {full_name}")
        print(f"- Tuổi hiện tại: {age} tuổi")

    elif choice == 3:
        data = raw_input.split(";")

        full_name = data[0].strip().title()
        birth_year = data[1].strip()

        name_parts = full_name.split()

        first_name = name_parts[0]
        middle_name = name_parts[1]
        last_name = name_parts[2]

        email = (
            first_name[0].lower()
            + middle_name[0].lower()
            + last_name.lower()
            + "@company.com"
        )

        member_id = last_name.upper() + birth_year[-2:]

        print("\n====================================")
        print("         THẺ THÀNH VIÊN MỚI")
        print("====================================")
        print(f"Họ và tên : {full_name}")
        print(f"Mã ID     : {member_id}")
        print(f"Email     : {email}")
        print("====================================")

    # Chức năng 4
    elif choice == 4:
        print("Chương trình đã dừng!")
        break