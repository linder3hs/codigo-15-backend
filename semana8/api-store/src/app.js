import express from "express";
import { apiVersion } from "./config";
import { userRouter, productRouter } from "./components";

export const app = express();
app.use(express.json());

app.use(`${apiVersion}/users`, userRouter);
app.use(`${apiVersion}/products`, productRouter);
