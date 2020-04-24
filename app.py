from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path 
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'hashdfldjl'#securly send messages to user so others cannot snoop in and see this info
  #make it long hard key that cannot be exposed. 

@app.route('/') #base url 
def home():  #name for the route and this is normal function
    return render_template('home.html')
    

@app.route('/your-url', methods=['GET', 'POST'])
def your_url(): #name of function and route do not need to match
    if request.method =='POST':
        urls= {} #empty dict

        if os.path.exists('urls.json'):   #check to see if exits so cannot change it
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys(): #checks if in the keys in dict
            flash('That short name has already been taken. Please select another name.')
            return redirect(url_for('home')) #should redirect back to home 
            #then able to save additional information if not already used 
        
        if 'url' in request.form.keys(): #goes through forms key dict and searches for 'url'
            urls[request.form['code']] = {'url':request.form['url']}  #grab code for key, then grab the url user passed in        else:
        else:
            f = request.files['file']
            #make sure files are not the same name so know that code file name will be unique 
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('/Users/eliot/Desktop/url_shortener' + full_name) #decide where to save the file  with this specific name
            urls[request.form['code']] = {'file':full_name} #saves file for this code 
            


        with open('urls.json', 'w') as url_file:  #opens file and write in file 'w' and only move forward if can open file named url_file
            json.dump(urls,url_file) #saves in url_file

        return render_template('your_url.html', code=request.form['code'])
    else:  #detects if a get 
        #return render_template('/') #renders the home 
        return redirect(url_for('home'))  #redirects to the home page by calling the function






