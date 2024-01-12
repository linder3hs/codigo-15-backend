import { PrismaClient, Prisma } from "@prisma/client";

export const prisma = new PrismaClient();

export const prismaError = Prisma.PrismaClientKnownRequestError;
