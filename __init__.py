from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)
    
    # Security headers (Talisman)
    Talisman(app)

    # Import routes dari app.py
    from app import (
        create_account,
        list_accounts,
        get_account,
        update_account,
        delete_account,
        home
    )

    # Register routes
    app.add_url_rule("/", view_func=home)
    app.add_url_rule("/accounts", view_func=list_accounts, methods=["GET"])
    app.add_url_rule("/accounts", view_func=create_account, methods=["POST"])
    app.add_url_rule("/accounts/<int:id>", view_func=get_account, methods=["GET"])
    app.add_url_rule("/accounts/<int:id>", view_func=update_account, methods=["PUT"])
    app.add_url_rule("/accounts/<int:id>", view_func=delete_account, methods=["DELETE"])

    return app