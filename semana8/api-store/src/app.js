import express from "express";
import { apiVersion } from "./config";
import { userRouter, productRouter } from "./components";
import cors from "cors";

export const app = express();

app.use(cors());
app.use(express.json());

app.use(`${apiVersion}/users`, userRouter);
app.use(`${apiVersion}/products`, productRouter);
