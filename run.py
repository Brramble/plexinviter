from flask import Flask, render_template, request, redirect, url_for
from modules.plex_invitation import send_plex_invitation, send_email
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_invitation', methods=['POST'])
def send_invitation():
    user_email = request.form['user_email']

    # Call the Plex invitation function with the provided user_email
    send_plex_invitation(user_email)

    # Set a message to display on the webpage
    message = f"Invitation sent and email sent successfully to {user_email}"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    #app.run(debug=True, port=3500)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
