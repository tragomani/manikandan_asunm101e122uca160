def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

product_list = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]

target_product = "Banana"

result = linear_search_product(product_list, target_product)

if result:
    print("Indices of", target_product, ":", result)
else:
    print(target_product, "not found in the product list.")
