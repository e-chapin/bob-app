from app import app


@app.rotue('/slack/interactive-endpoint', methods=['POST'])
def slack_interaction():
    print('An Interaction happend')
    return 'An interaction happened'