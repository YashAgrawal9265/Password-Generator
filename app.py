from flask import Flask, redirect, url_for, render_template, request, flash
import string
import random

lowerCaseCharacter = string.ascii_lowercase
upperCaseCharacter = string.ascii_uppercase
numericDigits = string.digits
specialSymbols= string.punctuation

app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        passLength = request.form.get('passLength')
        passSymbols = request.form.get('passSymbols')
        passNumbers = request.form.get('passNumbers')
        passLower = request.form.get('passLower')
        passUpper = request.form.get('passUpper')

        # Algorithm for generation password
        password = []
        if passSymbols == 'on':
            password.extend(specialSymbols)
            password.extend(lowerCaseCharacter)
            password.extend(upperCaseCharacter)
            password.extend(numericDigits)
        else:   
            password.extend(lowerCaseCharacter)
            password.extend(upperCaseCharacter)
            password.extend(numericDigits)

        password=random.sample(password,int(passLength))
        newPassword = "".join(password)
        # print(f"{passLength}, {passSymbols}, {passNumbers}, {passLower}, {passUpper}");
        return render_template('index.html', newPassword= newPassword)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)