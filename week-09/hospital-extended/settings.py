DB_CONNECTION_STRING = 'hospital.db'
DB_CREATION_QUERIES_FILE = 'db_creation_queries.py'
ACADEMIC_TITLES = ['nurse', 'doctor', 'pich']
ROOM_NUMBERS = [2, 4, 6, 8, 9, 12]
INJURIES = ['too awesome', 'too cool', 'zabobol']

# If changing any of the options below, remember to change the use in code as well
MAIN_MENU_OPTIONS = {1: 'login', 2: 'register', 3: 'help', 4: 'exit'}

# todo: find a more elegant way to save the options
LOGGED_IN_PATIENT_OPTIONS = {1: 'See free hours of your doctor', 2: 'Reserve hour for visitation',
                             3: 'Stay at the hospital for an injury', 4: 'See the academic of your doctor',
                             5: 'List your hospital stays', 6: 'Change doctor',
                             7: 'Change username and/or age', 8: 'Logout'}

LOGGED_IN_DOCTOR_OPTIONS = {1: 'List your patients', 2: 'Add hour for visitation',
                            3: 'Delete free hours for visitation',
                            4: 'See room number and duration of hospital stays for each of your patients',
                            5: 'Change username and/or age', 6: 'Raise in the hierarchy',
                            7: 'Logout'}
LOGOUT_KEY = '__logout'
# The below constant is used in registration
MAX_FAILED_PASSWORD_ATTEMPTS = 3
