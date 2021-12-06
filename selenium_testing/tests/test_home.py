from seleniumbase import BaseCase

class HomeTest(BaseCase):

    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

        #login
        self.open("https://practice.automationbro.com/my-account")
        self.add_text("#username","selenium123")
        self.add_text("#password","selenium123.!")
        self.sleep(5)
        self.click("button[name=login]")
        self.assert_text("Log out", ".woocommerce-MyAccount-content")

        #open home page
        self.open("https://practice.automationbro.com")
        
    def tearDown(self):
            print("RUNNING AFTER EACH TEST")

            #Logout
            self.open("https://practice.automationbro.com/my-account")
            self.click(".woocommerce-MyAccount-content a[href*=logout]")
            self.assert_element_visible("button[name=login]")

            super().tearDown()
    

    def test_home_page(self):
        #assert home page and logo
        #self.open("https://practice.automationbro.com")
        self.assert_title("Practice E-Commerce  – Automation Bro")
        self.assert_element(".custom-logo-link")

        #assert url on clicking get started
        self.click("#get-started")
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")
        self.assert_true("get-started" in get_started_url)

        #assert value of header
        self.assert_text("Think different. Make different.","h1")
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro",".tg-site-footer-section-1")


    # def test_menu_links(self):
    #     #find menu link elements
    #     menu_links_all = self.find_elements("li[id*=menu-item]")
    #     for link in menu_links_all:
    #         print(link.text)


