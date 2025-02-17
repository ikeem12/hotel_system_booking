from flask_mysqldb import MySQL
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = MySQL()
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri= None    
)