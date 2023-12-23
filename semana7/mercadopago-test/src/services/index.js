import { BASE_URL } from "./config";

function getFormatDate() {
  const date = new Date();
  return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
}

export async function storePayment(data) {
  try {
    const body = {
      payment_date: getFormatDate(),
      payer_email: data.payer.email,
      payer_document_type: data.payer.identification.type,
      payer_document_number: data.payer.identification.number,
      installments: data.installments,
      issuer_id: data.issuer_id,
      payment_method_id: data.payment_method_id,
      token: data.token,
      status: 1,
      amount: data.transaction_amount,
      client: 3,
    };
  } catch (error) {
    console.log(`Error: ${error.message}`);
  }
}
