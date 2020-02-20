import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


options = Options()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)

try:
    driver.get("https://www.google.co.jp/")
    # 簡易的にJSが評価されるまで秒数で待つ
    time.sleep(5)

    # aタグを抽出
    elem_list = driver.find_elements_by_tag_name("a")
    for elem in elem_list:
        # attributeの中からhrefを抽出して出力
        url = elem.get_attribute("href")
        print(url)
except:
    traceback.print_exc()
finally:
    # エラーが起きても起きなくてもブラウザを閉じる
    driver.quit()