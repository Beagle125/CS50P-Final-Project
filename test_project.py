#Import functions and class from project file
from project import Balance
from project import create_account
from project import open_account
from project import delete_account

#tests
def test_create_account():
#1
    assert create_account('test_username','test_password','PHP',100) == (f'Username:test_username, Password:test_password, Currency:PHP, Balance:{round(float(100),2)}')

def test_open_account():
#1
    assert open_account('test_username','test_password') == True

def test_delete_account():
#1
    assert delete_account('test_username') == 'Account successfully deleted!'
#2
    assert open_account('test_username','test_password') == False
