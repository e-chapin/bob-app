import os

from app import app
app.run(debug=False, port=os.environ.get('PORT'))