import React from 'react';
import { OccupantsView } from "./features/occupants/OccupantsView";
import { AddOccupants } from "./features/occupants/AddOccupants";
import { MoralBrake } from "./features/api/MoralBrake";
import { LightController } from "./features/light/LightController"
import './App.css';

function App() {
    return (
        <div className="App">
            <div className="buttonContainer">
                <AddOccupants destination="car"/>
                <div className="lightButton"><LightController/></div>
                <AddOccupants destination="crosswalk"/>
            </div>
            <OccupantsView/>
            <br/>
            <MoralBrake/>
        </div>
    )
}

export default App;
