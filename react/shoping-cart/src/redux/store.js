import { configureStore } from "@reduxjs/toolkit";
import cartReducer from "./slice/StoreSlice";

export const store = configureStore({
  reducer: {
    cart: cartReducer,
  },
});