console.log("Entered");

var UserBox = React.createClass({
    componentDidMount: function () {
        this.loadUsersFromServer();
    },
    getInitialState: function () {
        return {users: []};
    },
    loadUsersFromServer: function () {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState({users: data.results});
                console.log(this.state);
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    render: function () {
        return (
            <div className="usersBox">
                <h1>Users</h1>
                <UserList users={this.state.users} />
            </div>
        );
    }
});

var UserList = React.createClass({
    render: function () {
        console.log(this.props.users);
        var userNodes = this.props.users.map(function (user) {
            return (
                <User data={user}>
                </User>
            );
        });
        return (
            <div className="userList">
                {userNodes}
            </div>
        );
    }
});

var User = React.createClass({
    render: function () {
        return (
            <div className="user">
                <h2 className="userName">
                    {this.props.data.username}
                </h2>
                <span>{this.props.data.email}</span>
            </div>
        );
    }
});

console.log("Starting");

React.render(
    <UserBox url="/users/?format=json" />,
    document.getElementById('content')
);

console.log("Started");