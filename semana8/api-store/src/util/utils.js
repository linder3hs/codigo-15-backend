export function searchById(array, id) {
  return array.find((item) => item.id === id);
}

export function response(ok, data) {
  return { ok, data };
}
