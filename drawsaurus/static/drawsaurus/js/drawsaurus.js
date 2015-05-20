var GameList = React.createClass({
    componentDidMount: function () {
        this.loadGamesFromServer();
    },
    getInitialState: function () {
        return {games: []};
    },
    loadGamesFromServer: function () {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState({games: data.results});
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    render: function () {
        var gameNodes = this.state.games.map(function (game) {
            return (
                <GameOverview data={game}>
                </GameOverview>
            );
        });
        return (
            <div className="gameList">
                {gameNodes}
            </div>
        );
    }
});


var GameOverview = React.createClass({
    render: function () {
        return (
            <div className="gameOverview">
                <h2 className="gamePK">
                    Game ID {this.props.data.pk}
                </h2>
                <span>Next turn </span>
                <span>{this.props.data.next_turn_number}</span>
            </div>
        );
    }
});

var GameDetail = React.createClass({
    componentDidMount: function () {
        this.loadGameFromServer();
    },
    getInitialState: function () {
        return {};
    },
    loadGameFromServer: function () {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState(data);
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    render: function () {
        return (
            <div className="gameDetailw">
                <h2 className="gamePK">
                    Game ID {this.state.pk}
                </h2>
                <span>Next turn </span>
                <span>{this.state.next_turn_number}</span>
            </div>
        );
    }
});