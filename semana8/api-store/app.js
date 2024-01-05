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

app.get("/:id", (req, res) => {
  const user = searchById(users, Number(req.params.id));

  if (!user) {
    return responseError({ res, data: "User not found" });
  }

  return responseSuccess({ res, data: user });
});

app.post("/", (req, res) => {
  const user = req.body;
  user.id = users.length + 1;

  users.push(user);

  return responseSuccess({ res, data: "User created", status: 201 });
});

app.put("/:id", (req, res) => {
  const user = searchById(users, Number(req.params.id));

  if (!user) {
    return responseError({ res, data: "User not found" });
  }

  const body = req.body;

  Object.entries(body).forEach(([key, value]) => {
    user[key] = value;
  });

  return responseSuccess({ res, data: "User updated" });
});

app.delete("/:id", (req, res) => {
  const user = searchById(users, Number(req.params.id));

  if (!user) {
    return responseError({ res, data: "User not found" });
  }

  users.splice(user, 1);
  return responseSuccess({ res, data: "User deleted" });
});

app.listen(3000, function () {
  console.log("El servidor inicio en el puerto 3000 http://localhost:3000");
});
