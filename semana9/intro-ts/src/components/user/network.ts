import { Router } from "express";
import * as Controller from "./controller.js";

const userRouter: Router = Router();

userRouter.route("/").get(Controller.list);
userRouter.route("/:id").get(Controller.getById);
userRouter.route("/").post(Controller.store);
userRouter.route("/:id").put(Controller.update);
userRouter.route("/:id").delete(Controller.destroy);

export default userRouter;
