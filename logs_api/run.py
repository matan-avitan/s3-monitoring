from logs_api.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8080, debug=True, threaded=True)
