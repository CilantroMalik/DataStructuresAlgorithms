import React from 'react';
import { OccupantsView } from "./features/occupants/OccupantsView";
import { AddOccupants } from "./features/occupants/AddOccupants";
import './App.css';

function App() {
    return (
        <div className="App">
            <div className="buttonContainer">
                <AddOccupants destination="car"/>
                <AddOccupants destination="crosswalk"/>
            </div>
            <OccupantsView />
        </div>
    )
}

export default App;
