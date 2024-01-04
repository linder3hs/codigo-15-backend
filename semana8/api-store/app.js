// Forma antigua
// const express = require("express");

import express from "express";

const app = express();

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
  // Toda la informacion de URL es de tipo String
  const id = Number(req.params.id);
  const user = users.find((user) => user.id === id);

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

app.listen(3000, function () {
  console.log("El servidor inicio en el puerto 3000 http://localhost:3000");
});
