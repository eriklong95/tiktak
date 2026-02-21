import { useState } from "react";
import styles from "./signuppage.module.css";

function SignupPage(props) {
  const [username, setUsername] = useState("");
  const [status, setStatus] = useState("signingUp"); // possible values are 'signingUp', 'success', 'failure'
  const [errorMessage, setErrorMessage] = useState("");

  function createUser(event, name) {
    event.preventDefault();
    fetch(
      new Request(`/api/users`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(name),
      }),
    )
      .then((response) => {
        if (response.ok) {
          setStatus("success");
        } else if (response.status === 403) {
          setUsername("");
          setStatus("failure");
          setErrorMessage("Username already taken");
        } else {
          console.log(response.status);
          setUsername("");
          setStatus("failure");
          setErrorMessage("Unknown error");
        }
      })
      .catch((error) => {
        console.log(error);
        setStatus("failure");
        setErrorMessage(error.message);
      });
  }

  if (status === "success") {
    return (
      <>
        <p>You are now signed up, '{username}'. Welcome on board!</p>
        <button onClick={props.onClickLogin}>Go to login page</button>
      </>
    );
  } else {
    return (
      <div className={styles.signuppage}>
        <div className={styles.signupform}>
          <h1>Join tiktak!</h1>
          <div className={styles.userfocus}>
            <p>Choose a username</p>
            <form onSubmit={(e) => createUser(e, username)}>
              <input
                value={username}
                onChange={(e) => {
                  setUsername(e.target.value);
                  setStatus("signingUp");
                }}
                className={styles.inputfield}
              />
              <button className={styles.signupbutton}>Sign up</button>
            </form>
          </div>
          <dialog open={status === "failure"}>
            <p>{errorMessage}</p>
            <button onClick={() => setStatus("signingUp")}>OK</button>
          </dialog>
        </div>
        <div className={styles.loginlink}>
          <label>Already on tiktak?</label>
          <button
            onClick={props.onClickLogin}
            className={styles.gotologinbutton}
          >
            Log in
          </button>
        </div>
      </div>
    );
  }
}

export default SignupPage;
