import { useState } from "react";
import Lobby from "./components/login/Lobby";
import MyPage from "./components/MyPage";

function App() {
    const [loggedIn, setLoggedIn] = useState(false);
    const [user, setUser] = useState(null);

    if (loggedIn) {
        return (
            <MyPage user={user} logout={() => setLoggedIn(false)} />
        );
    } else {
        return (
            <Lobby setLoggedIn={setLoggedIn} setUser={setUser} />
        )
    }

}

export default App;
