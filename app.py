from flask import Flask, render_template
from flask import Flask, render_template, request, flash, redirect
from scripts.sendEmail import sendEmail
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('index.html', posts=[])

@app.route('/about')
def about():
    return render_template('about.html', posts=[])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            sendEmail(name, email, message)  # Call the Gmail API function
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send message: {e}', 'danger')
        return redirect('/contact')
    return render_template('contact.html', posts=[])

if __name__ == "__main__":
    app.run(debug=True, port=3000)
