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
        // TODO: get the url using hyperlinked pks
        var url = "/games/"+this.props.data.pk+"/";
        return (
            <div className="gameOverview">
                <h2 className="gamePK">
                    <a href={url}>Game ID {this.props.data.pk}</a>
                </h2>
                <span>Next turn </span>
                <span>unknown</span>
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
            <div className="gameDetail">
                <h2 className="gamePK">
                    Game ID {this.state.pk}
                </h2>
                <span>Next turn </span>
                <span>unknown</span>
            </div>
        );
    }
});