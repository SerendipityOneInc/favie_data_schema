# Makefile

# Find all .avsc files in the current directory and its subdirectories
AVRO_FILES := $(shell find . -name '*.avsc')
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
	pydantic-avro avro_to_pydantic --asvc $< --output "$$namespace_dir/$$model_name.py"