import React from 'react';
import { useSelector } from 'react-redux';
import { nanoid } from '@reduxjs/toolkit';
import styles from './OccupantsView.module.css';
import '../../main.css';

export const OccupantsView = () => {
    const carOccupants = useSelector(state => state.occupants.car)
    const crosswalkOccupants = useSelector(state => state.occupants.crosswalk)

    const carList = carOccupants.map(entity => (
        <div key={nanoid()}>
            <h3 className={styles.occupantName} key={nanoid()}>{entity}</h3>
        </div>
    ))
    const crosswalkList = crosswalkOccupants.map(entity => (
        <div key={nanoid()}>
            <h3 className={styles.occupantName}>{entity}</h3>
        </div>
    ))

    return (
        <div className="flex-row" style={{justifyContent: "center", marginTop: "10px"}}>
            <div className={styles.occupantList}>{carList}</div>
            <div className={styles.occupantList}>{crosswalkList}</div>
        </div>
    )
}