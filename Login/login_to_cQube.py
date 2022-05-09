from reuse_func import GetData

''' Script developed to validation of login is working or not '''

class cQube_Login():
    def __init__(self, driver):
        self.data = None
        self.driver = driver

    def test_login_to_cQube(self):
        self.data = GetData()
        count = 0
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print('login to cQube is successfully ')
        else:
            print('Login to cQube is failed ')
            count = count + 1
        return count
