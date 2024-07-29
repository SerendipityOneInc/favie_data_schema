# Makefile

# Define PYTHONPATH
export PYTHONPATH := $(PYTHONPATH):$(shell pwd)

# Find all .avsc files in the current directory and its subdirectories
AVRO_FILES := \
	$(shell find avsc/api -name '*.avsc') \
	$(shell find avsc/log/quora -name '*.avsc') \
	$(shell find avsc/log/reddit -name '*.avsc') \
	$(shell find avsc/log/crawler -name '*.avsc') \
	avsc/log/dw/product/common/brand.avsc \
	avsc/log/dw/product/common/attribute_item.avsc \
	avsc/log/dw/product/common/category_item.avsc \
	avsc/log/dw/product/common/price.avsc \
	avsc/log/dw/product/common/delivery_price.avsc \
	avsc/log/dw/product/common/standard_attributes.avsc \
	avsc/log/dw/product/common/delivery.avsc \
	avsc/log/dw/product/common/fulfillment.avsc \
	avsc/log/dw/product/common/images.avsc \
	avsc/log/dw/product/common/inventory.avsc \
	avsc/log/dw/product/common/promotion.avsc \
	avsc/log/dw/product/common/return_policy.avsc \
	avsc/log/dw/product/common/search_alias_item.avsc \
	avsc/log/dw/product/common/deal.avsc \
	avsc/log/dw/product/common/seller.avsc \
	avsc/log/dw/product/common/shipping.avsc \
	avsc/log/dw/product/common/simple_product.avsc \
	avsc/log/dw/product/common/videos.avsc \
	avsc/log/dw/product/common/offer.avsc \
	avsc/log/dw/product/favie_product.avsc

# Generate the corresponding .py file names
PYTHON_FILES := $(patsubst %.avsc,%.py,$(AVRO_FILES))

# Default target: generate all Python files
all: $(PYTHON_FILES)

# Rule to generate .py files from .avsc files
%.py: %.avsc
	@echo "Processing $<" # Add debug information
	@model_name=$$(basename $$(basename $<) .avsc) && \
	namespace_dir=$$(jq -r '.namespace' $< | tr '.' '/') && \
	echo "model_name: $$model_name" && \
	echo "namespace_dir: $$namespace_dir" && \
	mkdir -p $$namespace_dir && \
	pydantic-avro avro_to_pydantic --asvc $< --output "$$namespace_dir/$$model_name.py" && \
	echo "$$model_name.py generated" 