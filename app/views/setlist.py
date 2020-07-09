from app import app

@app.route('/setlistreminder/create', methods=['GET'])
def hello():
    return 'Hello Slack!'