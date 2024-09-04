# favie_data_schema
favie_data_schema


## jsonschema to avro

### infer avro schema from json data

https://konbert.com/convert/json/to/avro

### favie_data_schema/data/interface命名规范
1. favie_data_schema/data/interface 存放所有公开给外部调用的接口的schema，如果只是内部依赖schema，尽量不要放到interface里面
2. favie_data_schema/data/interface 下的一级目录为接口模块的名称，如：media表示多媒体，图片库、视频库相关schema会放在此目录下，product里放的都是商品库相关schema