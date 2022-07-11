# Practicing with selenium
# Automating Boring stuff
# -----------------------------------------------------------------------
# Tutorial - Lesson 1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


edge_driver_path = "C:\Development\msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver_path)
driver.maximize_window()
driver.implicitly_wait(20)

# driver.get("https://www.youtube.com")
driver.get("https://www.google.com.pe")
# driver.get("https://techwithtim.net")
# print(driver.title)
# driver.quit()

# -----------------------------------------------------------------------
# Tutorial - Lesson 2 - Locating Elements from HTML
# Example website: "https://techwithtim.net"

NAME = "q"
XPATH = '"//*[@id="rso"]/div[2]/video-voyager/div/div/div/div[1]/a/h3"'
# CLASS_NAME = "search-field"

search = driver.find_element(by=By.NAME, value='q')
search.send_keys("Taylor Swift - All too well speed up")
search.send_keys(Keys.RETURN)
time.sleep(3)
video = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[2]/video-voyager/div/div/div/div[1]/a/h3').click()
time.sleep(10)
driver.quit()

# search = driver.find_element(by=By.CLASS_NAME, value='search-field')
# search.send_keys("test")
# search.send_keys(Keys.RETURN)




# -----------------------------------------------------------------------
# Tutorial - Lesson 3

# -----------------------------------------------------------------------
# Tutorial - Lesson 4

# -----------------------------------------------------------------------
# Tutorial - Lesson 5


# -----------------------------------------------------------------------
# Tutorial - Lesson 6

# -----------------------------------------------------------------------
# Tutorial - Lesson 7

# Cambiaron los metodos pipipipi
# search = driver.find_element_by_name("search_query") 
# search.send_keys("Alonzo nub")

# Remember to verify if both the driver and your browser have the same version or you will get an error.
# And it would as it follows:

# selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of MSEdgeDriver only supports MSEdge version 100
# Current browser version is 103.0.1264.49 with binary path C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe

# Then you got a download a new driver (of any browser e.g. chrome, edge) of the current version of your browser in the previous case it would
# from version 100 to version 103 because my current browser version is 103.0.1264.49