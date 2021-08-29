import os

os.environ['DISPLAY'] = ':0'

from website import app

if __name__ == '__main__':
    # port = 10002
    # from selenium import webdriver
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument(f"--remote-debugging-port={port}")
    #
    # browser = webdriver.Chrome(chrome_options=chrome_options)
    # browser.get('https://google.com/')

    app.run(host='0.0.0.0', port=port)

# allow inbound rules
# sudo ufw allow 10002
