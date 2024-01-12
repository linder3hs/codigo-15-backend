import express, { type Application } from "express";
import cors from "cors";
import { userRouter, productRouter } from "./components";

const app: Application = express();
app.use(cors());
app.use(express.json());

app.use("/api/v1/users", userRouter);
app.use("/api/v1/products", productRouter);

export default app;
