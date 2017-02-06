import json
import datetime
# from decorators import check_ban_list_file


def ban_list_json_to_dict(ban_file):
    with open(ban_file, 'r') as r:
        return json.load(r)


def add_user_to_ban_list_json(ban_file, username):
    # Asserts ban-list file is not empty
    data = ban_list_json_to_dict(ban_file)
    with open(ban_file, 'w') as w:
        data.append({})
        data[-1]['username'] = username
        data[-1]['ban-start-date'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        data[-1]['wrong-attempts'] = 1

        w.write(json.dumps(data))


# @check_ban_list_file
def change_failed_password_attempts(ban_file, username, update):
    data = ban_list_json_to_dict(ban_file)
    try:
        user = [x for x in data if x['username'] == username][0]
        user['wrong-attempts'] += update
        user['ban-start-date'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if user['wrong-attempts'] < 0:
            user['wrong-attempts'] = 0
    except IndexError:
        add_user_to_ban_list_json(ban_file, username)
        return

    # Save changes to .json file
    with open(ban_file, 'w') as w:
        w.write(json.dumps(data))


def clear_login_ban_records(ban_file, username, WRONG_PASSWORD_ATTEMPTS):
    change_failed_password_attempts(ban_file, username, -WRONG_PASSWORD_ATTEMPTS)


