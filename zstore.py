# %%

from pydoc import describe
from pyppeteer import launch

browser = await launch({
    'headless': False,
    'executablePath': r"C:\Program Files\Google\Chrome\Application\chrome.exe"
})
# %%

page = await browser.newPage()
await page.goto('https://www.ztore.com/tc/category/all/beverage/carbonated-beverage')


# %%
# import math
# import re

# total_count =  await page.querySelector('.product-total')
# total_products = await page.evaluate('(total_count) => name.textContent', total_count)
# total_page=re.findall('(\d{1,4})', total_products)

# print(total_page)
# total = int(total_page[0])
# totalPages = math.ceil(total / 60)

# print(totalPages)

# %%
# from time import sleep
# for i in range(6):
#     if i==0:
#         await page.evaluate('window.scrollBy(0,document.body.scrollHeight)')
#         await page.waitForSelector('.viewAllButton')
#         await page.click(selector='.viewAllButton')
#     # await page.waitForSelector('.loading .load_more')
#     await page.waitForNavigation()
#     await page.evaluate('window.scrollBy(0,document.body.scrollHeight)')
    
# sleep(1.2)

# %%

await page.evaluate('window.scrollBy(0,document.body.scrollHeight)')
await page.waitForSelector('.viewAllButton')
await page.click(selector='.viewAllButton')

# for i in range(100):
    # await page.waitForNavigation()
    # await page.evaluate('document.querySelector(".loading.load_more").scrollIntoView({behavior: "smooth"})')
    # await page.waitForSelector('.loading.load_more')
    # await page.waitForNavigation()
    # sleep(4)
    # if (await page.evaluate('document.querySelector(".loading.load_more")') is None):
    #     break
# await page.waitForSelector('.loading .load_more')
# await page.evaluate('window.scrollBy(0,document.body.scrollHeight)')

# %%
from time import sleep

for i in range(8):
    await page.evaluate('document.querySelector(".loading.load_more").scrollIntoView({behavior: "smooth"})')
    sleep(4)

# %%
# items = await page.querySelectorAll('.ProductList > .ProductItem')

# %%
drinksList = []
for i in range(224):
    item =  f'.ProductList :nth-child({i+1})'
    # print(item)

    name =  await page.querySelector(f'{item} a .name_bbd .name .TruncateBox')
    productName = await page.evaluate('(name) => name.textContent', name)
    
    packSize =  await page.querySelector(f'{item} a .packsize span')
    description = await page.evaluate('(packSize) => packSize.textContent', packSize)
    
    priceEl =  await page.querySelector(f'{item} a .price') if await page.querySelector(f'{item} a .price span') is None else await page.querySelector(f'{item} a .price span') 
    price = await page.evaluate('(priceEl) => priceEl.textContent', priceEl)
    
    photo =  await page.querySelector(f'{item} a .img .ProgressiveImage span img')
    photoPath = await page.evaluate('(photo) => photo.src', photo)
    
    drinksList.append({
        "product_name": productName,
        "description": description,
        "image": f"""{photoPath}""",
        "price": price
    })
    

# %%
print(drinksList)

# %%
import pandas as pd

df = pd.DataFrame(drinksList)
df.describe()
# df.head()
df.to_csv('zstore_drinks.csv')
# %%
