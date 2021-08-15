from website import app

if __name__ == '__main__':
    import os

    os.environ['DISPLAY'] = ':0'

    app.run(host='0.0.0.0', port=10002)

# allow inbound rules
# sudo ufw allow 10002
