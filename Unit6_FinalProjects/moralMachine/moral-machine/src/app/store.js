import { configureStore } from '@reduxjs/toolkit';
import occupantsReducer from '../features/occupants/occupantsSlice';
import lightReducer from '../features/light/lightSlice'

export const store = configureStore({
  reducer: {
    occupants: occupantsReducer,
    light: lightReducer
  },
});
