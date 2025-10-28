from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    time.sleep(15)  # Add a 15-second delay
    page.goto("http://localhost:3000")
    page.click("text=1")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.click("text=0")
    page.screenshot(path="jules-scratch/verification/verification.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)