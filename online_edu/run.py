
from classes import Student, Admin, CourseStatus, Language, Speciality, SpecialityCourse, LessonStatus, Lesson, Course, \
    Module, Comment, Payment


def course_status_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(CourseStatus.select("course_status")) == 0:
            print("Data not yet exist!")

        else:
            for i in CourseStatus.select("course_status"):
                print(f"""
                            ID: {i[0]},
                            Name: {i[1]},
                            Create date: {i[2]},
                        """)

        return course_status_table()

    elif services == "2":  # INSERT
        name = input("Name: ")
        name = CourseStatus(name)
        print(name.insert("course_status"))
        return course_status_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: course_status_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "course_status_id":
            print(CourseStatus.update_id("course_status", column_name, old_data, new_data))
        else:
            print(CourseStatus.update("course_status", column_name, old_data, new_data))

        return course_status_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: color_status_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(CourseStatus.delete_id("color_status", value))
        else:
            print(CourseStatus.delete("color_status", column_name, value))
        return course_status_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return course_status_table()


def language_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(Language.select("language")) == 0:
            print("Data not yet exist!")

        else:
            for i in Language.select("language"):
                print(f"""
                            ID: {i[0]},
                            Name: {i[1]},
                            Last Updated: {i[2]},
                            Create date: {i[3]},
                        """)

        return language_table()

    elif services == "2":  # INSERT
        name = input("Name: ")
        name = Language(name)
        print(name.insert("language"))
        return language_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: language_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "language_id":
            print(Language.update_id("language", column_name, old_data, new_data))
        else:
            print(Language.update("language", column_name, old_data, new_data))

        return language_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: language_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(Language.delete_id("language", value))
        else:
            print(Language.delete("language", column_name, value))
        return language_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return language_table()


