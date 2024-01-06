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

export async function store(req, res) {
  try {
    const { product, category } = req.body;

    const productMap = {
      ...product,
      isNew: product.is_new,
      pertangeDiscount: product.pertange_discount,
    };

    delete productMap.is_new;
    delete productMap.pertange_discount;

    const newProduct = await prisma.product.create({
      data: {
        ...productMap,
        category: {
          create: {
            ...category,
          },
        },
      },
    });

    return responseSuccess({ res, data: newProduct });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}
