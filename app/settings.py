from decouple import config

DB_NAME = config("DB_NAME", "cart-management")
DB_HOST = config("DB_HOST", "localhost")
DB_PORT = config("DB_PORT", 5432)
DB_USER = config("DB_USER", "postgres")
DB_PASSWORD = config("DB_PASSWORD", "password")
