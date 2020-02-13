from flask import Blueprint, request, jsonify

from app import db
from .models import Auth

account = Blueprint("account", __name__)


@account.route("/signin", methods=["POST"])
def sign_in():
    data = request.get_json()
    auth = Auth.query.filter_by(email=data["email"]).first()
    if auth.verify_password(data["password"]) is False:
        return jsonify(), 401
    return jsonify({"token": "@TODO: token feature must be created"})


@account.route("/signup", methods=["POST"])
def sign_up():
    data = request.get_json()
    auth = Auth(email=data["email"], password=data["password"])
    db.session.add(auth)
    db.session.commit()

    return jsonify(), 201

