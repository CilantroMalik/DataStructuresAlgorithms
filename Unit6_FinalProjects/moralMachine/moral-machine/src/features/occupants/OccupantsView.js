import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { nanoid } from '@reduxjs/toolkit'
import styles from './OccupantsView.module.css';
import '../../main.css';

export const OccupantsView = () => {
    const carOccupants = useSelector(state => state.car)
    const crosswalkOccupants = useSelector(state => state.crosswalk)

    const carList = carOccupants.map(entity => (
        <div className={styles.fadeIn}>
            <h3>{entity}</h3>
        </div>
    ))
    const crosswalkList = crosswalkOccupants.map(entity => (
        <div className={styles.fadeIn}>
            <h3 key={nanoid()}>{entity}</h3>
        </div>
    ))

    return (
        <div style={{display: "flex"}}>
            <div>{carList}</div>
            <div>{crosswalkList}</div>
        </div>
    )
}