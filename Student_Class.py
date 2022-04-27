"""
Ý TƯỞNG: ÁP DỤNG TÍNH KẾ THỪA VÀ TÍNH ĐA HÌNH
- CLASS STUDENT KHỞI TẠO ĐỐI TƯỢNG:
    + THUỘC TÍNH:
        - ID
        - HỌ VÀ TÊN
        - NĂM SINH
        - KHỐI
        - ĐIỂM TRUNG BÌNH
        - XẾP LOẠI
    + PHƯƠNG THỨC:
        - HỌ VÀ TÊN HỌC SINH
        - NĂM SINH PHÂN LOẠI THEO KHỐI, 2003: LỚP 12; 2004: LỚP 11; 2005: LỚP 10
        - THỂ HIỆN THÔNG TIN HỌC SINH ĐIỂM TB VÀ XẾP LOẠI:
            + 8.0 >=: XẾP LOẠI GIỎI
            + 6.5 >= VÀ < 8.0: XẾP LOẠI KHÁ
            + 5.0 >= VÀ < 6.5: XẾP LOẠI TRUNG BÌNH
            + 3.5 >= VÀ < 5.0: XẾP LOẠI YẾU (THI LẠI CẬP NHẬT SAU)
            + < 3.5: XẾP LOẠI KÉM (LƯU BAN CẬP NHẬT SAU)
        - TỔNG SỐ HỌC SINH ĐANG HỌC

- CLASS STUDENT_10, STUDENT_11, STUDENT_12 KẾ THỪA STUDENT:
    + THUỘC TÍNH:
        - ID
        - HỌ VÀ TÊN
        - NĂM SINH
        - LỚP
        - ĐIỂM TRUNG BÌNH
        - XẾP LOẠI
    + PHƯƠNG THỨC:
        - HỌ VÀ TÊN HỌC SINH
        - CHIA LỚP THEO KHỐI
        - THỂ HIỂN THÔNG TIN HỌC SINH TRONG KHỐI VÀ XẾP LOẠI:
            + GIỎI NHẤT KHỐI
            + TẤT CẢ HỌC SINH ĐANG HỌC TRONG KHỐI
        - TỔNG SỐ HỌC SINH ĐANG HỌC

- CLASS STUDENT_ID:
    + THUỘC TÍNH:
        - ID
    + PHƯƠNG THỨC:
        - GEN ID THEO NĂM HỌC, KHỐI, LỚP VÀ SỐ THỨ TỰ
"""


from Course_Class import *
class Student:
    lst_student = []
    # Constructor Object #
    def __init__(self, id, name:str,sex:str , year_born:int, course, classroom , m_score:float):
        self.id = id
        self.name = name
        self.sex = sex
        self.year_born = year_born
        self.course = course
        self.classroom = classroom
        self.m_score = m_score
        self.rank = self.set_rank(m_score)
        self.age = int(Course.CURRENT_YEAR - year_born)


    # Method set abttribute Object:
    def set_rank(self, m_score):
        if m_score >= 8.0:
            self.rank = "GIỎI"
        elif (m_score < 8.0 and m_score >= 6.5):
            self.rank = "KHÁ"
        elif (m_score < 6.5 and m_score >= 5.0):
            self.rank = "TRUNG BÌNH"
        elif (m_score < 5.0 and m_score >= 3.5):
            self.rank = "YẾU"
        else:
            self.rank = "KÉM"
        return self.rank

    def set_name(self, name):
        self.name = name

    def set_year_born(self, year_born):
        self.year_born = year_born

    def set_sex(self, sex):
        self.sex = sex

    def set_score(self, m_score):
        self.m_score = m_score

    # Method get abttribute Object:
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_score(self):
        return self.m_score

    def get_rank(self):
        return self.rank

    # Method Show information Object:
    def show_info(self):
        print("\t\t\t- MÃ SỐ HỌC SINH: {}\n\t\t\t- TÊN HỌC SINH: {}\n\t\t\t- KHỐI: {}\n\t\t\t- LỚP: {}\n\t\t\t- ĐIỂM TRUNG BÌNH: {}\n\t\t\t- XẾP LOẠI: {}\n".format(self.id, self.name, self.course, self.classroom, self.m_score, self.rank))



hs1 = Course_12("12", "1")
hs1._set_id(hs1.course, hs1.classroom, hs1.count_stt)
hs1 = Student(hs1.get_id(),"Đoàn Ngọc Nữ", "Nữ", 2003, hs1.get_course(),hs1.get_classroom(), 3.2)
hs1.show_info()
