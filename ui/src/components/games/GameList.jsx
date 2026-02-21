import GameListItem from "./GameListItem";

function GameList(props) {
    return (
        <ul>
            {props.gameIds.map(i =>
                <GameListItem gameId={i} key={i}
                    setUserMode={props.setUserMode}
                    openGame={() => props.openGame(i)}
                />
            )}
        </ul>
    );
}

export default GameList;