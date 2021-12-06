from seleniumbase import BaseCase

class UploadTest(BaseCase):
    

    def test_upload(self):
        self.open("https://practice.automationbro.com/cart")
        file_path = './data/cake.jpeg'
        remove_hidden_class = "document.getElementById(upfile_1').classList.remove('file_input_hidden')"
        self.add_js_code(remove_hidden_class)
        self.choose_file('#upfile_1',file_path)
        self.sleep(5)
        self.click("#upload_1")