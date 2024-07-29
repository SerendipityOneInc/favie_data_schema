#!/bin/bash

echo "合并avro代码..."
python -m favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/product/common" --output-file="avsc/interface/product/output/favie_product.avsc" --main-schema="favie.data.product.FavieProduct"
echo "合并avro代码结束"

echo "转化合并后的代码..."
python -m favie.tools.avro_to_pydantic --avsc="avsc/interface/product/output/favie_product.avsc" --output-file="favie/data/interface/product/favie_product.py"
echo "转化合并后的代码结束"
