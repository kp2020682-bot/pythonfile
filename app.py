from flask import Flask, request, jsonify

app = Flask(__name__)
users = []

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return '''
        <h2>Add users</h2>
        <form method="POST">
            Name: <input type="text" name="name"><br><br>
            Age: <input type="text" name="age"><br><br>
            <button type="submit">Submit</button>
        </form>
        '''

    data = {
        "name": request.form.get('name'),
        "age": request.form.get('age')
    }

    users.append(data)

    return "<h3>User Added! <a href='/users'>See Users</a></h3>"


@app.route('/users')
def get_users():
    return jsonify(users)


@app.route('/delete-user/<int:index>')
def delete_user(index):
    if index < len(users):
        users.pop(index)
        return "Deleted"
    return "Invalid index"


if __name__ == '__main__':
    app.run( debug=True)