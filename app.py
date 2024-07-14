from routes import app

app.secret_key = 'your_secret_key'

app.secret_key = 'your_secret_key'
if __name__ == "__main__":
    app.run(debug=True, port=6901)
