from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey Chris -- Hello, World!'

# Full form data is needed to process new user
# Use email to ensure unique
# If not unique, delete record and notify user
# If unique, create new record and perform the following:
# - Determine number of record matches
# - Add number of records and other form data into an LLM prompt
# - Send prompt to LLM and get response
# - Take response and send user an email with recruiting report


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
