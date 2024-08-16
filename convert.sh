#!/bin/bash
set -e

echo "合并avro代码..."
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/product/source_code" --output-file="avsc/interface/product/output_code/favie_product.avsc" --main-schema="favie.data.interface.product.FavieProduct"
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/product/source_code" --output-file="avsc/interface/product/output_code/favie_review.avsc" --main-schema="favie.data.interface.product.FavieReview"
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/media/source_code" --output-file="avsc/interface/media/output_code/favie_image.avsc" --main-schema="favie.data.interface.media.FavieImage"
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/media/source_code" --output-file="avsc/interface/media/output_code/favie_image_crawl_request.avsc" --main-schema="favie.data.interface.media.FavieImageCrawlRequest"
echo "合并avro代码结束"

echo "转化合并后的代码..."
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/product/output_code/favie_product.avsc" --output-file="favie_data_schema/favie/data/interface/product/favie_product.py"
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/product/output_code/favie_review.avsc" --output-file="favie_data_schema/favie/data/interface/product/favie_review.py"
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/media/output_code/favie_image.avsc" --output-file="favie_data_schema/favie/data/interface/media/favie_image.py"
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/media/output_code/favie_image_crawl_request.avsc" --output-file="favie_data_schema/favie/data/interface/media/favie_image_crawl_request.py"
echo "转化合并后的代码结束"
