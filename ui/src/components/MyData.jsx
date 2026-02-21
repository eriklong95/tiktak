import styles from "./mydata.module.css";
import useData from "../hooks/useData";

function MyData(props) {
  const userData = useData(`/api/users/${props.username}`);

  return (
    <div className={styles.userdatapanel}>
      <h2 className={styles.heading}>Data about me</h2>
      <div className={styles.field}>
        <label>Username</label>
        <input
          type="text"
          value={props.username}
          readOnly
          className={styles.valuebox}
        />
      </div>
      <div className={styles.field}>
        <label>Rank</label>
        <input
          type="text"
          value={userData === null ? "" : userData.rank}
          readOnly
          className={styles.valuebox}
        />
      </div>
    </div>
  );
}

export default MyData;
