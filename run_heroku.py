import os

from app import app
app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT'))