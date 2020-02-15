from flask_youtube_search import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=2000, debug=True)