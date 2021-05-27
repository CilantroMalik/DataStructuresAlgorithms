import { createSlice } from '@reduxjs/toolkit';

// for the testing build, start off with a placeholder configuration
const initialState = {
    "car": ["Infant Child", "Small animal"],
    "crosswalk": ["Elderly Adult", "Adult"]
}

// create a slice to handle adding and removing occupants
const occupantsSlice = createSlice({
    name: 'occupants',
    initialState,
    reducers: {
        addToCar(state, action) { state.car.push(action.payload) },
        addToCrosswalk(state, action) { state.crosswalk.push(action.payload) },
        removeFromCar(state, action) {
            if (state.car.findIndex(i => i === action.payload) !== -1) {
                state.car.splice(state.car.findIndex(i => i === action.payload), 1)
            }
        },
        removeFromCrosswalk(state, action) {
            if (state.crosswalk.findIndex(i => i === action.payload) !== -1) {
                state.crosswalk.splice(state.crosswalk.findIndex(i => i === action.payload), 1)
            }
        }
    }
})

export const { addToCar, addToCrosswalk, removeFromCar, removeFromCrosswalk } = occupantsSlice.actions

export default occupantsSlice.reducer