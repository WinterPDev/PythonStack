from flask_app.config.mysqlconnection import connectToMySQL


class User:
    # schema = "users_schema" why no workie???
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def insert_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s)"
        return connectToMySQL("users_schema").query_db(query,data)

    @classmethod
    def pull_all_users(cls):
        query = "SELECT * FROM users"
        query_results = connectToMySQL("users_schema").query_db(query)

        users= []

        for each_row in query_results:
            new_user = cls(each_row)
            users.append(new_user)

        return users
