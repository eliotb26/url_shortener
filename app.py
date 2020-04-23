from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') #base url 
def home():  #name for the route and this is normal function
    return render_template('home.html')
    

@app.route('/your-url', methods=['GET', 'POST'])
def your_url(): #name of function and route do not need to match
    if request.method =='POST':
        return render_template('your_url.html', code=request.form['code'])
    else: 
        return 'This is not valid'






