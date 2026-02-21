import styles from "./square.module.css";

function Square(props) {
    const occupier = props.occupier;

    return (
        <button className={styles.square} onClick={props.makeMove}>
            {occupier}
        </button>
    );
}

export default Square;