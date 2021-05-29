import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { toggleLight } from "./lightSlice";
import '../../main.css';

export const LightController = () => {
    // need to fetch the current state of the light as well as be able to change it
    const light = useSelector(state => state.light.green)
    const dispatch = useDispatch()

    // simply dispatch an action to toggle the light to the opposite of its current boolean state
    const onLightClicked = () => {
        dispatch(toggleLight(!light))
    }

    // display a button that has different style amd text depending on the current light color
    return (
        <button style={{borderColor: (light ? "forestgreen" : "indianred"), backgroundColor: (light ? "forestgreen" : "indianred"), marginLeft: "27%"}} onClick={onLightClicked} title="click to change light">{light ? "Green Light" : "Red Light"}</button>
    )
}