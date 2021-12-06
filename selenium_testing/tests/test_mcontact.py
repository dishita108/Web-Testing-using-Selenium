from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_page(self):
        self.open("https://practice.automationbro.com/contact")
        self.send_keys('.contact-name input', 'Dishita Ashar')
        self.send_keys('.contact-email input', 'da@gmail.com')
        self.send_keys('.contact-phone input', '9876543219')
        self.send_keys('.contact-message textarea', 'Web testing using SeleniumBase')
        self.sleep(5)
        self.click("#evf-submit-277")
        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "div[role=alert]")