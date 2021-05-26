import { configureStore } from '@reduxjs/toolkit';
import occupantsReducer from '../features/occupants/occupantsSlice';

export const store = configureStore({
  reducer: {
    occupants: occupantsReducer
  },
});
