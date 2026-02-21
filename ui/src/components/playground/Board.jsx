import Square from "./Square";
import styles from "./board.module.css";

function Board(props) {

    function getOccupier(x, y, moves) {
        const move = moves.find(m => m.x === x && m.y === y);
        if (move === undefined) {
            return '';
        } else {
            return move.occupier;
        }
    }

    return (
        <div>
            <div className={styles.row}>
                <Square x={0} y={0} occupier={getOccupier(0, 0, props.moves)} makeMove={() => props.makeMove(0, 0)} />
                <Square x={1} y={0} occupier={getOccupier(1, 0, props.moves)} makeMove={() => props.makeMove(1, 0)} />
                <Square x={2} y={0} occupier={getOccupier(2, 0, props.moves)} makeMove={() => props.makeMove(2, 0)} />
            </div>
            <div className={styles.row}>
                <Square x={0} y={1} occupier={getOccupier(0, 1, props.moves)} makeMove={() => props.makeMove(0, 1)} />
                <Square x={1} y={1} occupier={getOccupier(1, 1, props.moves)} makeMove={() => props.makeMove(1, 1)} />
                <Square x={2} y={1} occupier={getOccupier(2, 1, props.moves)} makeMove={() => props.makeMove(2, 1)} />
            </div>
            <div className={styles.row}>
                <Square x={0} y={2} occupier={getOccupier(0, 2, props.moves)} makeMove={() => props.makeMove(0, 2)} />
                <Square x={1} y={2} occupier={getOccupier(1, 2, props.moves)} makeMove={() => props.makeMove(1, 2)} />
                <Square x={2} y={2} occupier={getOccupier(2, 2, props.moves)} makeMove={() => props.makeMove(2, 2)} />
            </div>
        </div>
    );
}

export default Board;