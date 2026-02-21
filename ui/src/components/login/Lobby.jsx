import { useState } from "react";
import LoginPage from "./LoginPage";
import SignupPage from "./SignupPage";
import styles from "./lobby.module.css"

function Lobby(props) {
    const [status, setStatus] = useState('loggingIn'); // possible values are 'loggingIn', 'signingUp'

    if (status === 'loggingIn') {
        return (
            <div className={styles.lobby}>
                <LoginPage setLoggedIn={props.setLoggedIn} onClickSignup={() => setStatus('signingUp')} setUser={props.setUser} />
            </div>
        );
    } else if (status === 'signingUp') {
        return (
            <SignupPage onClickLogin={() => setStatus('loggingIn')} />
        );
    }
}

export default Lobby;
