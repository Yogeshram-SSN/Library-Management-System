from website import create_app

app = create_app()
app.secret_key = 'very_much_secret'

if __name__ == '__main__':
    app.run(debug=True, port=3000)
