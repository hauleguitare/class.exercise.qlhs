class Course:
    #Variable 
    CURRENT_YEAR = 2022
    CURRENT_YEAR_ID = 22

    def __init__(self, course, classroom):
        self.course = course
        self.classroom = classroom
        self.year_study = Course.CURRENT_YEAR

    # Method set abttribute Object Course:
    def set_course(self, course):
        self.course = course

    def set_classroom(self, classroom):
        self.classroom = classroom

    def _set_id(self, course, classroom, stt):
        self.id = "{}{}{}".format(str(self.CURRENT_YEAR_ID), self.classroom, str(stt).zfill(2))

    # Method get abttribute Object Course:
    def get_course(self):
        return self.course

    def get_classroom(self):
        return self.classroom

    def get_id(self):
        return self.id

    # Show info
    def Show_info_course(self):
        print("KHỐI: {}\nLỚP: {}\nNĂM HỌC: {}".format(self.course, self.classroom, self.CURRENT_YEAR))

    def __repr__(self):
        return '(%s, %s)' %(self.course, self.classroom)

class Course_10(Course):
    count_stt = 0
    def __init__(self, course, classroom):
        Course_10.count_stt +=1
        self.lst_course = []
        super().__init__(course, classroom)


    def _set_id(self, course, classroom, stt):
        return super()._set_id(course, classroom, stt)

    def get_id(self):
        return super().get_id()     

class Course_11(Course):
    count_stt = 0
    def __init__(self, course, classroom):
        Course_11.count_stt += 1
        self.lst_course = []
        super().__init__(course, classroom)

    def _set_id(self, course, classroom, stt):
        return super()._set_id(course, classroom, stt)

    def get_id(self):
        return super().get_id()


class Course_12(Course):
    count_stt = 0
    def __init__(self, course, classroom):
        Course_12.count_stt +=1
        self.lst_course = []       
        super().__init__(course, classroom)

    def _set_id(self, course,  classroom, stt):
        return super()._set_id(course, classroom, stt)

    def get_id(self):
        return super().get_id()
