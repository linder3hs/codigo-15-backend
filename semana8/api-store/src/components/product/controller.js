import { responseSuccess, responseError } from "../../network/responses";
import { prisma } from "../../db";

export async function list(req, res) {
  try {
    const products = await prisma.product.findMany();

    responseSuccess({ res, data: products });
  } catch (error) {
    responseError({ res, data: error.message });
  }
}
