import React, { useState } from 'react';
import { useSelector } from 'react-redux';

export const MoralBrake = () => {

    const carOccupants = useSelector(state => state.occupants.car)
    const crosswalkOccupants = useSelector(state => state.occupants.crosswalk)
    const light = useSelector(state => state.light.green)
    const [result, setResult] = useState("(Decision will appear here once simulation is run.)")

    // handle a simulate button click -> make an XHR to fetch data from the API
    const onSimulateClicked = () => {
        let xmlHttp = new XMLHttpRequest();
        // retrieve the decision from the backend, which will return a response as a string in JSON format
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
                setResult(JSON.parse(xmlHttp.responseText).decision);
        }
        let carQuery = "";  // build up the query of occupant IDs based on their names, character by character
        for (const o of carOccupants) {  // map long-form names to IDs
            if (o === "Infant Child") { carQuery += "0" }
            else if (o === "Small Child") { carQuery += "1" }
            else if (o === "Teenage Child") { carQuery += "2" }
            else if (o === "Adult") { carQuery += "3" }
            else if (o === "Elderly Adult") { carQuery += "4" }
            else if (o === "Small animal") { carQuery += "5" }
            else if (o === "Large animal") { carQuery += "6" }
        }
        let crosswalkQuery = "";  // same procedure for crosswalk
        for (const o of crosswalkOccupants) {
            if (o === "Infant Child") { crosswalkQuery += "0" }
            else if (o === "Small Child") { crosswalkQuery += "1" }
            else if (o === "Teenage Child") { crosswalkQuery += "2" }
            else if (o === "Adult") { crosswalkQuery += "3" }
            else if (o === "Elderly Adult") { crosswalkQuery += "4" }
            else if (o === "Small animal") { crosswalkQuery += "5" }
            else if (o === "Large animal") { crosswalkQuery += "6" }
        }
        // make the API call with the parameters
        xmlHttp.open("GET", `http://localhost:8888/api/selfDriving/moralBrake?car=${carQuery}&crosswalk=${crosswalkQuery}&green=${light ? "1" : "0"}`, true); // true for asynchronous
        xmlHttp.send(null);
    }

    // simple layout: just the button and a text block to display the algorithm's decision
    return (
        <>
            <button onClick={onSimulateClicked} className="accent-button">Simulate Self-Driving Car</button>
            <h3 style={{border: "2px solid antiquewhite", borderRadius: "12px", padding: "5px", margin: "20px", color: "antiquewhite"}}>{result}</h3>
        </>
    )
}