from datetime import datetime
from db_connect import Database


class Base:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table}"
        return Database.connect(query, "select")

    @staticmethod
    def update_id(table, column_name, old_data, new_data):
        query = f"UPDATE {table} SET {column_name} = {new_data} WHERE {column_name} = {old_data}"
        return Database.connect(query, "update")

    @staticmethod
    def update(table, column_name, old_data, new_data):
        query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(table, data):
        query = f"DELETE FROM {table} WHERE {table}_id = {data}"
        return Database.connect(query, "delete")

    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = '{data}'"
        return Database.connect(query, "delete")


class Student(Base):
    def __init__(self, first_name, last_name, email, password, headline, bio, contact_url):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.headline = headline
        self.bio = bio
        self.contact_url = contact_url
        self.last_updated = f"{datetime.now()}"

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(first_name, last_name, email, password, headline, bio, contact_url, last_updated)
        VALUES('{self.first_name}', '{self.last_name}', '{self.email}', '{self.password}', '{self.headline}', '{self.bio}',
         '{self.contact_url}', '{self.last_updated}');
        """
        return Database.connect(query, "insert")


class Admin(Base):
    def __init__(self, first_name, last_name, email, password, headline, bio, contact_url):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.headline = headline
        self.bio = bio
        self.contact_url = contact_url
        self.last_updated = f"{datetime.now()}"

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(first_name, last_name, email, password, headline, bio, contact_url, last_updated)
        VALUES('{self.first_name}', '{self.last_name}', '{self.email}', '{self.password}', '{self.headline}', '{self.bio}',
         '{self.contact_url}', '{self.last_updated}');
        """
        return Database.connect(query, "insert")


class LessonStatus(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(name) VALUES('{self.name}');
        """
        return Database.connect(query, "insert")


class Speciality(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES('{self.name}');"""
        return Database.connect(query, "insert")


class Language(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(name) VALUES('{self.name}');
        """
        return Database.connect(query, "insert")


class CourseStatus(Base):
    def __init__(self, name):
        self.name = name
        self.table_name = "course_status"

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(name) VALUES('{self.name}');
        """
        return Database.connect(query, "insert")


class Course(Base):
    def __init__(self, name, description, rating, active_students, admin_id, language_id, price, course_status_id, support_date):
        self.name = name
        self.description = description
        self.rating = rating
        self.active_students = active_students
        self.admin_id = admin_id
        self.language_id = language_id
        self.price = price
        self.course_status_id = course_status_id
        self.support_date = support_date

    @staticmethod
    def select(table):
        query = """SELECT course.course_id, course.name, course.description, course.rating, admin.first_name,
        admin.last_name, course_status.name, language.name, course.price FROM course
        INNER JOIN admin ON course.admin_id = admin.admin_id
        INNER JOIN course_status ON course_status.course_status_id = course.course_status_id
        INNER JOIN language ON language.language_id = course.language_id"""

        return Database.connect(query, "select")

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(name, description, rating, admin_id, language_id, price, course_status_id, support_date)
        VALUES('{self.name}', '{self.description}', {self.rating}, {self.admin_id}, {self.language_id}, {self.price},
        {self.course_status_id}, '{self.support_date}'); """
        return Database.connect(query, "insert")


class SpecialityCourse(Base):
    def __init__(self, speciality_id, course_id):
        self.speciality_id = speciality_id
        self.course_id = course_id

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(speciality_id, course_id) VALUES({self.speciality_id}, {self.course_id});
        """
        return Database.connect(query, "insert")


class Module(Base):
    def __init__(self, name, course_id, lesson_count, last_updated):
        self.name = name
        self.course_id = course_id
        self.lesson_count = lesson_count
        self.last_updated = f"{datetime.now()}"

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(name, course_id, lesson_count, last_updated) 
        VALUES('{self.name}', {self.course_id}, {self.lesson_count}, '{self.last_updated}');
        """
        return Database.connect(query, "insert")


class Lesson(Base):
    def __init__(self, name, description, lesson_status_id, module_id):
        self.name = name
        self.description = description
        self.lesson_status_id = lesson_status_id
        self.module_id = module_id

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(name, description, lesson_status_id, module_id) 
        VALUES('{self.name}', '{self.description}', {self.lesson_status_id}, {self.module_id});
        """
        return Database.connect(query, "insert")


class Comment(Base):
    def __init__(self, text, student_id, course_id):
        self.text = text
        self.student_id = student_id
        self.course_id = course_id

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(text, student_id, course_id) VALUES('{self.text}', {self.student_id}, {self.course_id});
        """
        return Database.connect(query, "insert")


class Payment(Base):
    def __init__(self, course_id, student_id, amount, card_number):
        self.course_id = course_id
        self.student_id = student_id
        self.amount = amount
        self.card_number = card_number

    def insert(self, table):
        query = f"""
        INSERT INTO {table}(course_id, student_id, amount, card_number) 
        VALUES({self.course_id}, {self.student_id}, {self.amount}, {self.card_number});
        """
        return Database.connect(query, "insert")
