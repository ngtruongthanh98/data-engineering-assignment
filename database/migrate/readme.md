aws dynamodb create-table --cli-input-json file://D:\Documents\Master\Data-Engineering-v2\Source\data-engineering-assignment\database\migrate\product_table.json  --endpoint-url http://localhost:8000

aws dynamodb create-table --cli-input-json file://D:\Documents\Master\Data-Engineering-v2\Source\data-engineering-assignment\database\migrate\comment_table.json  --endpoint-url http://localhost:8000

aws dynamodb create-table --cli-input-json file://D:\Documents\Master\Data-Engineering-v2\Source\data-engineering-assignment\database\migrate\category_table.json  --endpoint-url http://localhost:8000

aws dynamodb update-table --table-name Product --global-secondary-index-updates "[{\"Create\": {\"IndexName\": \"ProductNameGlobalIndex\",\"KeySchema\":[{\"AttributeName\": \"ProductName\",\"KeyType\": \"HASH\"}],\"Projection\":{\"ProjectionType\": \"ALL\"}}}]" --attribute-definitions AttributeName=ProductName,AttributeType=S --endpoint-url http://localhost:8000