from Student_Class import *
from time import sleep
while True:

    print("""
    XIN CHÀO, ĐÂY LÀ ỨNG DỤNG QUẢN LÝ HỌC SINH:
        VUI LÒNG CHỌN CÁC CHỨC NĂNG SAU:
        0.  THOÁT CHƯƠNG TRÌNH
        1.  THÊM HỌC SINH
        2.  TÌM HỌC SINH
        3.  CẬP NHẬT HỌC SINH
        4.  TRA CỨU HỌC SINH THEO KHỐI (CẬP NHẬT SAU)
        5.  TỔNG SỐ HỌC SINH ĐANG HỌC
        6.  XÓA HỌC SINH
    """)
    choose = int(input("VUI LÒNG NHẬP CHỨC NĂNG SAU: "))

    # EXIT PROGRAM
    if choose == 0:
        break
    
    # THÊM HỌC SINH:
    elif choose == 1:
        add_name = input("VUI LÒNG NHẬP TÊN HỌC SINH: ")
        add_sex = input("VUI LÒNG NHẬP GIỚI TÍNH: ")
        add_year_born = int(input("VUI LÒNG NHẬP NĂM SINH: "))
        add_course = input("VUI LÒNG NHẬP KHỐI: ")
        print("""
            ĐĂNG KÝ TÊN LỚP THEO CÚ PHÁP:
                1.  C1 (C LÀ KHỐI 10)
                2.  B3 (B LÀ KHỐI 11)
                3.  A5 (A LÀ KHỐI 12)
        """)
        add_classroom = input("VUI LÒNG NHẬP LỚP: ")
        add_score = float(input("VUI LÒNG NHẬP ĐIỂM TRUNG BÌNH MÔN: "))

        if add_course == "10":
            hocsinh = Course_10(add_course, add_classroom)
            hocsinh._set_id(hocsinh.course, hocsinh.classroom, hocsinh.count_stt)
            hocsinh = Student(hocsinh.get_id(), add_name, add_sex, add_year_born, hocsinh.get_course(), hocsinh.get_classroom(), add_score)
            print("ĐÃ THÊM HỌC SINH...")
            sleep(1)
            hocsinh.show_info()
            sleep(3)   #time sleep
            hocsinh.lst_student.append(hocsinh)

        elif add_course == "11":
            hocsinh = Course_11(add_course, add_classroom)
            hocsinh._set_id(hocsinh.course, hocsinh.classroom, hocsinh.count_stt)
            hocsinh = Student(hocsinh.get_id(), add_name, add_sex, add_year_born, hocsinh.get_course(), hocsinh.get_classroom(), add_score)
            print("ĐÃ THÊM HỌC SINH...")
            sleep(1)   #time sleep
            hocsinh.show_info()
            sleep(3)   #time sleep
            hocsinh.lst_student.append(hocsinh)

        elif add_course == "12":
            hocsinh = Course_12(add_course, add_classroom)
            hocsinh._set_id(hocsinh.course, hocsinh.classroom, hocsinh.count_stt)
            hocsinh = Student(hocsinh.get_id(), add_name, add_sex, add_year_born, hocsinh.get_course(), hocsinh.get_classroom(), add_score)
            print("ĐÃ THÊM HỌC SINH...\n")
            sleep(1)   #time sleep
            hocsinh.show_info()
            sleep(3)   #time sleep
            hocsinh.lst_student.append(hocsinh)
        else:
            pass

    # TÌM HỌC SINH:
    elif choose == 2:
        while True:
            print("""
                    VUI LÒNG CHỌN CÁC CHỨC NĂNG SAU:
            0.  THOÁT RA            1.  TÌM HỌC SINH THEO MÃ SỐ
            2.  TÌM HỌC SINH THEO TÊN
            """)
            choose_find = int(input("VUI LÒNG CHỌN CHỨC NĂNG: "))
            # THOÁT RA
            if choose_find == 0:
                break
            # TÌM HỌC SINH THEO MÃ SỐ
            elif choose_find == 1:
                find_id = input("VUI LÒNG NHẬP MÃ SỐ HỌC SINH: ")
                for i in hocsinh.lst_student:
                    if i.get_id() == find_id:
                        print("ĐÃ TÌM THẤY HỌC SINH !")
                        sleep(1)
                        i.show_info()
                        sleep(3)
                        break
                else:
                    print("KHÔNG TÌM THẤY HỌC SINH TRONG DANH SÁCH.")
                    sleep(1)
            # TÌM HỌC SINH THEO TÊN
            elif choose_find == 2:
                find_name = input("VUI LÒNG NHẬP TÊN HỌC SINH: ")
                for i in hocsinh.lst_student:
                    if i.get_name() == find_name:
                        print("ĐÃ TÌM THẤY TÊN HỌC SINH !")
                        sleep(1)
                        i.show_info()
                        sleep(3)
                else:
                    print("ĐÃ TÌM HẾT !")
                    sleep(1)
    
    # CẬP NHẬT HỌC SINH:
    elif choose == 3:
        print("""
            lƯU Ý:
                - CHỈ CÓ THỂ CẬP NHẬT CÁC THÔNG TIN SAU:
            0.  THOÁT RA    1.  TÊN         2.  NĂM SINH 
            3.  GIỚI TÍNH   4.  ĐIỂM TRUNG BÌNH MÔN (HẠNH KIỂM SẼ TỰ ĐỘNG CẬP NHẬT KHI THAY ĐỔI ĐIỂM TRUNG BÌNH MÔN)
            5. TẤT CẢ
        """)
        find_id = input("VUI LÒNG NHẬP MÃ SỐ HỌC SINH: ")
        for i in hocsinh.lst_student:
            if i.get_id() == find_id:
                choose_setting_reset = int(input("VUI LÒNG CHỌN CHỨC NĂNG CẬP NHẬT: "))
                if choose_setting_reset == 0:
                    break
                
                elif choose_setting_reset == 1:
                    reset_name = input("VUI LÒNG CẬP NHẬT TÊN HỌC SINH: ")
                    i.set_name(reset_name)

                elif choose_setting_reset == 2:
                    reset_year_born = input("VUI LÒNG CẬP NHẬT NĂM SINH HỌC SINH: ")
                    i.set_year_born(reset_year_born)

                elif choose_setting_reset == 3:
                    reset_sex = input("VUI LÒNG CẬP NHẬT GIỚI TÍNH HỌC SINH: ")
                    i.set_sex(reset_sex)
                elif choose_setting_reset == 4:
                    reset_score = float(input("VUI LÒNG CẬP NHẬT ĐIỂM TRUNG BÌNH MÔN: "))
                    i.set_score(reset_score)
                    i.set_rank(reset_score)

                elif choose_setting_reset == 5:
                    i.set_name(input("VUI LÒNG CẬP NHẬT TÊN HỌC SINH: "))
                    i.set_year_born(input("VUI LÒNG CẬP NHẬP NĂM SINH HỌC SINH: "))
                    i.set_sex(input("VUI LÒNG NHẬP GIỚI TÍNH HỌC SINH: "))
                    reset_score = float(input("VUI LÒNG NHẬP ĐIỂM TRUNG BÌNH MÔN: "))
                    i.set_score(reset_score)
                    i.set_rank(reset_score)

                print("ĐANG CẬP NHẬT...")
                sleep(2)
                print("ĐÃ CẬP NHẬT!")
                sleep(0.5)
                i.show_info()
                sleep(3)
            else:
                print("KHÔNG CÓ DỮ LIỆU HỌC SINH CẦN CẬP NHẬT!")
                sleep(2)
        else:
            print("ĐÃ CẬP NHẬT XONG!")
    # TÌM TẤT CẢ HỌC SINH THEO KHỐI:
    elif choose == 4:
        pass

    # TỔNG SỐ HỌC SINH ĐANG HỌC:
    elif choose == 5:
        Sum_Student = len(hocsinh.lst_student)
        print(f"\t\tHIỆN ĐANG CÓ {Sum_Student} HỌC SINH ĐANG THEO HỌC\n")
        print("\t\tLƯU Ý: TỔNG SỐ HỌC SINH NÀY HIỆN ĐANG THEO HỌC, LƯU BAN VÀ HOÃN HỌC")
        sleep(4)

    # XÓA HỌC SINH:
    elif choose == 6:
        find_id = input("VUI LÒNG NHẬP MÃ SỐ HỌC SINH CẦN XÓA: ")
        for i in hocsinh.lst_student:
            if i.get_id() == find_id:
                i.show_info()
                sleep(1)
                print("""
                    BẠN CÓ CHẮC CHẮN XÓA DỮ LIỆU HỌC SINH NÀY KHÔNG ?

                        0.  NO                      1.  YES
                """)
                choose_del = int(input("VUI LÒNG CHỌN: "))
                if choose_del == 0:
                    break
                elif choose_del == 1:
                    hocsinh.lst_student.remove(i)
                    sleep(1.5)
                    print("ĐÃ XÓA THÀNH CÔNG!")
                    sleep(3)
        
    


