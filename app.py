from flask import Flask

# WSGI Application
app=Flask(__name__)

#Decorator
@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/members')
def members():
    return 'Welcome Guys'

if __name__=='__main__':
    app.run(debug=True)