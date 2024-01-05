// Forma antigua
// const express = require("express");

import express from "express";
import { searchById } from "./utils.js";
import { responseSuccess, responseError } from "./responses.js";
import { PrismaClient } from "@prisma/client";

const app = express();
app.use(express.json());

const prisma = new PrismaClient();

app.get("/", async (_req, res) => {
  try {
    const users = await prisma.user.findMany(); //SELECT * FROM users;
    return responseSuccess({ res, data: users });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

app.get("/:id", async (req, res) => {
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
});

app.post("/", async (req, res) => {
  try {
    await prisma.user.create({
      data: req.body,
    });

    return responseSuccess({ res, data: "User created", status: 201 });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

app.put("/:id", async (req, res) => {
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
});

app.delete("/:id", async (req, res) => {
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
});

app.listen(3000, function () {
  console.log("El servidor inicio en el puerto 3000 http://localhost:3000");
});
