#!/bin/bash
set -e

echo "合并Product avro代码..."
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/product/source_code" --output-file="avsc/interface/product/output_code/favie_product_detail.avsc" --main-schema="favie.data.interface.product.FavieProductDetail"
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/product/source_code" --output-file="avsc/interface/product/output_code/favie_product_review.avsc" --main-schema="favie.data.interface.product.FavieProductReview"
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/product/source_code" --output-file="avsc/interface/product/output_code/favie_product_review_summary.avsc" --main-schema="favie.data.interface.product.FavieProductReviewSummary"
echo "合并Product avro代码结束"

echo "转化合并后的Product代码..."
# python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/product/output_code/favie_product_detail.avsc" --output-file="favie_data_schema/favie/data/interface/product/favie_product_detail.py"
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/product/output_code/favie_product_review.avsc,avsc/interface/product/output_code/favie_product_review_summary.avsc,avsc/interface/product/output_code/favie_product_detail.avsc" --output-file="favie_data_schema/favie/data/interface/product/favie_product.py"
echo "转化合并后的Product代码结束"

echo "合并Media avro代码..."
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/media/source_code" --output-file="avsc/interface/media/output_code/favie_media_image.avsc" --main-schema="favie.data.interface.media.FavieMediaImage"
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/media/source_code" --output-file="avsc/interface/media/output_code/favie_image_crawl_request.avsc" --main-schema="favie.data.interface.media.FavieImageCrawlRequest"
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/media/source_code" --output-file="avsc/interface/media/output_code/favie_image_crawl_response.avsc" --main-schema="favie.data.interface.media.FavieImageCrawlResponse"
echo "合并Media avro代码结束"

echo "转化合并后的Media代码..."
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/media/output_code/favie_media_image.avsc" --output-file="favie_data_schema/favie/data/interface/media/favie_media_image.py"
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/media/output_code/favie_image_crawl_request.avsc,avsc/interface/media/output_code/favie_image_crawl_response.avsc" --output-file="favie_data_schema/favie/data/interface/media/favie_image_crawl.py"
echo "转化合并后的Media代码结束"

echo "合并Webpage avro代码..."
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/interface/webpage/source_code" --output-file="avsc/interface/webpage/output_code/favie_webpage.avsc" --main-schema="favie.data.interface.webpage.FavieWebpage"
echo "合并Webpage avro代码结束"

echo "转化合并后的Webpage代码..."
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/interface/webpage/output_code/favie_webpage.avsc" --output-file="favie_data_schema/favie/data/interface/webpage/favie_webpage.py"
echo "转化合并后的Webpage代码结束"


echo "处理AmazonList..."
python -m favie_data_schema.favie.tools.combine_schemas_with_unique_define --source-directory="avsc/inner_data/crawler/amazon/source_code" --output-file="avsc/inner_data/crawler/amazon/output_code/amazon_list_crawler_result.avsc" --main-schema="favie.data.crawl_data.crawler.AmazonListCrawlResult"
python -m favie_data_schema.favie.tools.avro_to_pydantic --avsc="avsc/inner_data/crawler/amazon/output_code/amazon_list_crawler_result.avsc" --output-file="favie_data_schema/favie/data/crawl_data/crawler/amazon_list_crawler_result.py"
echo "处理AmazonList结束"