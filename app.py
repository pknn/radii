from app import app

if __name__ == "__main__":
    app.run()
    # app.run(host="127.0.0.1", port="5000", debug=True, ssl_context="adhoc")
else:
    from meinheld import server

    server.listen(("0.0.0.0", 80))
    server.run(app)
