import type { Response } from "express";
import { prismaError } from "../db";
import { responseError } from "../network/responses";

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

export function handleResponseError(res: Response, error: unknown) {
  if (error instanceof prismaError) {
    return responseError({
      res,
      data: `DB Error(${error.code}): ${error.message}`,
    });
  }
  return responseError({ res, data: `Error: ${error}` });
}
