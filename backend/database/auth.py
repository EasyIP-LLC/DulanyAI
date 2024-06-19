from sqlalchemy.orm import Session
from .models import LoginCredential, RegUser
from .factory import DatabaseCall
from app.extensions import bcrypt
from flask import jsonify
import logging


class Auth(DatabaseCall):
    def __init__(self):
        super().__init__()

    def signInUser(self, email: str, password: str):
        user = self.session.query(LoginCredential).filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return jsonify({"message": f"User {email} signed in successfully."}), 200
        else:
            return jsonify({"error": "Invalid credentials."}), 401

    def registerUser(
        self, firstName: str, lastName: str, email: str, phone: str, password: str
    ):
        try:
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

            loginCredential = LoginCredential(
                email=email,
                password=hashed_password,
                token="None",
                login_provider="default",
            )

            user = RegUser(
                first_name=firstName,
                last_name=lastName,
                phone=phone,
                login_credential_id=loginCredential.id,
            )

            self.createAndCommit([loginCredential, user])

            requestResponse = {
                "request": "user registered successfully",
                "user": {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone": user.phone,
                    "email": email,
                },
            }
            return jsonify(requestResponse), 200

        except Exception as e:
            self.session.rollback()
            self.logger.error(f"An error occurred during registration: {e}")
            return jsonify({"error": f"An error occurred: {e}"}), 400

    def signOutUser(self):
        try:
            # Implement sign out logic here
            self.logger.info("Sign out logic")
            return jsonify({"message": "User signed out successfully."}), 200
        except Exception as e:
            self.logger.error(f"An error occurred during sign out: {e}")
            return jsonify({"error": f"An error occurred: {e}"}), 400
