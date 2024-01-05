import express from "express";
import userRouter from "./components/user/network.js";

export const app = express();
app.use(express.json());

app.use("/api/v1/users", userRouter);
