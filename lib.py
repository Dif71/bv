import random
import numpy as np
import bezier

def proxy():
    prxs = ['','']
    random.shuffle(prxs)
    PROXY = uas[0]
    return PROXY

def ua(Version):
    if Version=="mobile":
        uas = ["Mozilla/5.0 (iPad; CPU OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.85 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPod; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.85 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Android 12; Mobile; rv:68.0) Gecko/68.0 Firefox/96.0","Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:96.0) Gecko/96.0 Firefox/96.0","Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.85 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/96.0 Mobile/15E148 Safari/605.1.15","Mozilla/5.0 (iPad; CPU OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPod touch; CPU iPhone 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36 OPR/63.3.3216.58675","Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36 OPR/63.3.3216.58675","Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36 OPR/63.3.3216.58675","Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36 EdgA/97.0.1072.69","Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36 EdgA/97.0.1072.69","Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36 EdgA/97.0.1072.69","Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36 EdgA/97.0.1072.69","Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 EdgiOS/97.1072.69 Mobile/15E148 Safari/605.1.15","Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Mobile Safari/537.36 Edge/40.15254.603","Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/96.0 Mobile/15E148 Safari/605.1.15","Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/96.0 Mobile/15E148 Safari/605.1.15","Mozilla/5.0 (iPod touch; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/96.0 Mobile/15E148 Safari/605.1.15"]
    else :
        uas = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (X11; Linux i686; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:91.0) Gecko/20100101 Firefox/91.0","Mozilla/5.0 (X11; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0","Mozilla/5.0 (Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/97.0.1072.69","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/97.0.1072.69","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 OPR/83.0.4254.16","Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 OPR/83.0.4254.16","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 OPR/83.0.4254.16","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 OPR/83.0.4254.16","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15","Mozilla/5.0 (X11; CrOS x86_64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36","Mozilla/5.0 (X11; CrOS armv7l 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36","Mozilla/5.0 (X11; CrOS aarch64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36","Mozilla/5.0 (X11; CrOS x86_64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36","Mozilla/5.0 (X11; CrOS armv7l 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36","Mozilla/5.0 (X11; CrOS aarch64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15","Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Vivaldi/4.3","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/97.0.1072.69","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/97.0.1072.69","Mozilla/5.0 (Windows NT 10.0; WOW64;Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Vivaldi/4.3","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Vivaldi/4.3"]
    random.shuffle(uas)
    UA = uas[0]
    return UA

def bezier_mouse(location, size, panelHeight): ##move mouse to middle of element
    x, relY = location["x"], location["y"]
    absY = relY + panelHeight
    w, h = size["width"], size["height"]
    wCenter = w/2
    hCenter = h/2
    xCenter = int(wCenter + x)
    yCenter = int(hCenter + absY)

    start = pyautogui.position()
    end = xCenter, yCenter

    x2 = (start[0] + end[0])/2 #midpoint x
    y2 = (start[1] + end[1]) / 2 ##midpoint y

    control1X = (start[0] + x2)/2
    control1Y = (end[1] + y2) / 2

    control2X = (end[0] + x2) / 2
    control2Y = (start[1] + y2) / 2

    # Two intermediate control points that may be adjusted to modify the curve.
    control1 = control1X, y2 ##combine midpoints to creat perfect curve
    control2 = control2X, y2


    # Format points to use with bezier
    control_points = np.array([start, control1, control2, end])
    points = np.array([control_points[:, 0], control_points[:, 1]])  # Split x and y coordinates
    # You can set the degree of the curve here, should be less than # of control points
    degree = 3
    # Create the bezier curve
    curve = bezier.Curve(points, degree)

    curve_steps = 50  # How many points the curve should be split into. Each is a separate pyautogui.moveTo() execution
    delay = 0.003  # Time between movements. 1/curve_steps = 1 second for entire curve

    # Move the mouse
    for j in range(1, curve_steps + 1):
        # The evaluate method takes a float from [0.0, 1.0] and returns the coordinates at that point in the curve
        # Another way of thinking about it is that i/steps gets the coordinates at (100*i/steps) percent into the curve
        x, y = curve.evaluate(j / curve_steps)
        pyautogui.moveTo(x, y)  # Move to point in curve
        pyautogui.sleep(delay)  # Wait delay

def proxy_json():
    manifest_json = """
    {
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
    }
    """
    return manifest_json
    
def proxy_js(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS):
    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
            username: "%s",
            password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
    return background_js
        
        
        
        
        
        

"""
def roxy():
    from fp.fp import FreeProxy
    proxy = FreeProxy(timeout=0.1).get()
    proxy = proxy.replace("http://","")
    print(proxy)
def proxy():
    key = '3MHXi8EN330DSWbR0GJGzkPW5vFLDMgX'
    conn = http.client.HTTPSConnection("api.webscrapingapi.com")
    conn.request("GET", "/v1?api_key=" + key + "&url=https%3A%2F%2Fapi.ipify.org%2F%3Fformat%3Djson&device=desktop&proxy_type=residential")
    res = conn.getresponse()
    data = res.read()
    ips = data.decode("utf-8")
    jip = json.loads(ips)
    print(jip['ip'] + ":55443")
"""
