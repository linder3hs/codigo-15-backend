import type { Response, Request } from "express";
import { prisma } from "../../db";
import { responseSuccess, responseError } from "../../network/responses";
import { handleResponseError } from "../../utils";
import { hash } from "../../crypto";

export async function list(_req: Request, res: Response): Promise<Response> {
  try {
    const users = await prisma.user.findMany();
    return responseSuccess({ res, data: users });
  } catch (error) {
    return handleResponseError(res, error);
  }
}

export async function getById(req: Request, res: Response): Promise<Response> {
  try {
    const user = await prisma.user.findUnique({
      where: {
        id: Number(req.params.id),
      },
    });

    if (!user) {
      return responseError({ res, data: "User not found" });
    }
    return responseSuccess({ res, data: user });
  } catch (error) {
    return handleResponseError(res, error);
  }
}

export async function store(req: Request, res: Response): Promise<Response> {
  try {
    req.body.password = hash(req.body.password);

    await prisma.user.create({ data: req.body });

    return responseSuccess({ res, data: "User created", status: 201 });
  } catch (error) {
    return handleResponseError(res, error);
  }
}

export async function update(req: Request, res: Response): Promise<Response> {
  try {
    if (req.body.password) {
      req.body.password = hash(req.body.password);
    }

    const user = await prisma.user.update({
      where: { id: Number(req.params.id) },
      data: req.body,
    });

    if (!user) {
      return responseError({ res, data: "User not found" });
    }

    return responseSuccess({ res, data: "User updated" });
  } catch (error) {
    return handleResponseError(res, error);
  }
}

export async function destroy(req: Request, res: Response): Promise<Response> {
  try {
    await prisma.user.delete({ where: { id: Number(req.params.id) } });

    return responseSuccess({ res, data: "User deleted" });
  } catch (error) {
    return handleResponseError(res, error);
  }
}
