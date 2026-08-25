const parsers = {
  promedio: form => ({ notas: form.notas.value.split(",").map(Number) }),
  calificacion: form => ({ nota: Number(form.nota.value) }),
  carrito: form => ({ carrito: JSON.parse(form.carrito.value), producto: form.producto.value.trim() }),
  descuento: form => ({ precio: Number(form.precio.value), descuento: Number(form.descuento.value) }),
  stock: form => ({ nombre: form.nombre.value.trim(), stock: Number(form.stock.value), cantidad: Number(form.cantidad.value) }),
  buscar: form => ({ inventario: JSON.parse(form.inventario.value), nombre: form.nombre.value.trim() }),
  reporte: form => ({ inventario: JSON.parse(form.inventario.value) }),
  ventas: form => ({ ventas: form.ventas.value.split(",").map(monto => ({ monto: Number(monto.trim()) })), descuento: Number(form.descuento.value) }),
  horario: form => ({ inicio: form.inicio.value, fin: form.fin.value })
};

function formatResult(endpoint, value) {
  if (endpoint === "promedio") return `Promedio: ${Number(value).toFixed(2)}`;
  if (endpoint === "calificacion") return value;
  if (endpoint === "descuento") return `$ ${Number(value).toFixed(2)}`;
  if (endpoint === "horario") return value ? "✓ Horario válido" : "✕ Horario inválido";
  if (endpoint === "buscar") return value ? JSON.stringify(value, null, 2) : "No se encontró el producto";
  if (typeof value === "object") return JSON.stringify(value, null, 2);
  return String(value);
}

document.querySelectorAll(".runner-card").forEach(form => {
  form.addEventListener("submit", async event => {
    event.preventDefault();
    const endpoint = form.dataset.endpoint;
    const output = form.querySelector(".result");
    const button = form.querySelector("button[type=submit]");
    output.className = "result loading";
    output.querySelector("strong").textContent = "Ejecutando Python…";
    button.disabled = true;

    try {
      const payload = parsers[endpoint](form);
      if (Object.values(payload).some(value => typeof value === "number" && Number.isNaN(value))) throw new Error("Ingresá solamente valores numéricos válidos.");
      const response = await fetch(`/api/${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      const data = await response.json();
      if (!data.ok) throw new Error(data.error);

      output.className = "result success";
      output.querySelector("strong").textContent = formatResult(endpoint, data.result);

      if (endpoint === "carrito") {
        form.carrito.value = JSON.stringify(data.result);
        form.producto.value = "";
        form.querySelector("[data-cart]").innerHTML = data.result.map(item => `<span>${item}<button type="button" aria-label="Quitar ${item}">×</button></span>`).join("");
        form.querySelectorAll("[data-cart] button").forEach((remove, index) => remove.addEventListener("click", () => {
          const cart = JSON.parse(form.carrito.value);
          cart.splice(index, 1);
          form.carrito.value = JSON.stringify(cart);
          remove.parentElement.remove();
          if (!cart.length) form.querySelector("[data-cart]").innerHTML = "<span>El carrito está vacío</span>";
        }));
      }
      if (endpoint === "stock") form.stock.value = data.result.stock;
    } catch (error) {
      output.className = "result error";
      output.querySelector("strong").textContent = error.message || "No se pudo ejecutar la función.";
    } finally {
      button.disabled = false;
    }
  });
});

document.querySelector("#clearResults").addEventListener("click", () => {
  document.querySelectorAll(".result").forEach(output => {
    output.className = "result";
    output.querySelector("strong").textContent = "Esperando ejecución…";
  });
});

const sidebar = document.querySelector("#sidebar");
document.querySelector("#menuButton").addEventListener("click", () => sidebar.classList.toggle("open"));
document.querySelectorAll(".nav-link").forEach(link => link.addEventListener("click", () => sidebar.classList.remove("open")));

const observer = new IntersectionObserver(entries => entries.forEach(entry => {
  if (!entry.isIntersecting) return;
  document.querySelectorAll(".nav-link").forEach(link => link.classList.toggle("active", link.dataset.target === entry.target.id));
}), { rootMargin: "-20% 0px -65% 0px" });
document.querySelectorAll("#inicio, .module-section").forEach(section => observer.observe(section));
