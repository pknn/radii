from meinheld import server

from app import app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=True)
else:
    server.listen(("0.0.0.0", 80))
    server.run(app)
