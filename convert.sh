#!/bin/bash
set -e

echo "合并avro代码..."
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/product/common" --output-file="avsc/interface/product/output/favie_product.avsc" --main-schema="favie.data.interface.product.FavieProduct"
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/product/common" --output-file="avsc/interface/product/output/favie_review.avsc" --main-schema="favie.data.interface.product.FavieReview"
echo "合并avro代码结束"

echo "转化合并后的代码..."
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/product/output/favie_product.avsc" --output-file="favie_data_schema/favie/data/interface/product/favie_product.py"
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/product/output/favie_review.avsc" --output-file="favie_data_schema/favie/data/interface/product/favie_review.py"
echo "转化合并后的代码结束"
