import credentials

CONNECTION_STRING = 'bank.db'
BAN_LIST_FILE = 'ban-list.json'
BAN_TIME = 300
WRONG_PASSWORD_ATTEPMTS = 5

# SMTP settings
EMAIL_ACCOUNT_USER = credentials.email_username
EMAIL_ACCOUNT_PASSWORD = credentials.email_password

EMAIL_SUBJ = 'Password reset token'
EMAIL_BODY = 'Your password reset token is:'  # note that at the end is added the token
