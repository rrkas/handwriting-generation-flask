if __name__ == '__main__':
    from selenium import webdriver
    browser = webdriver.Chrome('/usr/bin/chromedriver')
    browser.get('https://google.com/')

    from website import app
    app.run(host='0.0.0.0', port=10002)

# allow inbound rules
# sudo ufw allow 10002
