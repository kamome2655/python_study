import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


import logging
logging.basicConfig(filename='test.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info("処理を開始します。")
logging.critical('criticalメッセージ')
logging.error('errorメッセージ')
logging.warning('warningメッセージ')
logging.debug('debugメッセージ') 


# Chromeを起動する関数
def set_driver(driver_path, headless_flg):
    if "chrome" in driver_path:
          options = ChromeOptions()
    else:
      options = Options()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    if "chrome" in driver_path:
        return Chrome(executable_path=os.getcwd() + "/" + driver_path,options=options)
    else:
        return Firefox(executable_path=os.getcwd()  + "/" + driver_path,options=options)

# main処理


def main():
    search_keyword = input("キーワードを入れてください > ")
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')

    # 検索窓に入力
    driver.find_element_by_class_name(
        "topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()

    df = pd.DataFrame()
        
    while True:
        name_list = driver.find_elements_by_class_name("cassetteRecruit__name")
        copy_list = driver.find_elements_by_class_name("cassetteRecruit__copy")

        print(len(name_list))
        for name,copy in zip(name_list,copy_list):
            print(name.text,copy.text)

            df = df.append({
                "会社名": name.text, 
                "求人タイトル": copy.text,
            }, ignore_index=True)
                        
        try:
            time.sleep(5)
            driver.execute_script('document.querySelector(".karte-close").click()')
        except:
            pass
            try:
                time.sleep(5)
                element = driver.find_element_by_class_name('iconFont--arrowLeft')
                driver.execute_script('arguments[0].click();', element)
            except:
        
                print("最終ページです")
                break


    df.to_csv("記事一覧.csv", encoding="utf-8_sig")             

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()