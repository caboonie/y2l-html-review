from flask import Flask, request, url_for, redirect
from flask import render_template
from database import get_all_swatches, create_swatch

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        print(request.files)
        
        f = request.files['front']
        f.save("static/images/"+f.filename)
        b = request.files['back']
        b.save("static/images/"+b.filename)
        create_swatch(f.filename,b.filename,request.form['yarn type'])
            
    return render_template("homepage.html")


@app.route('/allofem')
def swatch_page():
    swatches = get_all_swatches()
    return render_template("swatchpage.html",swatches=swatches)

if __name__ == '__main__':
   app.run(debug = True)

