import { useState } from "react";
import BoardContainer from "./BoardContainer";
import GameInfo from "./GameInfo";
import styles from "./playground.module.css";

function Playground(props) {
  const [game, setGame] = useState(null);
  const [turn, setTurn] = useState(false);

  function refreshGame() {
    fetch(new Request(`/api/games/${props.gameId}`))
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setGame(data);
      })
      .catch((error) => {
        console.log(error);
      });

    fetch(new Request(`/api/games/${props.gameId}/turn`))
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setTurn(data);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  return (
    <div className={styles.playground}>
      <p>Game ID: {props.gameId}</p>
      <GameInfo
        game={game}
        turn={turn}
        refreshGame={refreshGame}
        user={props.user}
      />
      <BoardContainer
        game={game}
        turn={turn}
        refreshGame={refreshGame}
        user={props.user}
      />
      <button
        onClick={() => props.setUserMode("browsing")}
        className={styles.exitbutton}
      >
        Return to my page
      </button>
      <button onClick={refreshGame}>Refresh</button>
    </div>
  );
}

export default Playground;
