import React from 'react';
import { OccupantsView } from "./features/occupants/OccupantsView";
import { AddOccupants } from "./features/occupants/AddOccupants";
import './App.css';

function App() {
    return (
        <div className="App">
            <AddOccupants destination="car"/>
            <OccupantsView />
        </div>
    )
}

export default App;