def speciality_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(Speciality.select("speciality")) == 0:
            print("Data not yet exist!")

        else:
            for i in Speciality.select("speciality"):
                print(f"""
                            ID: {i[0]},
                            Name: {i[1]},
                            Create date: {i[2]},
                        """)

        return speciality_table()

    elif services == "2":  # INSERT
        name = input("Name: ")
        name = Speciality(name)
        print(name.insert("speciality"))
        return speciality_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name (ID: speciality_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "speciality_id":
            print(Speciality.update_id("speciality", column_name, old_data, new_data))
        else:
            print(Speciality.update("speciality", column_name, old_data, new_data))

        return speciality_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: speciality_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(Speciality.delete_id("speciality", value))
        else:
            print(Speciality.delete("speciality", column_name, value))
        return speciality_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return speciality_table()


def lesson_status_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(LessonStatus.select("lesson_status")) == 0:
            print("Data not yet exist!")

        else:
            for i in LessonStatus.select("lesson_status"):
                print(f"""
                            ID: {i[0]},
                            Name: {i[1]},
                            Create date: {i[2]},
                        """)

        return lesson_status_table()

    elif services == "2":  # INSERT
        name = input("Name: ")
        name = LessonStatus(name)
        print(name.insert("lesson_status"))
        return lesson_status_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: lesson_status_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "lesson_status_id":
            print(LessonStatus.update_id("lesson_status", column_name, old_data, new_data))
        else:
            print(LessonStatus.update("lesson_status", column_name, old_data, new_data))

        return lesson_status_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: lesson_status_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(LessonStatus.delete_id("lesson_status", value))
        else:
            print(LessonStatus.delete("lesson_status", column_name, value))
        return lesson_status_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return lesson_status_table()


def course_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(Course.select("course")) == 0:
            print("Data not yet exist!")

        else:
            for i in Course.select("course"):
                print(f"""
                            ID: {i[0]},
                            Name: {i[1]},
                            Description: {i[2]},
                            Rating: {i[3]},
                            Active Students: {i[4]},
                            Admin ID: {i[5]},
                            Language ID: {i[6]},
                            Price: {i[7]},
                            Course Status ID: {i[8]},
                            Support Date: {i[9]},
                            Last Updated: {i[10]},
                            Create date: {i[11]},
                        """)

        return course_table()

    elif services == "2":  # INSERT
        name = input("Name: ")
        description = input("Description: ")
        rating = float(input("Rating: "))
        active_students = int(input("Active students: "))
        admin_id = int(input("Admin ID: "))
        language = int(input("Language ID: "))
        price = int(input("Price: "))
        course_status = int(input("Course status ID: "))
        support_date = input("Support Date: ")

        name = Course(name, description, rating, active_students, admin_id, language, price, course_status,
                      support_date)
        print(name.insert("course"))
        return course_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: course_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "course_id":
            print(Course.update_id("course", column_name, old_data, new_data))
        else:
            print(Course.update("course", column_name, old_data, new_data))

        return course_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: course_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(Course.delete_id("course", value))
        else:
            print(Course.delete("course", column_name, value))
        return course_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return course_table()


def speciality_course_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(SpecialityCourse.select("speciality_course")) == 0:
            print("Data not yet exist!")

        else:
            for i in SpecialityCourse.select("speciality_course"):
                print(f"""
                            ID: {i[0]},
                            Speciality ID: {i[1]},
                            Course ID: {i[2]},
                            Create date: {i[3]},
                        """)

        return speciality_course_table()

    elif services == "2":  # INSERT
        speciality_id = int(input("Speciality ID: "))
        course_id = int(input("Course ID: "))
        name = SpecialityCourse(speciality_id, course_id)
        print(name.insert("speciality_course"))
        return speciality_course_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: speciality_course_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "speciality_course_id":
            print(SpecialityCourse.update_id("speciality_course", column_name, old_data, new_data))
        else:
            print(SpecialityCourse.update("speciality_course", column_name, old_data, new_data))

        return speciality_course_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: speciality_course_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(SpecialityCourse.delete_id("speciality_course", value))
        else:
            print(SpecialityCourse.delete("speciality_course", column_name, value))
        return speciality_course_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return speciality_course_table()


def module_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(Module.select("module")) == 0:
            print("Data not yet exist!")

        else:
            for i in Module.select("module"):
                print(f"""
                            ID: {i[0]},
                            Name: {i[1]},
                            Course ID: {i[2]},
                            Lesson Count: {i[3]},
                            Last Updated: {i[4]},
                            Create date: {i[5]},
                        """)

        return module_table()

    elif services == "2":  # INSERT
        name = input("Name: ")
        course_id = int(input("Course ID: "))
        lesson_count = int(input("Lesson Count: "))
        last_update = input("Last Updated: ")
        name = Module(name, course_id, lesson_count, last_update)
        print(name.insert("module"))
        return module_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: module_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "module_id":
            print(Module.update_id("module", column_name, old_data, new_data))
        else:
            print(Module.update("module", column_name, old_data, new_data))

        return module_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: module_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(Module.delete_id("module", value))
        else:
            print(Module.delete("module", column_name, value))
        return module_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return module_table()


def lesson_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(Lesson.select("lesson")) == 0:
            print("Data not yet exist!")

        else:
            for i in Lesson.select("lesson"):
                print(f"""
                            ID: {i[0]},
                            Name: {i[1]},
                            Description: {i[2]},
                            Lesson Status ID: {i[3]},
                            Module ID: {i[4]},
                            Create date: {i[5]},
                        """)

        return lesson_table()

    elif services == "2":  # INSERT
        name = input("Name: ")
        description = input("Description: ")
        lesson_status_id = int(input("Lesson Status ID: "))
        module_id = int(input("Module ID: "))
        name = Lesson(name, description, lesson_status_id, module_id)
        print(name.insert("lesson"))
        return lesson_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: lesson_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "lesson_id":
            print(Lesson.update_id("lesson", column_name, old_data, new_data))
        else:
            print(Lesson.update("lesson", column_name, old_data, new_data))

        return lesson_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: lesson_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(Lesson.delete_id("lesson", value))
        else:
            print(Lesson.delete("lesson", column_name, value))
        return lesson_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return lesson_table()


def admin_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(Admin.select("admin")) == 0:
            print("Data not yet exist!")

        else:
            for i in Admin.select("admin"):
                print(f"""
                            ID: {i[0]},
                            First Name: {i[1]},
                            Last Name: {i[2]},
                            Email: {i[3]},
                            Password: {i[4]},
                            Headline: {i[5]},
                            Bio: {i[6]},
                            Contact Url: {i[7]},
                            Last Updated: {i[8]},
                            Create Date: {i[9]}
                        """)

        return admin_table()

    elif services == "2":  # INSERT
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        password = input("Password: ")
        headline = input("Headline: ")
        bio = input("Bio: ")
        contact_url = input("Contact Url: ")
        name = Admin(first_name, last_name, email, password, headline, bio, contact_url)
        print(name.insert("admin"))
        return admin_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: admin_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "admin_id":
            print(Admin.update_id("admin", column_name, old_data, new_data))
        else:
            print(Admin.update("admin", column_name, old_data, new_data))

        return admin_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: admin_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(Admin.delete_id("admin", value))
        else:
            print(Admin.delete("admin", column_name, value))
        return admin_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return admin_table()


def student_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(Student.select("student")) == 0:
            print("Data not yet exist!")

        else:
            for i in Student.select("student"):
                print(f"""
                            ID: {i[0]},
                            First Name: {i[1]},
                            Last Name: {i[2]},
                            Email: {i[3]},
                            Password: {i[4]},
                            Headline: {i[5]},
                            Bio: {i[6]},
                            Contact Url: {i[7]},
                            Last Updated: {i[8]},
                            Create Date: {i[9]}
                        """)

        return student_table()

    elif services == "2":  # INSERT
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        password = input("Password: ")
        headline = input("Headline: ")
        bio = input("Bio: ")
        contact_url = input("Contact Url: ")
        name = Student(first_name, last_name, email, password, headline, bio, contact_url)
        print(name.insert("student"))
        return student_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: student_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "student_id":
            print(Student.update_id("student", column_name, old_data, new_data))
        else:
            print(Student.update("student", column_name, old_data, new_data))

        return student_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: student_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(Student.delete_id("student", value))
        else:
            print(Student.delete("student", column_name, value))
        return student_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return student_table()


def comment_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(Comment.select("comment")) == 0:
            print("Data not yet exist!")

        else:
            for i in Comment.select("comment"):
                print(f"""
                            ID: {i[0]},
                            Text: {[1]},
                            Student ID: {i[2]},
                            Course ID: {i[3]},
                        """)

        return comment_table()

    elif services == "2":  # INSERT
        name = input("Comment: ")
        student_id = int(input("Student ID: "))
        course_id = int(input("Course ID: "))
        name = Comment(name, student_id, course_id)
        print(name.insert("comment"))
        return comment_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: comment_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "comment_id":
            print(Comment.update_id("comment", column_name, old_data, new_data))
        else:
            print(Comment.update("comment", column_name, old_data, new_data))

        return comment_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: comment_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(Comment.delete_id("comment", value))
        else:
            print(Comment.delete("comment", column_name, value))
        return comment_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return comment_table()


def payment_table():
    services = input("""
                Services:
                    1. SELECT
                    2. INSERT
                    3. UPDATE
                    4. DELETE
                    0. Back
                    >>> """)

    if services == "1":  # SELECT
        if len(Payment.select("payment")) == 0:
            print("Data not yet exist!")

        else:
            for i in Payment.select("payment"):
                print(f"""
                            ID: {i[0]},
                            Course ID: {i[1]},
                            Student ID: {i[2]},
                            Amount: {i[3]},
                            Card Number: {i[4]},
                            Create Date: {i[5]},
                        """)

        return payment_table()

    elif services == "2":  # INSERT
        course_id = int(input("Course ID: "))
        student_id = int(input("Student ID: "))
        amount = float(input("Amount: "))
        card_num = int(input("Card NUmber: "))
        name = Payment(course_id, student_id, amount, card_num)
        print(name.insert("payment"))
        return payment_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name(ID: payment_id): ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "payment_id":
            print(Payment.update_id("payment", column_name, old_data, new_data))
        else:
            print(Payment.update("payment", column_name, old_data, new_data))

        return payment_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column ID (ID: payment_id): ")
        value = input("Data: ")
        if column_name == "id":
            print(Payment.delete_id("payment", value))
        else:
            print(Payment.delete("payment", column_name, value))
        return payment_table()

    elif services == "0":
        return tables()

    else:
        print("Error!")
        return payment_table()


def tables():
    table = input("""
        Tables:
        1. Student
        2. Admin
        3. Lesson status
        4. Speciality
        5. Language
        6. Course status
        7. Course
        8. Speciality course
        9. Modules
        10. Lesson
        11. Comment
        12. Payment
        >>> """)

    if table == "1":
        return student_table()

    elif table == "2":
        return admin_table()

    elif table == "3":
        return lesson_status_table()

    elif table == "4":
        return speciality_table()

    elif table == "5":
        return language_table()

    elif table == "6":
        return course_status_table()

    elif table == "7":
        return course_table()

    elif table == "8":
        return speciality_course_table()

    elif table == "9":
        return module_table()

    elif table == "10":
        return lesson_table()

    elif table == "11":
        return comment_table()

    elif table == "12":
        return payment_table()

    else:
        print("Error")
        return tables()


if __name__ == "__main__":
    tables()
