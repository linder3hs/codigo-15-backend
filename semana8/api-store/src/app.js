import express from "express";
import { apiVersion } from "./config";
import { userRouter } from "./components";

export const app = express();
app.use(express.json());

app.use(`${apiVersion}/users`, userRouter);
