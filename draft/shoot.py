import asyncio, sys, os
from playwright.async_api import async_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "file://" + os.path.join(ROOT, "index.html")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, w, h, dark in [("desktop", 1280, 900, False), ("mobile", 390, 844, False), ("dark", 1280, 900, True)]:
            pg = await b.new_page(viewport={"width": w, "height": h}, color_scheme="dark" if dark else "light", device_scale_factor=2 if w < 500 else 1)
            errors = []
            pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            pg.on("pageerror", lambda e: errors.append(str(e)))
            await pg.goto(URL, wait_until="load")
            await pg.wait_for_timeout(400)
            await pg.screenshot(path=os.path.join(ROOT, "draft", f"{name}.png"))
            await pg.screenshot(path=os.path.join(ROOT, "draft", f"{name}-full.png"), full_page=True)
            print(f"{name}: console_errors={errors}")
            await pg.close()
        await b.close()

asyncio.run(main())
