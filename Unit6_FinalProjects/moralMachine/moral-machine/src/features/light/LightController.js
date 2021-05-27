import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { toggleLight } from "./lightSlice";
import '../../main.css';

export const LightController = () => {
    const light = useSelector(state => state.light.green)
    const dispatch = useDispatch()

    const onLightClicked = () => {
        dispatch(toggleLight(!light))
    }

    return (
        <button style={light ? {borderColor: "forestgreen", backgroundColor: "forestgreen", marginLeft: "27%"} : {borderColor: "indianred", backgroundColor: "indianred", marginLeft: "27%"}} onClick={onLightClicked} title="click to change light">{light ? "Green Light" : "Red Light"}</button>
    )
}