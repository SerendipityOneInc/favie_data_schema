AVRO_FILES = $(wildcard *.avsc)
PYTHON_FILES = $(AVRO_FILES:.avsc=.py)

all: $(PYTHON_FILES)

%.py: %.avsc
    @model_name=$(basename $< .avsc) && \
    namespace_dir=$(jq -r '.namespace' $< | tr '.' '/') && \
    mkdir -p $$namespace_dir && \
    pydantic-avro avro_to_pydantic --asvc $< --output "$$namespace_dir/$$model_name.py"