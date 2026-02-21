import { useState } from "react";
import styles from "./loginpage.module.css";

function LoginPage(props) {
  const [textInput, setTextInput] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [errorDialogOpen, setErrorDialogOpen] = useState(false);

  async function handleLoginAttempt(event, username, setLoggedIn, setUser) {
    event.preventDefault();

    fetch(
      new Request(`/api/users/${username}`, {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      }),
    )
      .then((response) => {
        if (response.ok) {
          setUser(username);
          setLoggedIn(true);
        } else {
          setLoggedIn(false);
          setUser("");
          setErrorMessage("Login failed");
          setErrorDialogOpen(true);
        }
      })
      .catch((error) => {
        console.log(error);
        setErrorMessage(error.message);
        setErrorDialogOpen(true);
      });
  }

  return (
    <div className={styles.loginpage}>
      <div className={styles.loginform}>
        <h1>Welcome to tiktak!</h1>
        <div className={styles.userfocus}>
          <p>Log in to start playing.</p>
          <form
            onSubmit={(e) =>
              handleLoginAttempt(e, textInput, props.setLoggedIn, props.setUser)
            }
          >
            <input
              type="text"
              value={textInput}
              onChange={(e) => setTextInput(e.target.value)}
              className={styles.inputfield}
            />
            <button className={styles.loginbutton}>Login</button>
          </form>
        </div>
        <dialog open={errorDialogOpen}>
          <p>{errorMessage}</p>
          <button onClick={() => setErrorDialogOpen(false)}>OK</button>
        </dialog>
      </div>
      <div className={styles.signuplink}>
        <label>Not on tiktak yet?</label>
        <button onClick={props.onClickSignup} className={styles.signupbutton}>
          Sign up
        </button>
      </div>
    </div>
  );
}

export default LoginPage;
