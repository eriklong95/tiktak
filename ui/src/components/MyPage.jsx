import MyData from "./MyData";
import MyGames from "./MyGames";
import Playground from "./playground/Playground";
import { useState } from "react";
import styles from './mypage.module.css';

function MyPage(props) {
    const [userMode, setUserMode] = useState('browsing') // possible values: 'browsing', 'playing'
    const [activeGameId, setActiveGameId] = useState(null);

    if (userMode === 'browsing') {
        return (
            <div className={styles.mypage}>
                <MyData username={props.user} />
                <MyGames user={props.user} setUserMode={setUserMode} setActiveGameId={setActiveGameId} />
                <button onClick={props.logout} className={styles.logoutbutton}>Log out</button>
            </div>
        );
    } else {
        return (
            <div className={styles.mypage}>
                <Playground setUserMode={setUserMode} gameId={activeGameId} user={props.user} />
            </div>
        );
    }
}

export default MyPage;
