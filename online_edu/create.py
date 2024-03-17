from db_connect import Database


def create_table():

    student_table = """
        CREATE TABLE student(student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20),
            email VARCHAR(20),
            password VARCHAR(20),
            headline VARCHAR(50),
            bio TEXT,
            contact_url VARCHAR(30),
            last_updated DATE,
            create_date TIMESTAMP DEFAULT now());
    """

    admin_table = """
            CREATE TABLE admin(admin_id SERIAL PRIMARY KEY,
                first_name VARCHAR(20) NOT NULL,
                last_name VARCHAR(20),
                email VARCHAR(20),
                password VARCHAR(20),
                headline VARCHAR(50),
                bio TEXT,
                contact_url VARCHAR(30),
                last_updated DATE,
                create_date TIMESTAMP DEFAULT now());
        """

    lesson_status_table = """
        CREATE TABLE lesson_status(lesson_status_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_date TIMESTAMP DEFAULT now());
    """

    speciality_table = """
            CREATE TABLE speciality(speciality_id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                create_date TIMESTAMP DEFAULT now());
        """

    language_table = """
                CREATE TABLE language(language_id SERIAL PRIMARY KEY,
                    name VARCHAR(20),
                    last_updated DATE,
                    create_date TIMESTAMP DEFAULT now());
            """

    course_status_table = """
                CREATE TABLE course_status(course_status_id SERIAL PRIMARY KEY,
                    name VARCHAR(20),
                    create_date TIMESTAMP DEFAULT now());
            """

    course_table = """
        CREATE TABLE course(course_id SERIAL PRIMARY KEY,
            name VARCHAR(40),
            description TEXT,
            rating FLOAT,
            admin_id INT REFERENCES admin(admin_id),
            language_id INT REFERENCES language(language_id),
            price NUMERIC,
            course_status_id INT REFERENCES course_status(course_status_id),
            support_date DATE,
            last_update DATE,
            create_date TIMESTAMP DEFAULT now());
    """

    speciality_course_table = """
            CREATE TABLE speciality_course(speciality_course_id SERIAL PRIMARY KEY,
                speciality_id INT REFERENCES speciality(speciality_id),
                course_id INT REFERENCES course(course_id),
                create_date TIMESTAMP DEFAULT now());
        """

    modules_table = """
                CREATE TABLE modules(module_id SERIAL PRIMARY KEY,
                    name VARCHAR(20),
                    course_id INT REFERENCES course(course_id),
                    lesson_count INT,
                    last_updated DATE,
                    create_date TIMESTAMP DEFAULT now());
            """

    lesson_table = """
                CREATE TABLE lesson(lesson_id SERIAL PRIMARY KEY,
                    name VARCHAR(20),
                    description TEXT,
                    lesson_status_id INT REFERENCES lesson_status(lesson_status_id),
                    module_id INT REFERENCES modules(module_id),
                    create_date TIMESTAMP DEFAULT now());
            """

    comment_table = """
        CREATE TABLE comment(comment_id SERIAL PRIMARY KEY,
            text TEXT,
            student_id INT REFERENCES student(student_id),
            course_id INT REFERENCES course(course_id));
    """

    payment_table = """
        CREATE TABLE payment(payment_id SERIAL PRIMARY KEY,
            course_id INT REFERENCES course(course_id),
            student_id INT REFERENCES student(student_id),
            amount FLOAT,
            card_number BIGINT,
            create_date TIMESTAMP DEFAULT now());
        """

    data = {
        "student_table": student_table,
        "admin_table": admin_table,
        "lesson_status_table": lesson_status_table,
        "speciality_table": speciality_table,
        "language_table": language_table,
        "course_status_table": course_status_table,
        "course_table": course_table,
        "speciality_course_table": speciality_course_table,
        "modules_table": modules_table,
        "lesson_table": lesson_table,
        "comment_table": comment_table,
        "payment_table": payment_table
    }

    for i in data:
        print(f"{i}: {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()

