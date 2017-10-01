from factory import create_app


app = create_app()


@app.route(app.config['APPLICATION_ROOT'] + '/')
def index():
    return "Flask/Postgres API"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
