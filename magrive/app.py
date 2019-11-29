from flask import Flask, redirect, url_for, request , render_template
import onlypy2 as py_script

using = False

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('froala_index.html')

@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
	global using
	if request.method == 'POST':
		if not using:
			using = True
			if request.form['pin'] == 'h1p4': 
				magnet_link = request.form['magnet_link'] 
				email_id = request.form['email']
				share_link = 'Check the given magnet link'
				try:
					share_link = py_script.process_link(magnet_link, email_id)
				except:
					print("some error")
				using = False 
				return str(share_link)
			else:
				using = False
				return "Only for authorised people :), Please don't waste your time guessing the pin."

		else:
			return "Sorry, the server is in use, Please try after some time ;)"

if __name__ == '__main__': 
	app.run(host="0.0.0.0", port=80, threaded = True) 
