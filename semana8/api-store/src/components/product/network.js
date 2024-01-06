import { Router } from "express";
import * as Controller from "./controller";

const productRouter = Router();

productRouter.route("/").get(Controller.list);

export default productRouter;
