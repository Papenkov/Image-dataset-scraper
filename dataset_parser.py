import requests
import os
from tqdm import tqdm, trange
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import argparse
import re



def get_img_urls(url, page_numbers):
    urls = []
    for page_n in trange(page_numbers, desc="Parsing progress"):

        soup = bs(requests.get(url).content, "html.parser")

        # найти блок со сменой страницы find changing page blok
        mydivs = soup.find("div", {"class": "pager pager_light"})
        # забрать ссылку на след. страницу get next page link
        for i in range(len(mydivs)):
            try:
#                 page_number = mydivs.find_all("a")[i].attrs.get("data-page")
                next_page_link = mydivs.find_all("a")[i].attrs.get("href")
#                 if page_number and next_page_link:
#                     print(f"Move to page number: {page_number} \tlink: {next_page_link}")
            except:
                pass
            
        url = urljoin(url, next_page_link)
#         print(f"Next page url: {url}")
        
        for img in soup.find_all("img"):
            # extract images links (lays in "src" and "data-src" tags)
            if img.attrs.get("src"):
                urls.append(img.attrs.get("src"))
            elif img.attrs.get('data-src'): 
                urls.append(img.attrs.get('data-src'))
                
    # drop noninformative links (same in any page)  
    static = 'static.depositphotos.com/storage/image'
    clear_url_list = [im_http for im_http in urls if not re.search(static, im_http)]
    return clear_url_list


def download(urls):
    """
    Download images from extracted urls_list to `pathname` dir
    """
    # if path_to_dir not exist create it
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
        print(f"Created folder to saving dataset: {pathname}")
    for n, url in enumerate(tqdm(urls, "Downloading pictures")):
        # загружаем тело ответа по частям, а не сразу
        response = requests.get(url, stream=True)
        filename = os.path.join(pathname, f"{n}.jpg")
        with open(filename, "wb") as f:
            # записываем прочитанные данные, в файл
            f.write(response.content)
            
            
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=str, help='path to initial link')
    parser.add_argument('-n', type=int, default=20, help='number of pages for parsing')  # about ~100 pictures on 1 page (default_pages=20; 20*100 = 2000 samples)
    parser.add_argument('-f', type=str, help='path to folder to save dataset')
    args = parser.parse_args()

    url = args.p
    page_numbers = args.n
    pathname = os.path.abspath(args.f)
    
    print("\n", "*"*90, sep="")
    print(f"Folder for saving dataset: {pathname}\n")
    url_list = get_img_urls(url, page_numbers)
    print(f"\nSamples found: {len(url_list)}\n")
    download(url_list)
    print("\nLoading dataset has done\n", "*"*90, "\n", sep="")