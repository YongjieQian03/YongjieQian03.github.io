"""Preview script. Serves the exported out/ directory and captures screenshots into draft/."""
import asyncio
import http.server
import os
import socketserver
import threading

from playwright.async_api import async_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")
PORT = 8210

PAGES = [
    ("home", "/"),
    ("publications", "/publications/"),
    ("projects", "/projects/"),
    ("awards", "/awards/"),
    ("cv", "/cv/"),
]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve():
    os.chdir(OUT)
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


async def capture():
    base = f"http://127.0.0.1:{PORT}"
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        shots = [
            ("home", "/", 1400, 1000, False),
            ("home-dark", "/", 1400, 1000, True),
            ("mobile", "/", 390, 844, False),
            ("publications", "/publications/", 1400, 1000, False),
            ("projects", "/projects/", 1400, 1000, False),
            ("cv", "/cv/", 1400, 1000, False),
        ]

        for name, path, width, height, dark in shots:
            page = await browser.new_page(
                viewport={"width": width, "height": height},
                color_scheme="dark" if dark else "light",
            )
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            await page.goto(base + path, wait_until="load")
            await page.wait_for_timeout(2500)
            await page.screenshot(path=os.path.join(ROOT, "draft", f"p-{name}.png"), full_page=True)
            print(f"{name}: console_errors={errors}")
            await page.close()

        await browser.close()


if __name__ == "__main__":
    server = serve()
    try:
        asyncio.run(capture())
    finally:
        server.shutdown()
