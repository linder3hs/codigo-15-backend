import type { Response, Request } from "express";
import { responseSuccess, responseError } from "../../network/responses";
import { prisma } from "../../db";
import { handleResponseError } from "../../utils";
import { mapInsertProduct } from "./utils";
import { IBody } from "../../core/types";

export async function list(_req: Request, res: Response): Promise<Response> {
  try {
    const products = await prisma.product.findMany();

    return responseSuccess({ res, data: products });
  } catch (error) {
    return handleResponseError(res, error);
  }
}

export async function store(req: Request, res: Response): Promise<Response> {
  try {
    const { ok, data } = mapInsertProduct(req.body as IBody);

    if (!ok) {
      return responseError({ res, data });
    }

    const newProduct = await prisma.product.create({ data });

    return responseSuccess({ res, data: newProduct });
  } catch (error) {
    return handleResponseError(res, error);
  }
}
