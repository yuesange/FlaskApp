#we are going to use flask

from flask import Flask, render_template, request



app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def hello_world():
    return render_template('base.html') 

@app.route("/entries")
def entries():
    return "Here are all my entries"     

@app.route("/cocktails", methods=['GET']) 
def find_cocktails():
    data = request.args.get('email')
    return render_template('cocktail.html',email=data,something="nacho friday!")

@app.route("/clothingstore", methods=['POST'])
def go_shopping():
    data = request.form['email'] 
    #details ={name:"sdd",difficulty:'""',img:""}
    #cocktails = [{name:"",picture:""},{name:"",picture:""},]
    return render_template('poe.html',
      email=data, 
      something="nacho friday!")

@app.route("/art")
def see_art():
    return "Art"        

@app.route("/coffee")
def hot_coffee():
    return "barista"        



if __name__ == "__main__": 
	app.run( 
		host='0.0.0.0', 
		port=5565
	)