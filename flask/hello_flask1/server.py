# from flask import Flask, render_template

# app = Flask (__name__)

# print(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html", xaxis= 8, yaxis= 8)

# @app.route('/<x>')
# def oneinput(x):
#     return render_template('index.html',xaxis=8, yaxis=int(x))

# @app.route ('/<x1>/<x2>')
# def twoinput(x1,x2):
#     return render_template('index.html', xaxis=int(x1), yaxis=int(x2))
    
# if __name__=="__main__":
#     app.run(debug=True)