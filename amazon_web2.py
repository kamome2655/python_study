import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd
import datetime
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import eel

LOG_FILE_PATH = "./log/log_{datetime}.log"
EXP_CSV_PATH="./exp_list_{datetime}.csv"
log_file_path=LOG_FILE_PATH.format(datetime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

### Chromeを起動する関数
def set_driver(driver_path, headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

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
    return Chrome(ChromeDriverManager().install(), options=options)

### ログファイルおよびコンソール出力
def log(txt):
    now=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    logStr = '[%s: %s] %s' % ('log',now , txt)
    # ログ出力
    with open(log_file_path, 'a', encoding='utf-8_sig') as f:
        f.write(logStr + '\n')
    print(logStr)


### main処理
def main(url_name):
    log("処理開始")
    # driverを起動
    driver = set_driver("chromedriver.exe", False)
    # Webサイトを開く
    driver.get(url_name)
    time.sleep(5)
    
    eel.view_log_js("処理開始")
    
    
    df = pd.DataFrame()

     
    count = 0
    success = 0
    fail = 0

    while True:
        item_name = driver.find_elements_by_class_name("zg-item-immersion")
        for item in item_name:
            try:
                link = item.find_element_by_tag_name("a").get_attribute("href")
                driver2 = set_driver("chromedriver.exe", False)
                driver2.get(link)
                item_name = driver2.find_element_by_id("productTitle").text
                item_price = driver2.find_element_by_css_selector(".a-lineitem.a-align-top").text
                item_delivery = driver2.find_element_by_id("deliveryBlockMessage").text
                item_asin = driver2.find_element_by_id("ASIN").get_attribute("value")
                print(item_name,item_price,item_delivery,item_asin)
                driver2.quit()
                log(f"{count}件目成功 : {item_name}")
                success+=1
                eel.view_log_js(f"{count}件目成功 ") 
                
                df = df.append({
                    "商品名": item_name,
                    "価格": item_price,
                    "リードタイム": item_delivery,
                    "ASIN": item_asin,
                }, ignore_index=True)
                
            except Exception as e:
                log(f"{count}件目失敗 : {item_name}")
                log(e)
                fail+=1
                eel.view_log_js(f"{count}件目失敗 ") 
            finally:
                # finallyは成功でもエラーでも必ず実行
                count+=1
                
      
            
        # 次のページボタンがあればクリックなければ終了
        next_page = driver.find_elements_by_xpath("//ul/li[@class='a-last']/a")
        time.sleep(5)
        if len(next_page) >= 1:
            next_page_link = next_page[0].get_attribute("href")
            driver.get(next_page_link)
        else:
            log("最終ページです。終了します。")
            eel.view_log_js("最終ページです。終了します。")
            break

    # CSV出力
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    
    df.to_csv(EXP_CSV_PATH.format(datetime=now), encoding="utf-8-sig")
    log(f"処理完了 成功件数: {success} 件 / 失敗件数: {fail} 件")
    eel.view_log_js(f"処理完了 成功件数: {success} 件 / 失敗件数: {fail} 件")
    
