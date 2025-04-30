import os

# Database path
DB_PATH = os.getenv('DB_PATH', 'default_db_path')  # default if variable not exist

# Email configuration
EMAIL_SERVER = os.getenv('EMAIL_SERVER', 'smtp.example.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))  # Converti in intero
SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'your_email@example.com')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL', 'receiver_email@example.com')
