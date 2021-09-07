from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'It aint a secret if everyone knows about it!'


@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:    
        session['counter'] = 0
    return render_template('index.html',counter=session['counter'])

@app.route('/destroy_session')
def destroy():
    session.pop('counter')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)