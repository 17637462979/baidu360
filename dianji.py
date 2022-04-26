#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mr.z
@time: 2022-04-20
@desc:
"""
from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:

        browser = p.webkit.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=False)
        page.goto('https://www.baidu.com/')
        page.fill("#kw", "啊啊啊啊啊")
        page.click("#su")
        page.wait_for_selector("#content_left")
        print(page.context)
        hrefs1 = page.query_selector_all('xpath=//h3[contains(@class,"t")]/a')
        hrefs = [x for x in hrefs1]
        print(hrefs)
        if len(hrefs1) < 10:
            _hrefs = page.query_selector_all('xpath=//div[@id="content_left"]/div/div/div/h3/a')
            # print(type(_hrefs))
            for href in _hrefs:
                print(href)
                hrefs.append(href)
        for i in hrefs:
            print(i.get_attribute('href'))
        texts = page.query_selector_all('xpath=//div[@class="c-container"]/div/h3/a')
        for j in texts:

            print(j.inner_text())
        page.screenshot(path=f'example-{p.firefox.name}.png')
        browser.close()



def main360():
    with sync_playwright() as p:

        browser = p.webkit.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=False)
        page.goto('https://www.so.com/')
        page.fill("#input", "啊啊啊啊啊")
        page.click("#search-button")
        page.wait_for_selector(".result")
        print(page.context)
        hrefs = page.query_selector_all('xpath=//li[@class="res-list"]/h3/a')
        # hrefs = [x for x in hrefs1]
        # print(hrefs)
        # if len(hrefs1) < 10:
        #     _hrefs = page.query_selector_all('xpath=//div[@id="content_left"]/div/div/div/h3/a')
            # print(type(_hrefs))
            # for href in _hrefs:
            #     print(href)
            #     hrefs.append(href)
        for i in hrefs:
            print(i.get_attribute('href'))
        texts = page.query_selector_all('xpath=//div[@class="c-container"]/div/h3/a')
        for j in texts:

            print(j.inner_text())
        page.screenshot(path=f'example-{p.firefox.name}.png')
        browser.close()


if __name__ == '__main__':
    main360()