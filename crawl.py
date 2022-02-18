import os,subprocess,datetime,time,random,argparse,http.client,json,zipfile,pyautogui,requests,urllib.parse,lib
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from random import randint,shuffle


# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--Target", required=True)
parser.add_argument("-p", "--Proxy")
parser.add_argument("-r", "--Referer")
parser.add_argument("-v", "--Version")
args = parser.parse_args()


if args:
      
    Target = "http://" + args.Target
    Query = "site:" + args.Target
    Version = args.Version
    Referer = args.Referer
    
    # if Version:
        # vR = args.Version
    # else:
        # vR = "desktop"
    # PDIR = "/root/x/p/"+vR
    # if not os.path.exists(PDIR):
      # os.makedirs(PDIR)
    
    ua = lib.ua(Version)
    
    if "Android"  in ua or "iPhone"  in ua or "iPod" in ua:
        h = [240,360,480,480]
        w = [320,640,640,800]
    elif "iPad" in ua:
        h = [768,864,768,600,600,480,480]
        w = [1366,1152,1024,1024,800,800,640]
    else :
        w = [1024,1280,1280,1280,1360,1440,1152,1600,1600,1680,1920,1920]
        h = [768,720,800,1024,768,900,864,900,1200,1050,1080,1200]
        
    t = random.randint(0,len(w)-1)
    
    subprocess.call(["xrandr", "-s", str(w[t])+ "x"+str(h[t])])
    # subprocess.call(["xrandr", "--mode", str(w[t])+ "x"+str(h[t])],"--display",":0")
    time.sleep(5)
    
    if Referer == "google":
        RefX = "https://www.google.com/search?q="+Query+"&hl=en&gl=US"
    elif Referer == "googleimage":
        RefX = "https://www.google.com/search?q="+Query+"&hl=en&tbm=isch&source=hp&biw="+str(w[t])+"&bih="+str(h[t])+"&sclient=img"
    elif Referer == "bing":
        RefX = "https://www.bing.com/search?q="+Query
    elif Referer == "bingimage":
        RefX = "https://www.bing.com/images/search?q="+Query+"&qs=HS&sc=1-0&FORM=QBLH&sp=1"
    elif Referer == "yandex":
        RefX = "https://yandex.com/search/?text="+Query
    elif Referer == "yandeximage":
        RefX = "https://yandex.com/images/search?from=tabbar&text="+Query
    elif Referer == "yahoo":
        RefX = "https://search.yahoo.com/search?p="+Query
    elif Referer == "yahooimage":
        RefX = "https://images.search.yahoo.com/search/images?p="+Query
    elif Referer == "duckduckgo":
        RefX = "https://duckduckgo.com/?q="+Query
    elif Referer == "duckduckgoimage":
        RefX = "https://duckduckgo.com/?t=h_&iax=images&ia=images&q="+Query
    elif Referer == "ecosia":
        RefX = "https://www.ecosia.org/search?&q="+Query
    elif Referer == "ecosiaimage":
        RefX = "https://www.ecosia.org/images?q="+Query
    elif Referer == "aol":
        RefX = "https://search.aol.com/aol/search?q="+Query
    elif Referer == "aolimage":
        RefX = "https://search.aol.com/aol/image?q="+Query
    elif Referer == "baidu":
        RefX = "https://www.baidu.com/s?wd="+Query
    else:
        Referer = "google"
        RefX = "https://www.google.com/search?q="+Query+"&hl=en&gl=US"
        
    if "Mac" in ua:
        VendorX = "Apple Computer, Inc."
    else:
        VendorX = "Google Inc."
    
    if "Windows" in ua:
        if "Win64" in ua:
            PlatformX = "Win64"
        elif "Windows" in ua:
            PlatformX = "Win32"
        else:
            PlatformX = "Windows"
    elif "Mac" in ua:
        PlatformX = "Macintosh"
    else:
        PlatformX = "Linux"
        
    def ad_popup(browser):
        try:
            WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.CLASS_NAME, "coupon-poplayer-modal"))) ##coupon popup
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-close"))).click()
        except:
            pass
    
    def mose(X,Y):
        pX = random.randint(100,X-100)
        pY = random.randint(100,Y-200)
        pyautogui.moveTo(pX, pY, random.randint(1,3), pyautogui.easeInOutQuad)
    
    def skrol():
        tr = random.randint(1,3)
        time.sleep(tr)
        if tr==2:
            tuen = stop//random.randint(1,10)
            browser.execute_script("scrollBy(0,-"+str(tuen)+");")                
        elif tr==3:
            tuen = stop//random.randint(1,10)
            browser.execute_script("scrollBy(0,-"+str(tuen)+");")
            tuen = stop//random.randint(1,10)
            browser.execute_script("scrollBy(0,"+str(tuen)+");")
        else:
            pyautogui.moveTo(random.randint(0,w[t]), random.randint(0,h[t]), 1, pyautogui.easeInOutQuad)

    
    def muter(Target):
        link = browser.find_elements(By.XPATH,"//a[@href]")
        random.shuffle(link)
        for a in link:
            if Target in a.get_attribute("href"):
                pyautogui.moveTo(a.location['x'],a.location['y'],random.randint(1,3), pyautogui.easeInQuad)
                time.sleep(random.randint(1,2))
                action = ActionChains(browser)
                action.move_to_element(a).click().perform()
                break
    
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--disable-extensions")
    # options.add_argument("--profile-directory=/root/x/p")
    # options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--disable-plugins-discovery")
    options.add_argument("--incognito")
    if args.Proxy:
        PROXY = args.Proxy
        ipx = PROXY.split(':')
        if PROXY.count(":")==3:
            p_json = lib.proxy_json()
            p_js = lib.proxy_js(ipx[0],ipx[1],ipx[2],ipx[3])
            pluginfile = 'proxy.zip'
            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", p_json)
                zp.writestr("background.js", p_js)
            options.add_extension(pluginfile)
        else:
            options.add_argument('--proxy-server='+PROXY)
        ipi = requests.get("http://worldtimeapi.org/api/ip/"+ipx[0]).json()
        tz_params = {'timezoneId': ipi['timezone']}
    
    # options.add_argument("user-data-dir="+PDIR)
    options.add_argument("--disable-fre")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-no-first-run")
    options.add_argument("disable-popup-blocking")
    options.add_argument("disable-notifications")
    options.add_argument("disable-gpu")
    options.add_argument("--window-size="+str(w[t])+","+str(h[t]))
    options.add_argument('user-agent=%s' % ua)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    browser = webdriver.Chrome(options=options)
    browser.delete_all_cookies()
    if args.Proxy:
        browser.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)
    stealth(browser,languages=["en-US", "en"],vendor=VendorX,platform=PlatformX,webgl_vendor="Intel Inc.",renderer="Intel Iris OpenGL Engine",fix_hairline=True,)
    # browser.get(Target)
    # browser.maximize_window()
    # browser.switch_to_active_element()
    # browser.set_window_position(0, 0)
    # browser.set_window_size(w[t], h[t])
    # browser.get(RefX)

    # browser.get("https://whoer.net/")
    # browser.get("https://2ip.io/privacy/")
    # browser.get("https://pixelscan.net/")
    # time.sleep(10)
    # ad_popup(browser)
    
    if Referer == "google":
        browser.get("https://www.google.com/?hl=en")        
        try :
            if Version == "mobile" :
                scroll = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="section-layout section-scrollbox scrollable-y scrollable-show"]')))
                browser.execute_script("arguments[0].scrollBy(0,arguments[0].scrollHeight)", scroll)
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#L2AGLb > div")))
            browser.find_element(By.CSS_SELECTOR, "#L2AGLb > div").click()
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="q"]')))
        except:
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="q"]')))
        q = browser.find_element(By.CSS_SELECTOR, 'input[name="q"]')
        q.send_keys(Query)
        q.send_keys(Keys.ENTER)
        if w[t]>1000:
            for j in range(1,2):
                mose(w[t],h[t])
        muter(Target)
    elif Referer == "bing":
        browser.get(RefX)
    else:
        browser.get(RefX)
        link = browser.find_elements(By.XPATH,"//a[@href]")
        random.shuffle(link)
        for a in link:
            if Target in a.get_attribute("href"):
                if w[t]>1000:
                    for j in range(1,2):
                        mose(w[t],h[t])
                total_height = int(browser.execute_script("return document.body.scrollHeight"))
                dly = random.randint(100,300)
                stop = random.randint(h[t],(h[t]*2))
                for j in range(1, total_height):
                    browser.execute_script("window.scrollTo(0, {});".format(j))
                    if j%dly == 0:
                        time.sleep(0.3)
                    if j == stop :
                        break
                skrol()
                browser.get(a.get_attribute("href"))
                break
                
   
    # pyautogui.moveTo(random.randint(0,w[t]), random.randint(0,h[t]), 1, pyautogui.easeInOutQuad)
    begin_time = datetime.datetime.now()
    try :
        ################## PAGE VIEW ##################
        for i in range(random.randint(5,15)):
            if w[t]>1000:
                for j in range(1,2):
                    mose(w[t],h[t])
            muter(Target)
            cek = browser.find_elements(By.CLASS_NAME, 'list-item')
            if cek :
                stop = random.randint((h[t]*2),(h[t]*10))
            else :
                stop = random.randint(h[t],(h[t]*2))

            total_height = int(browser.execute_script("return document.body.scrollHeight"))
            dly = random.randint(100,300)
            for j in range(1, total_height):
                browser.execute_script("window.scrollTo(0, {});".format(j))
                if j%dly == 0:
                    time.sleep(0.3)
                if j == stop :
                    break
            skrol()
            #time.sleep(random.randint(2,4))

        ################## CLICK ADS ##################
        link = browser.find_elements(By.XPATH,"//a[@href]")
        random.shuffle(link)
        Tads = 'auass.org'
        for a in link:
            # if 'googleads.g.doubleclick.net' in a.get_attribute("href"):
            if Tads in a.get_attribute("href"):
                a.click()
                print("sukses")
                f = open("st.txt", "w")
                f.write("")
                f.close()
                break
                
        dly = random.randint(75,200)
        total_height = int(browser.execute_script("return document.body.scrollHeight"))
        for j in range(1, total_height):
            browser.execute_script("window.scrollTo(0, {});".format(j))
            if j%dly == 0:
                time.sleep(0.3)
        skrol()
        # time.sleep(random.randint(3,7))
        
        ############PAGE VIEW IKLAN###########
        for i in range(random.randint(2,4)):
            if w[t]>1000:
                for j in range(1,2):
                    mose(w[t],h[t])
            muter(Tads)
            stop = random.randint(h[t],(h[t]*5))
            total_height = int(browser.execute_script("return document.body.scrollHeight"))
            dly = random.randint(100,300)
            for j in range(1, total_height):
                browser.execute_script("window.scrollTo(0, {});".format(j))
                if j%dly == 0:
                    time.sleep(0.3)
                if j == stop :
                    break
            skrol()
            # time.sleep(random.randint(2,4))
                    
        browser.quit()
    except:
        print("error")
        # subprocess.call(["python3.8","crawl.py","-t",Target,"-r",Referer])
        browser.quit()
    print(datetime.datetime.now()-begin_time)

