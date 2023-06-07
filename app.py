from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        length = int(request.form['length'])
        include_uppercase = 'uppercase' in request.form
        include_lowercase = 'lowercase' in request.form
        include_numbers = 'numbers' in request.form
        include_special_chars = 'special_chars' in request.form

        password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)

        return render_template('index.html', password=password)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
