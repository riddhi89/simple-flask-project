import flask


app = flask.Flask(__name__)


@app.route("/users")
def list_users():
    """
    List all users
    ---
    get:
        summary: Lists all users
        description: List all the users
        tags:
          - Users
        operationId: list_users
        responses:
            '200':
                description: A list of all users
                schema: list_all_users
    """
    users_dict = [
        {'name': 'jack', 'email': 'jack@gmail.com', 'age': 25},
        {'name': 'jill', 'email': 'jill@gmail.com', 'age': 28},
    ]
    return flask.jsonify(users=users_dict)


@app.route("/users/<string:username>")
def get_user_details(username):
    """
    Get user details
    ---
    get:
        summary: Get user details
        description: Returns details of specified user
        tags:
          - Users
        operationId: get_user
        parameters:
          - name: username
            in: path
            required: true
            description: Name of the user
            schema:
                type: string
        responses:
            '200':
                description: User details
                schema: get_user_details
    """
    user_details = {
        'name': username, 'email': '{}@gmail.com'.format(username), 'age': 28
    }
    return flask.jsonify(user=user_details)


if __name__ == '__main__':
    app.run()
