import { PrismaClient } from "@prisma/client";
import { responseSuccess, responseError } from "../../network/responses";

const prisma = new PrismaClient();

export async function list(req, res) {
  try {
    const users = await prisma.user.findMany();
    return responseSuccess({ res, data: users, status: 203 });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}

export async function getById(req, res) {
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
    return responseError({ res, data: error.message });
  }
}

export async function store(req, res) {
  try {
    await prisma.user.create({
      data: req.body,
    });

    return responseSuccess({ res, data: "User created", status: 201 });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}

export async function update(req, res) {
  try {
    const user = await prisma.user.update({
      where: {
        id: Number(req.params.id),
      },
      data: req.body,
    });

    if (!user) {
      return responseError({ res, data: "User not found" });
    }

    return responseSuccess({ res, data: "User updated" });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}

export async function destroy(req, res) {
  try {
    await prisma.user.delete({
      where: {
        id: Number(req.params.id),
      },
    });

    return responseSuccess({ res, data: "User deleted" });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}
