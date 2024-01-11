import express, { type Application, Request, Response } from "express";
import cors from "cors";

const app: Application = express();
app.use(cors());

app.get("/", (req: Request, res: Response): Response => {
  return res.json({
    message: "Hola mundo",
  });
});

export default app;
