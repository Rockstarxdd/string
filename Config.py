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
    API_ID = "13347879"
    API_HASH = "241f2ef7f35ce132fc849eb9964f4b10"
    BOT_TOKEN = "5114672990:AAFpOMbq9B6FD3Icwe2YPXJwBjz9inapblM"
    DATABASE_URL = "postgresql://ecvcveyr:AALEuRK1daNipxraQzSxxWzDiO79rJPb@abul.db.elephantsql.com/ecvcveyr"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "@Starz_bots"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

       #✗ Pᴏᴡᴇʀᴇᴅ 💕 By Rockstar
