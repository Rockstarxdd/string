import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = ""
    API_HASH = ""
    BOT_TOKEN = "51146sshsys90:AAFpOMbq9B6mdjjdcwe2YPXJwBjz9inapblM"
    DATABASE_URL = "postgresql://ecvcveyr:AALEuRK1daNipxrO79rJPb@abul.db.elepndjjdjdhantsql.com/ecvcveyr"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "@Starz_bots"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

       #✗ Pᴏᴡᴇʀᴇᴅ 💕 By Rockstar
