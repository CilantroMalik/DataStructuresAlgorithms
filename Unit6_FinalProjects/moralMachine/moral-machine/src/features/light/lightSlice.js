import { createSlice } from '@reduxjs/toolkit';

// for the testing build, start off with a placeholder configuration
const initialState = {"green": true}

// create a slice to handle adding and removing occupants
const lightSlice = createSlice({
    name: 'light',
    initialState,
    reducers: {
        toggleLight(state, action) { state.green = action.payload }
    }
})

export const { toggleLight } = lightSlice.actions

export default lightSlice.reducer