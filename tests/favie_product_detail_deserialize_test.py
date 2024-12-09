from read_json_util import read_object

from favie_data_schema.api.data.product import FavieProductDetail

if __name__ == "__main__":
    product_detail = read_object("favie_data_schema/favie/resources/product_detail.json", FavieProductDetail)
    if product_detail:
        print(product_detail.model_dump_json(exclude_none=True))
