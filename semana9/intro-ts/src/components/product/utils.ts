import { IBody, IProduct, IProductDB } from "../../core/types";
import { response } from "../../utils";

function mapProduct(product: IProduct) {
  const productMap = {
    ...product,
    isNew: product.is_new,
    pertangeDiscount: product.pertange_discount,
  } as IProductDB;

  delete productMap.is_new;
  delete productMap.pertange_discount;

  if (product.category_id) {
    productMap.categoryId = product.category_id;
    delete productMap.category_id;
  }

  return productMap;
}

export function mapInsertProduct(body: IBody) {
  const { product, category } = body;

  // caso 1: Que nos envien product.category_id y category
  if (product.category_id && category) {
    return response({
      ok: false,
      data: "No puedes enviar un category_id y category",
    });
  }

  // caso 2: Nos envian product y category
  if (product && category) {
    const insertData = {
      ...mapProduct(product),
      category: {
        create: {
          ...category,
        },
      },
    };

    return response({ ok: true, data: insertData });
  }

  return response({ ok: true, data: mapProduct(product) });
}
