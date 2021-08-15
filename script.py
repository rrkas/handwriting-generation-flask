if __name__ == '__main__':
    import os

    os.environ['DISPLAY'] = ':0'

    from install_package import install
    install('flask')

    from website import app
    app.run(host='0.0.0.0', port=10002)

# allow inbound rules
# sudo ufw allow 10002
