import asyncio
import os
from playwright.async_api import async_playwright

HTML = os.path.abspath(r'c:\Users\User\Desktop\Ben\Code\Datos\one-pager.html')
OUT  = r'c:\Users\User\Desktop\Ben\Code\Datos\PriorityPulse-One-Pager.pdf'

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f'file:///{HTML}', wait_until='networkidle')
        await page.pdf(
            path=OUT,
            format='A4',
            print_background=True,
            scale=0.78,
            margin={'top': '12mm', 'bottom': '12mm', 'left': '14mm', 'right': '14mm'},
        )
        await browser.close()
        print(f'Saved: {OUT}')

asyncio.run(main())
