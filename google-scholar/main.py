from selenium import webdriver
import time
from Kit import *


import re
import os
import bibtexparser
import random



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




# driver.get(url)





# 读取bibtex文件，生成字典
bib_name = r'C:\Users\kenger\Documents\GitHub\GH_bot_kenger\wolfbolin\test.bib'

out_bib =  bibtexparser.bibdatabase.BibDatabase()

# 将BibTeX内容分割为各个条目
with open(bib_name, 'r', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)





count = 0 



# for entry in bib_database.entries:
while True:
    try:

        # 输入待查找的论文名字
        paper_name = input("请输入待查找的论文名字：")

        # paper_name = entry['title']
        # print("待查找的论文名字：", paper_name)

        search_box = driver.find_element(by="xpath", value='//*[@id="gs_hdr_tsi"]')
        search_box.clear()  # 清除搜索框中的内容
        search_box.send_keys(paper_name) 
        time.sleep(random.randint(2, 5))
        search_button = driver.find_element(by="xpath", value='//*[@id="gs_hdr_tsb"]')
        search_button.click()

        # 随机睡眠2-5秒
        time.sleep(random.randint(2, 5))


        # 使用XPath定位具有id属性为"gs_res_ccl_mid"的元素
        element =driver.find_element(by="css selector", value='#gs_res_ccl_mid > div > div.gs_ri')  

        # 找到该元素下的第一个a元素
        first_a_element = element.find_element(by="xpath", value='./descendant::a[1]')

        # 获取第一个a元素的href属性和文本内容
        href = first_a_element.get_attribute("href")
        name = first_a_element.text

        # 如果herf的最后一个字符是/，则去掉它
        if href[-1] == "/":
            href = href[:-1]

        # print("第一个a元素的href属性:", href)
        print("第一个a元素的文本内容:", name)

        
        # entry['url'] = href
        # out_bib.entries.append(entry)

        count += 1
        if count % 10 == 0:
            # 打开文件以写入BibTeX数据
            with open('out.bib', 'w', encoding='utf-8') as bibtex_file:
                bibtexparser.dump(out_bib, bibtex_file)

        print(f"\n,\nurl = {{{href}}}")

        time.sleep(random.randint(2, 5))
    except Exception as e:
        print(e)
        print("请重新输入")
        

