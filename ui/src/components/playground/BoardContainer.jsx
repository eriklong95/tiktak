import Board from "./Board";

function BoardContainer(props) {
  if (props.game === null) {
    return <p>Press 'Refresh' to load game.</p>;
  }

  function makeMove(x, y) {
    console.log("Making move...");
    const userIsA = props.game.playerA === props.user;
    const myTurn =
      (userIsA && props.turn === "A") || (!userIsA && props.turn === "B");

    if (!myTurn) {
      alert("It is not your turn.");
      return;
    }

    const myRole = userIsA ? "A" : "B";

    fetch(
      new Request(`/api/games/${props.game.id}/moves`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          x: x,
          y: y,
          occupier: myRole,
        }),
      }),
    )
      .then((response) => {
        if (response.ok) {
          console.log("Successfully made move!");
          props.refreshGame();
        } else {
          console.log("Making move failed");
        }
      })
      .catch((error) => {
        console.log(error.message);
      });
  }

  return <Board moves={props.game.moves} makeMove={makeMove} />;
}

export default BoardContainer;
