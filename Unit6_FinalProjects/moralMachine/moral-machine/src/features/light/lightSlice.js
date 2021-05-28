import { createSlice } from '@reduxjs/toolkit';

// for the testing build, start off with a placeholder configuration
const initialState = {"green": true} // make an object since primitive types don't interact well with Immer

// create a slice to track whether the light is red or green, with a single method to toggle the state
const lightSlice = createSlice({
    name: 'light',
    initialState,
    reducers: {
        toggleLight(state, action) { state.green = action.payload }
    }
})

export const { toggleLight } = lightSlice.actions

export default lightSlice.reducer