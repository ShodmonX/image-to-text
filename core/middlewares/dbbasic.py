import mysql.connector

my_db = mysql.connector.connect(
    host="database-1.crmi4swy49ff.eu-north-1.rds.amazonaws.com",
    user="admin",
    password="0ut7gaW6OGd2DQSNTIlf",
    database="imagetotextbot"
    )

my_cursor = my_db.cursor()

def add_user(user_id: str, username: str, first_name: str, last_name: str):
    my_cursor.execute("insert into users (user_id, username, first_name, last_name, user_condition) values (%s, %s, %s, %s, %s)", [user_id, username, first_name, last_name, "active"])
    my_db.commit()


def user_condition_change_active(user_id: str):
    my_cursor.execute("select user_condition from users where user_id=%s", [user_id])
    if my_cursor.fetchone()[0] == "passive":
        my_cursor.execute("update users set user_condition=%s where user_id=%s", ["active", user_id])
        my_db.commit()


def user_condition_change_passive(user_id: str):
    my_cursor.execute("select user_condition from users where user_id=%s", [user_id])
    if my_cursor.fetchone()[0] == "active":
        my_cursor.execute("update users set user_condition=%s where user_id=%s", ["passive", user_id])
        my_db.commit()


def all_user_ids():
    my_cursor.execute("select user_id from users")
    return [i[0] for i in my_cursor.fetchall()]

def number_of_all_users():
    my_cursor.execute("select count(user_id) from users")
    return my_cursor.fetchone()[0]

def number_of_active_users():
    my_cursor.execute("select count(user_id) from users where user_condition='active'")
    return my_cursor.fetchone()[0]

def number_of_passive_users():
    my_cursor.execute("select count(user_id) from users where user_condition='passive'")
    return my_cursor.fetchone()[0]

