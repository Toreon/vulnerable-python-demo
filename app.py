import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = False

def html_start():
    html = '''<html>
    <head><title>DevSecOps demo</title></head>
    <body>
    '''
    return html

def html_end():
    html = '''    </body>
</html>'''
    return html

@app.route('/', methods=['GET'])
def loginform():
    html_form = '''

        <h1>Log in</h1>

        <form action="./authenticate/" method="post">
            Username <input name="user_name" type="text" /><br />
            Password <input name="user_password" type="password" /><br />
            <input type="submit" value="Log in">
        </form>

    '''
    return html_start() + html_form + html_end()

@app.route('/authenticate/', methods=['POST'])
def verify_password():

    super_secret_password = "R5$s9*!k_959h2wvligw40*-+27Q4"
    
    html_response = "<h1>Checking login for " + request.form["user_name"] + "</h1>"

    if(request.form["user_password"] != super_secret_password):
        html_response+="Wrong password"
    else:
        html_response+="Correct password"
    
    html_response+='''<br />Click <a href="/">here</a> to return to the login page'''

    return html_start() + html_response + html_end()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8181)