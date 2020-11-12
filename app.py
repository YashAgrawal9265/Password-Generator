from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        passLength = request.form.get('passLength')
        passSymbols = request.form.get('passSymbols')
        passNumbers = request.form.get('passNumbers')
        passLower = request.form.get('passLower')
        passUpper = request.form.get('passUpper')
        print(f"{passLength}, {passSymbols}, {passNumbers}, {passLower}, {passUpper}");
        return redirect(url_for('home'))

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)