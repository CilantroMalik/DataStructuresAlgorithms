import React, { useState } from 'react';
import { useSelector } from 'react-redux';

export const MoralBrake = () => {

    const carOccupants = useSelector(state => state.occupants.car)
    const crosswalkOccupants = useSelector(state => state.occupants.crosswalk)
    const light = useSelector(state => state.light.green)
    const [result, setResult] = useState("(Decision will appear here once simulation is run.)")

    const onSimulateClicked = () => {
        let xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
                setResult(JSON.parse(xmlHttp.responseText).decision);
        }
        let carQuery = "";
        for (const o of carOccupants) {
            if (o === "Infant Child") { carQuery += "0" }
            else if (o === "Small Child") { carQuery += "1" }
            else if (o === "Teenage Child") { carQuery += "2" }
            else if (o === "Adult") { carQuery += "3" }
            else if (o === "Elderly Adult") { carQuery += "4" }
            else if (o === "Small animal") { carQuery += "5" }
            else if (o === "Large animal") { carQuery += "6" }
        }
        let crosswalkQuery = "";
        for (const o of crosswalkOccupants) {
            if (o === "Infant Child") { crosswalkQuery += "0" }
            else if (o === "Small Child") { crosswalkQuery += "1" }
            else if (o === "Teenage Child") { crosswalkQuery += "2" }
            else if (o === "Adult") { crosswalkQuery += "3" }
            else if (o === "Elderly Adult") { crosswalkQuery += "4" }
            else if (o === "Small animal") { crosswalkQuery += "5" }
            else if (o === "Large animal") { crosswalkQuery += "6" }
        }
        xmlHttp.open("GET", `http://localhost:8888/api/selfDriving/moralBrake?car=${carQuery}&crosswalk=${crosswalkQuery}&green=${light ? "1" : "0"}`, true); // true for asynchronous
        xmlHttp.send(null);
    }

    return (
        <>
            <button onClick={onSimulateClicked} className="accent-button">Simulate Self-Driving Car</button>
            <h3 style={{border: "2px solid antiquewhite", borderRadius: "12px", padding: "5px", margin: "20px", color: "antiquewhite"}}>{result}</h3>
        </>
    )
}