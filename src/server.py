from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods=['post'])
def success():
    if request.method =='POST':
        email =request.form["email"]
        infected_bool= request.form["infected_bool"]
        economic_impact_bool= request.form["economic_impact_bool"]

        print (email,infected_bool)
        return render_template("success.html")
    
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5006)