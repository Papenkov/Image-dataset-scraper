# Image-dataset-scraper
Images scraping code from ["depositphotos.com"](https://depositphotos.com/) for your CV tasks.

"Depositphotos.com" is an international photobank with millions of pictures.

If you need create a unique CV dataset with specific images/targets it will be useful to search whole dataset from one resourse. 
Depositphotos.com provides adaptive searching and filters to specify your request.

# Usage

- Go to ["depositphotos.com"](https://depositphotos.com/)
- Print your request in search form:
 
![image](https://github.com/Papenkov/Image-dataset-scraper/assets/64463542/ec70ff2a-fa79-48f8-8149-39cc73978c60)



- Add searching filters
- And copy the link

![main](https://user-images.githubusercontent.com/64463542/168816403-83a3ae19-43c3-45c8-8eb1-ea2e0e537abf.jpg)


# Example

[Download dataset_scraper.py](https://drive.google.com/file/d/1LSrPLYVEf3w0lTqlACe9WIdo43swEkPJ/view?usp=sharing) file or just [copy](./dataset_parser.py) it from repo

Open in terminal from folder where you downloaded the dataset_scraper.py

Run command: 

python dataset_scraper.py -p "link" -n "number_of_pages_for_scraping" -f "folder_to_save_files"

```python
python dataset_parser.py -p 'https://depositphotos.com/stock-photos/sunglasses-man.html?sh=b7a729fc0832fe1d266e59e5d3701bc47222c6cf&filter=all' -n 10 -f ./dataset/sunglasses_man/
```

**Note:**

one "pages_for_scraping" contains about ~100 images, so if you need for example 1000 images specify -n to "10";

don't forget check the data before training CV model.
