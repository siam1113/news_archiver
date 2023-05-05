import boto3

client = boto3.client('dynamodb', region_name='us-west-2')

table_name = 'news_archive'

data = {
  "news_archive_key": {
    "S": "2"
  },
  "link": {
    "S": "link"
  },
  "source": {
    "S": "bdnews24"
  },
  "thumbnail": {
    "S": "link"
  },
  "title": {
    "S": "Title of the news"
  }
}
try:
    response = client.put_item(TableName=table_name, Item=data)
    print(response)
    query = client.execute_statement(Statement="SELECT * FROM news_archive")
    print(query)
except Exception as e:
    print(e)