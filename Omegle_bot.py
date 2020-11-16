from selenium import webdriver
from time import sleep
while True:
    driver = webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")#provide the local download location of chrome driver for my case it is in downloads
    driver.get('https://www.omegle.com/')
    driver.maximize_window()
    sleep(2)
    loginbtn = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[1]/div/div/div[1]/input")
    loginbtn.send_keys('youtube')#Type your common intrest here
    cli=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[2]/img")
    cli.click()
    sleep(2)
    lol=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea")
    lol.send_keys('Want to learn hacking for free? Then check this out https://www.youtube.com/c/NoobHacker')#Type your text that you want to spam 
    sleep(2)
    zaz=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button")
    zaz.click()
    sleep(3)
    driver.close()
