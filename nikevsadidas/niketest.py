
clean_urls = []

with open("product_page_urls.txt" , "r") as f:
    for line in f:
        text = line.strip()
        if text not in clean_urls:
            clean_urls.append(text)



with open("clean_urls_v2.txt" , "w") as f:
    for item in clean_urls:
        f.write("%s\n" % item)
        print(item)
print(len(clean_urls))