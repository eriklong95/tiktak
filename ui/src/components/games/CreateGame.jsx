import { useState } from "react";
import CreateGameDialog from "./CreateGameDialog";
import CreateGameInfoBox from "./CreateGameInfoBox";
import styles from './creategame.module.css';

function CreateGame(props) {
    const [dialogOpen, setDialogOpen] = useState(false);
    const [infoOpen, setInfoOpen] = useState(false);
    const [infoMessage, setInfoMessage] = useState('');

    return (
        <>
            <button onClick={() => setDialogOpen(true)} className={styles.newgamebutton}>Create a new game!</button>
            <CreateGameDialog
                open={dialogOpen}
                setDialogOpen={setDialogOpen}
                user={props.user}
                setInfoOpen={setInfoOpen}
                setInfoMessage={setInfoMessage}
            />
            <CreateGameInfoBox open={infoOpen} message={infoMessage} setOpen={setInfoOpen} refreshGameList={props.refreshGameList} />
        </>
    );
}

export default CreateGame;
