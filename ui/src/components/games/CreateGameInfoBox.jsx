function CreateGameInfoBox(props) {
    function onOk() {
        props.setOpen(false);
        props.refreshGameList();
    }

    return (
        <dialog open={props.open}>
            <section>
                {props.message}
            </section>
            <button onClick={onOk}>OK</button>
        </dialog>
    );
}

export default CreateGameInfoBox;
