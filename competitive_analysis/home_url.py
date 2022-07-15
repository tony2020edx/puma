

all_home_urls = []

base_url_puma = "https://www.flipkart.com/search?q=running+shoes+for+men&sid=osp%2Ccil%2C1cu&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=running+shoes+for+men%7CSports+Shoes&requestId=4922c884-a369-4627-9d44-a1c96daba1be&as-searchtext=running+shoes&p%5B%5D=facets.size_uk%255B%255D%3D10&p%5B%5D=facets.brand%255B%255D%3DPUMA&page="
base_url_adidas = "https://www.flipkart.com/search?q=running+shoes+for+men&sid=osp%2Ccil%2C1cu&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=running+shoes+for+men%7CSports+Shoes&requestId=4922c884-a369-4627-9d44-a1c96daba1be&as-searchtext=running+shoes&p%5B%5D=facets.size_uk%255B%255D%3D10&p%5B%5D=facets.brand%255B%255D%3DADIDAS&page="
base_url_nike = "https://www.flipkart.com/search?q=running+shoes+for+men&sid=osp%2Ccil%2C1cu&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=running+shoes+for+men%7CSports+Shoes&requestId=4922c884-a369-4627-9d44-a1c96daba1be&as-searchtext=running+shoes&p%5B%5D=facets.size_uk%255B%255D%3D10&p%5B%5D=facets.brand%255B%255D%3DNIKE&page="
base_url_sketchers = "https://www.flipkart.com/search?q=running+shoes+for+men&sid=osp%2Ccil%2C1cu&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=running+shoes+for+men%7CSports+Shoes&requestId=4922c884-a369-4627-9d44-a1c96daba1be&as-searchtext=running+shoes&p%5B%5D=facets.size_uk%255B%255D%3D10&p%5B%5D=facets.brand%255B%255D%3DSkechers&page="



for i in range(1, 21):
    url = base_url_puma + str(i)
    all_home_urls.append(url)


for i in range(1, 17):
    url = base_url_adidas + str(i)
    all_home_urls.append(url)

for i in range(1, 5):
    url = base_url_nike + str(i)
    all_home_urls.append(url)

for i in range(1, 3):
    url = base_url_sketchers + str(i)
    all_home_urls.append(url)


print(len(all_home_urls))