import { initMercadoPago, CardPayment } from "@mercadopago/sdk-react";

initMercadoPago(import.meta.env.VITE_MERCADOPAGO_PUBLIC_KEY);

export default function App() {
  const initialization = {
    amount: 500,
  };

  const handleOnSubmit = (formData) => {
    console.log(formData);
  };

  return (
    <main
      style={{
        margin: 6,
      }}
    >
      <h1>Pagando con mercado pago</h1>
      <CardPayment
        initialization={initialization}
        onSubmit={handleOnSubmit}
        customization={{
          paymentMethods: {
            maxInstallments: 1,
          },
          visual: {
            style: {
              theme: "default",
            },
          },
        }}
      />
    </main>
  );
}
