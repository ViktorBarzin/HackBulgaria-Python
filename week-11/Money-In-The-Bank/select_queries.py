LOGIN = '''
SELECT ID, USERNAME, BALANCE, MESSAGE
FROM CLIENTS
WHERE USERNAME = ?
AND PASSWORD = ?
LIMIT 1
'''