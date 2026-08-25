import json
import mimetypes
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

from Modulo_1.calcular_promedio import calcular_promedio
from Modulo_1.obtener_calificacion import obtener_calificacion
from Modulo_2.agregar_producto import agregar_producto
from Modulo_2.aplicar_descuento import aplicar_descuento
from Modulo_3.actualizar_stock import actualizar_stock
from Modulo_3.buscar_producto import buscar_producto
from Modulo_3.generar_reporte import generar_reporte
from Modulo_4.procesar_ventas import procesar_ventas
from Modulo_4.validar_horario import validar_horario


ROOT = Path(__file__).resolve().parent


def ejecutar(ruta, datos):
    if ruta == "promedio":
        return calcular_promedio(datos["notas"])
    if ruta == "calificacion":
        return obtener_calificacion(datos["nota"])
    if ruta == "carrito":
        return agregar_producto(datos.get("carrito"), datos["producto"])
    if ruta == "descuento":
        return aplicar_descuento(datos["precio"], datos["descuento"])
    if ruta == "stock":
        producto = {"nombre": datos["nombre"], "stock": datos["stock"]}
        return actualizar_stock(producto, datos["cantidad"])
    if ruta == "buscar":
        return buscar_producto(datos["inventario"], datos["nombre"])
    if ruta == "reporte":
        return generar_reporte(datos["inventario"])
    if ruta == "ventas":
        return procesar_ventas(datos["ventas"], datos["descuento"])
    if ruta == "horario":
        return validar_horario(datos["inicio"], datos["fin"])
    raise ValueError("Función no disponible")


class Manejador(BaseHTTPRequestHandler):
    def responder_json(self, contenido, estado=200):
        cuerpo = json.dumps(contenido, ensure_ascii=False).encode("utf-8")
        self.send_response(estado)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_POST(self):
        ruta = urlparse(self.path).path
        if not ruta.startswith("/api/"):
            self.responder_json({"ok": False, "error": "Ruta no encontrada"}, 404)
            return
        try:
            largo = int(self.headers.get("Content-Length", "0"))
            datos = json.loads(self.rfile.read(largo) or b"{}")
            resultado = ejecutar(ruta.removeprefix("/api/"), datos)
            self.responder_json({"ok": True, "result": resultado})
        except (ValueError, TypeError, KeyError, json.JSONDecodeError) as error:
            self.responder_json({"ok": False, "error": str(error)}, 400)
        except Exception as error:
            self.responder_json({"ok": False, "error": f"Error de ejecución: {error}"}, 500)

    def do_GET(self):
        ruta = urlparse(self.path).path
        if ruta == "/api/salud":
            self.responder_json({"ok": True, "motor": "Python"})
            return
        archivo = ROOT / ("index.html" if ruta in ("/", "") else ruta.lstrip("/"))
        try:
            archivo = archivo.resolve()
            archivo.relative_to(ROOT)
            if not archivo.is_file():
                raise FileNotFoundError
            contenido = archivo.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", mimetypes.guess_type(archivo.name)[0] or "application/octet-stream")
            self.send_header("Content-Length", str(len(contenido)))
            self.end_headers()
            self.wfile.write(contenido)
        except (FileNotFoundError, ValueError):
            self.send_error(404, "Archivo no encontrado")

    def log_message(self, formato, *args):
        print(f"[Actividad 03] {formato % args}")


if __name__ == "__main__":
    direccion = ("127.0.0.1", 4174)
    print(f"Aplicación disponible en http://{direccion[0]}:{direccion[1]}")
    ThreadingHTTPServer(direccion, Manejador).serve_forever()
