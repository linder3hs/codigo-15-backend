// Forma antigua
// const express = require("express");

import express from "express";
import { searchById } from "./utils.js";

const app = express();
app.use(express.json());

const users = [
  {
    id: 1,
    name: "Linder",
    lastname: "Hassinger",
    email: "linder@gmail.com",
    password: "linder340",
  },
];

// app.get("/", function (request, response) {
//   return response.json({
//     ok: true,
//     data: users,
//   });
// });

// vamos a minificar esto
app.get("/", (_req, res) => {
  return res.json({
    ok: true,
    data: users,
  });
});

app.get("/:id", (req, res) => {
  const user = searchById(users, Number(req.params.id));

  if (!user) {
    return res.json({
      ok: false,
      data: "User not found",
    });
  }

  return res.json({
    ok: true,
    data: user,
  });
});

app.post("/", (req, res) => {
  const user = req.body;
  user.id = users.length + 1;

  users.push(user);

  return res.status(201).json({
    ok: true,
    data: "User created",
  });
});

app.delete("/:id", (req, res) => {
  const user = searchById(users, Number(req.params.id));

  if (!user) {
    return res.json({
      ok: false,
      data: "User not found",
    });
  }

  users.splice(user, 1);

  return res.json({
    ok: true,
    data: "User deleted",
  });
});

app.listen(3000, function () {
  console.log("El servidor inicio en el puerto 3000 http://localhost:3000");
});
