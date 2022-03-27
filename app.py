from flask import Flask, Response, request, url_for

app = Flask(__name__)

@app.route('/')
def welcome_to_flask():
    return "Welcome to Flask!"

@app.route('/hello')
def hello_from_flask():
    return "Hello from Flask!"

@app.route('/bye')
def goodbye_from_flask():
    return "Goodbye from Flask!"


@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')


@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data to the Flask app: " + data_sent, mimetype='text/plain')


@app.route('/dynamic/<word>')
def get_name(word):
    return Response("Hello " + word)


@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = "Your number squared is" + " " + str(squared)
    return line



@app.route('/sayhello/<name>')
def say_hello_page(name):
    return """
    <html>
    <head>
        <title>Simple Flask Route</title>
    </head>
    <body>
        <h1>Name Page</h1>
        <p>Hello {}!<p>
    </body>
    </html>
    """.format(name)



@app.route('/person/<name>/<int:age>')
def person(name, age):
    return """
        <html>
    <head>
        <title>Person A</title>
    </head>
    <body>
        <h1>First Person</h1>
        <p>Hello {}!</p>
        <p>You are {} year(s) old.</p>
    </body>
    </html>
    """.format(name, age)


# HOMEWORK

@app.route('/about/<name>/<int:age>')
def about(name, age):
    hello_url = url_for('hello_from_flask')
    return """
           <html>
       <head>
           <title>About you</title>
       </head>
       <body>
           <h1>About you</h1>
           <p>Hello {}!</p>
           <p>You are {} year(s) old.</p>
           <a href="{}">Click to Say Hello</a>
       </body>
       </html>
       """.format(name, age, hello_url)




if __name__ == "__main__":
    app.run(debug=True)