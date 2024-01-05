export function responseSuccess({ res, data, status = 200 }) {
  return res.status(status).json({
    ok: true,
    data,
  });
}

export function responseError({ res, status = 500, data }) {
  return res.status(status).json({
    ok: false,
    data,
  });
}
