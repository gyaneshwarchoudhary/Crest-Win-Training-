# user_service.py
import logging


class Database:
    """Simulated database class."""

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.users = {}  # in‑memory store

    def connect(self):
        logging.info(f"Connecting to {self.connection_string}")
        # In reality you'd establish a connection here

    def get_user(self, user_id):
        return self.users.get(user_id)

    def add_user(self, user):
        self.users[user["id"]] = user
        return user

    def update_user(self, user_id, data):
        if user_id in self.users:
            self.users[user_id].update(data)
            return self.users[user_id]
        return None


class EmailSender:
    """Simulated email sender."""

    def send_welcome_email(self, user_email):
        # Imagine this sends an actual email via SMTP
        logging.info(f"Sending welcome email to {user_email}")
        return True


class UserService:
    def __init__(self, db: Database, email_sender: EmailSender):
        self.db = db
        self.email_sender = email_sender

    def get_user(self, user_id):
        return self.db.get_user(user_id)

    def create_user(self, user_data):
        # Ensure id is present
        if "id" not in user_data:
            raise ValueError("User must have an id")
        user = self.db.add_user(user_data)
        self.email_sender.send_welcome_email(user["email"])
        return user

    def update_email(self, user_id, new_email):
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        user["email"] = new_email
        self.db.update_user(user_id, {"email": new_email})
        return user
