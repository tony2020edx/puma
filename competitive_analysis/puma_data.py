
text_sp = "₹4,029"

text_mrp = "6,499"
text_discount = "38% off"

text_reviews = "Be the first to Review this product"

def get_ratings(text):
    text_list = text.split(" ")
    if len(text_list) == 5:
        ratings = text_list[0]
    elif len(text_list) == 3:
        ratings = text_list[0]
    else:
        ratings = 0

    return ratings


def get_reviews(text):
    text_list = text.split(" ")
    if len(text_list) == 5:
        reviews = text_list[3]
    elif len(text_list) == 3:
        reviews = 0
    else:
        reviews = 0

    return  reviews


print(get_ratings(text_reviews))
print(get_reviews(text_reviews))


product_name = dom.xpath('//span[@class="B_NuCI"]/text()')
brand_name = dom.xpath('//span[@class="G6XhRU"]/text()')
sale_price = dom.xpath('//div[@class="_30jeq3 _16Jk6d"]/text()')
mrp = dom.xpath('//div[@class="_3I9_wc _2p6lqe"]/text()')
seller_rating = dom.xpath('//div[@class="_3Ay6Sb _31Dcoz pZkvcx"]/span/text()')
product_rating = dom.xpath('//div[@class="_3LWZlK _3uSWvT"]/text()')


print(product_name[0])
print(brand_name[0])
print(sale_price[0])
print(mrp[1])
print(seller_rating[0])
print(product_rating[0])
print(ratings_and_reviews[0])


['Product Name', 'Brand', 'Sale Price', 'MRP', 'Seller Rating', 'Ratings Count', 'Reviews Count', 'Discount', 'Product Rating']