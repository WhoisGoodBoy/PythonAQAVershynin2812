from lesson28.connection import session
from lesson28.models.very_cool_users_table import VeryCoolUsersTable



class VeryCoolUsersTableRepository:
    def __init__(self):
        self.sess = session

    def add_one_row(self, user):
        self.sess.add(user)
        self.sess.commit()

    def get_by_user_id(self, user_id):
        return self.sess.get(VeryCoolUsersTable, {'id':user_id})


users_repository = VeryCoolUsersTableRepository()
#user_to_add = VeryCoolUsersTable(id='CCCCCCCC', first_name='Gustavo', last_name='Fringman', age=55, email='gustavo_fringman@gmail.com')
#users_repository.add_one_row(user_to_add)
hello_my_name_is_gustavo = users_repository.get_by_user_id('CCCCCCCC')
print(hello_my_name_is_gustavo)
