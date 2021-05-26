import React from 'react';
import { addToCar, addToCrosswalk, removeFromCar, removeFromCrosswalk } from "./occupantsSlice";
import styles from './AddOccupants.module.css';
import '../../main.css';

export const AddOccupants = (props) => {

    // TODO actually implement adding and removing functionality on button clicks

    return (
        <div className={styles.buttonGroup}>
            <h2 style={{color: "antiquewhite", marginLeft: props.destination === "car" ? "11%" : "-17%"}}>
                Add to {props.destination === "car" ? "Car" : "Crosswalk"}
            </h2>

            <div className="flex-row" style={{justifyContent: "center"}}>
                <div style={{display: "flex", flexFlow: "column wrap", marginLeft: props.destination === "car" ? "11%" : "-17%"}}>
                    <button style={{margin: "6px"}}>Infant Child</button>
                    <button style={{margin: "6px"}}>Small Child</button>
                    <button style={{margin: "6px"}}>Teenage Child</button>
                    <button style={{margin: "6px"}}>Adult</button>
                </div>
                <div style={{display: "flex", flexFlow: "column wrap"}}>
                    <button style={{margin: "6px"}}>Elderly Adult</button>
                    <button style={{margin: "6px"}}>Small Animal</button>
                    <button style={{margin: "6px"}}>Large Animal</button>
                    <button style={{backgroundColor: "red", borderColor: "red", margin: "6px"}}>Remove</button>
                </div>
            </div>
        </div>
    )
}