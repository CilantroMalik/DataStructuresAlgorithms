import React from 'react';
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addToCar, addToCrosswalk, removeFromCar, removeFromCrosswalk } from "./occupantsSlice";
import styles from './AddOccupants.module.css';
import '../../main.css';

export const AddOccupants = (props) => {

    const dispatch = useDispatch()
    const [removing, setRemoving] = useState(false)

    const onButtonClicked = (entity) => {
        if (removing) {
            if (props.destination === "car") { dispatch(removeFromCar(entity)) }
            else { dispatch(removeFromCrosswalk(entity)) }
        } else {
            if (props.destination === "car") { dispatch(addToCar(entity)) }
            else { dispatch(addToCrosswalk(entity)) }
        }
    }

    return (
        <div className={styles.buttonGroup}>
            <h2 style={{color: "antiquewhite", marginLeft: props.destination === "car" ? "30%" : "-9%"}}>
                Add to {props.destination === "car" ? "Car" : "Crosswalk"}
            </h2>

            <div className="flex-row" style={{justifyContent: "center"}}>
                <div style={{display: "flex", flexFlow: "column wrap", marginLeft: props.destination === "car" ? "30%" : "-9%"}}>
                    <button onClick={() => onButtonClicked("Infant Child")} className={removing ? "muted-button" : ""} style={{margin: "6px"}}>Infant Child</button>
                    <button onClick={() => onButtonClicked("Small Child")} className={removing ? "muted-button" : ""} style={{margin: "6px"}}>Small Child</button>
                    <button onClick={() => onButtonClicked("Teenage Child")} className={removing ? "muted-button" : ""} style={{margin: "6px"}}>Teenage Child</button>
                    <button onClick={() => onButtonClicked("Adult")} className={removing ? "muted-button" : ""} style={{margin: "6px"}}>Adult</button>
                </div>
                <div style={{display: "flex", flexFlow: "column wrap"}}>
                    <button onClick={() => onButtonClicked("Elderly Adult")} className={removing ? "muted-button" : ""} style={{margin: "6px"}}>Elderly Adult</button>
                    <button onClick={() => onButtonClicked("Small animal")} className={removing ? "muted-button" : ""} style={{margin: "6px"}}>Small animal</button>
                    <button onClick={() => onButtonClicked("Large animal")} className={removing ? "muted-button" : ""} style={{margin: "6px"}}>Large animal</button>
                    <button onClick={() => setRemoving(!removing)}
                            style={removing ? {margin: "6px"} : {backgroundColor: "red", borderColor: "red", margin: "6px"}}>
                        {removing ? "Add" : "Remove"}
                    </button>
                </div>
            </div>
        </div>
    )
}