import { createHmac } from "node:crypto";

export function hash(text: string): string {
  return createHmac("sha256", "secret").update(text).digest("hex");
}
