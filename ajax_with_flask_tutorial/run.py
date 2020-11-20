from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('postform.html')



@app.route('/user_input', methods=['GET', 'POST'])
def user_input():

    # For POST request
    print(request.form)
    result = request.json
    print('result is ',result)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)



