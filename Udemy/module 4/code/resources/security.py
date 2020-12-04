from resources.user import UserModal
from werkzeug.security import safe_str_cmp


# users = [
#     {
#         "id": 1,
#         "username": 'bob',
#         "password": 'abcd',
#     }
# ]

# username_mapping = {u.username: u for u in users}

# username_mapping = {
#     'bob':
#         {
#             "id": 1,
#             "username": 'bob',
#             'password': 'abcd',
#         }
# }

# userid_mapping = {u.id: u for u in users}

# userid_mapping = {
#     1:
#         {
#             "id": 1,
#             "username": 'bob',
#             'password': 'abcd',
#         }
# }


def authenticate(username, password):
    user = UserModal.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModal.find_by_id(user_id)
