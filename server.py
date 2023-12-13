from waitress import serve
from app import app, db, login_manager  # Import db as well
import os
import sys
import logging
from logger import log_args_and_return
from models.air_dsr import AIRDSR  # Import model
from models.login import USER

# Logging Configuration
log_format = '%(asctime)s %(levelname)s %(message)s'
log_level = logging.INFO
logging.basicConfig(format=log_format, level=log_level, stream=sys.stdout)


# Login manager configuration
@login_manager.user_loader
def load_user(user_id):
    user= USER.query.get(int(user_id))
    if user:
        return user
    return None

def run_app():
    # Move the table creation logic here
    with app.app_context():
        # if not AIRDSR.__table__.exists(db.engine):
        #     AIRDSR.__table__.create(db.engine)
        #     logging.info("AIRDSR table created")
        # new_user = USER('Admin', '2021-12-11', 'test@tsvglobal.com', 'password', '', '', 'external', 'RO', 'AMARA RAJA BATTERIES LIMITED')
        # db.session.add(new_user)
        # db.session.commit()
        db.create_all()  # Uncomment if you want to create all tables
        host = os.environ.get('SERVER_HOST', 'localhost')
        port = int(os.environ.get('SERVER_PORT', '9099'))
        serve(app, host=host, port=port)

if __name__ == "__main__":
    try:
        run_app()
    except Exception as e:
        logging.exception("An unhandled exception occurred: %s", str(e))
