import { Router } from "express";
import * as Controller from "./controller";

const productRouter: Router = Router();

productRouter.route("/").get(Controller.list);
productRouter.route("/").post(Controller.store);

export default productRouter;
