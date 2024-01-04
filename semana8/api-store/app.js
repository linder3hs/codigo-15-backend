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

app.get("/", function (request, response) {
  return response.json({
    ok: true,
    data: users,
  });
});

app.listen(3000, function () {
  console.log("El servidor inicio en el puerto 3000 http://localhost:3000");
});
