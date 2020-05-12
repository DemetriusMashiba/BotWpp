from selenium import webdriver
import time

#bot made by Demetrius leonardo
#Automate the sending of messages in the zip zop

class zazapbot():
    def __init__(self):
        self.falacorno = "Bom dia amigos e amigas"
        self.grupos = ["Oi"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')


    def falaralgo(self):            
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        
        for grupo in self.grupos:
            teste = self.driver.find_elements_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            teste.click()
            chat_box = self.driver.find_elements_class_name('1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.falacorno)
            vai_logo = self.driver = self.driver.find_elements_by_xpath("//span[@data-icon = 'send']")
            time.sleep(3)
            vai_logo.click()
            time.sleep(5)


bot = zazapbot()
bot.falaralgo()