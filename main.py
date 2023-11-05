from selenium import webdriver
import time
from Kit import *



# 设置浏览器驱动程序的路径，这里以Chrome为例
driver_path = "路径到你的Chrome驱动程序/chromedriver.exe"  # 请替换为你的驱动程序路径
chrome_driver_path = r'"C:\Users\kenger\Documents\GitHub\kenger_ai\chatgpt_with_selenium\chatgpt_selenium_automation\chromedriver104.exe"'
# the sintax r'"..."' is required because the space in "Program Files" in the chrome path
chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'



# # 创建一个Chrome浏览器实例
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# 打开Google学术网站
url = "https://scholar.google.com.hk/?hl=zh-CN"
history_folder = "remote-chrome-google-scholar-profile"
free_port = find_available_port()

launch_chrome_with_remote_debugging(chrome_path, free_port, url, history_folder)

wait_for_human_verification()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{free_port}")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

