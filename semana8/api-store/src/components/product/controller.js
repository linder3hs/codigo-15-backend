import { responseSuccess, responseError } from "../../network/responses";
import { prisma } from "../../db";
import { mapInsertProduct } from "./utils";

export async function list(req, res) {
  try {
    const products = await prisma.product.findMany();

    responseSuccess({ res, data: products });
  } catch (error) {
    responseError({ res, data: error.message });
  }
}

export async function store(req, res) {
  try {
    const { ok, data } = mapInsertProduct(req.body);

    if (!ok) {
      return responseError({ res, data });
    }

    const newProduct = await prisma.product.create({ data });

    return responseSuccess({ res, data: newProduct });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}
