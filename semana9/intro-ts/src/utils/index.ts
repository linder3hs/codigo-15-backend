interface Item {
  id: number;
  name: string;
}

export function searchById(array: Item[], id: number): Item | undefined {
  return array.find((item: Item) => item.id === id);
}

interface IResponse {
  ok: boolean;
  data: any;
}

export function response({ ok, data }: IResponse): IResponse {
  return {
    ok,
    data,
  };
}
