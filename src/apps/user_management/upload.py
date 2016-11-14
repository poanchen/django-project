from boto3.dynamodb.conditions import Key, Attr
import boto3
import uuid
import botocore

# s3 configuration
s3 = boto3.client(
  's3',
  aws_access_key_id='key_id',
  aws_secret_access_key='access_key',
  region_name='region_name')
bucket = 'bucket_name'
prefix = ''

# dynamodb configuration
dynamodb = boto3.resource(
  'dynamodb',
  aws_access_key_id='key_id',
  aws_secret_access_key='access_key',
  region_name='region_name')

# List all objects within a S3 bucket path
response = s3.list_objects(
  Bucket = bucket,
  Prefix = prefix
)

def create_user_folder(folder_name):
  r = s3.put_object(
    Bucket = bucket,
    Body='',
    Key=folder_name+'/')

def test():
  # persons = [
  #   {
  #     'first_name' : 'Micheal',
  #     'last_name' : 'Phelps',
  #     'education' : 'University of Google',
  #     'current_location' : 'Victoria, BC',
  #     'hr_rate' : 'CAD$20-30',
  #   },
  #   {
  #     'first_name' : 'Bill',
  #     'last_name' : 'Gates',
  #     'education' : 'University of Microsoft',
  #     'current_location' : 'Washington, DC',
  #     'hr_rate' : 'CAD$25-35',
  #   },
  #   {
  #     'first_name' : 'Tim',
  #     'last_name' : 'Cook',
  #     'education' : 'University of Apple',
  #     'current_location' : 'New York, AB',
  #     'hr_rate' : 'CAD$25-30',
  #   },
  #   {
  #     'first_name' : 'Micheal',
  #     'last_name' : 'Jordan',
  #     'education' : 'University of NBA',
  #     'current_location' : 'Florida, BD',
  #     'hr_rate' : 'CAD$15-20',
  #   },
  #   {
  #     'first_name' : 'Donald',
  #     'last_name' : 'Trump',
  #     'education' : 'University of America',
  #     'current_location' : 'Los Angles, BT',
  #     'hr_rate' : 'CAD$20-30',
  #   },
  #   {
  #     'first_name' : 'Barack',
  #     'last_name' : 'Obama',
  #     'education' : 'University of America',
  #     'current_location' : 'Victoria, BC',
  #     'hr_rate' : 'CAD$30-40',
  #   },
  # ]

  # for x in range(len(persons)):
  #   add_person_profile(persons[x])
  return 'testing'

# def add_person_profile(person):
#   person_first_name = person['first_name']
#   person_last_name = person['last_name']
#   person_education = person['education']
#   person_current_location = person['current_location']
#   person_hr_rate = person['hr_rate']

#   try:
#     table = dynamodb.Table('user_profile')
#   except botocore.exceptions.ClientError as e:
#     # http://stackoverflow.com/questions/33068055/boto3-python-and-how-to-handle-errors
#     return 'failed'
#   else:
#     token = uuid.uuid4().hex

#     response = table.put_item(
#       Item={
#         'user_id': token,
#         'first_name': person_first_name,
#         'last_name': person_last_name,
#         'education': person_education,
#         'current_location': person_current_location,
#         'hr_rate': person_hr_rate
#       }
#     )
#     # if response['ResponseMetadata']['HTTPStatusCode'] == 200:

def get_list_of_tutors(param):
  filter_expression = []
  expression_attribute_names = {}
  expression_attribute_values = {}
  try:
    q = param['q']
    filter_expression.append('(#q = :q)')
    expression_attribute_names['#q'] = 'last_name'
    expression_attribute_values[':q'] = q
  except KeyError:
    pass
  try:
    m_p = param['m_p']
    filter_expression.append('(#p <= :m_p)')
    expression_attribute_names['#p'] = 'hr_rate'
    expression_attribute_values[':m_p'] = m_p
  except KeyError:
    pass
  try:
    l = param['l']
    filter_expression.append('(#l = :l)')
    expression_attribute_names['#l'] = 'current_location'
    expression_attribute_values[':l'] = l
  except KeyError:
    pass

  try:
    table = dynamodb.Table('user_profile')
  except botocore.exceptions.ClientError as e:
    # http://stackoverflow.com/questions/33068055/boto3-python-and-how-to-handle-errors
    return 'failed'
  else:
    if filter_expression_to_string(filter_expression) != '' and expression_attribute_names and expression_attribute_values:
      response = table.scan(
        FilterExpression = filter_expression_to_string(filter_expression),
        ExpressionAttributeNames = expression_attribute_names,
        ExpressionAttributeValues = expression_attribute_values,
      )
    else:
      response = table.scan(
        ReturnConsumedCapacity = 'TOTAL',
      )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
      items = response['Items']
      return items

def filter_expression_to_string(filter_expression):
  if not filter_expression:
    return ''
  length_of_filter_expression = len(filter_expression)
  filter_expression_to_string = ''
  for x in range(length_of_filter_expression):
    filter_expression_to_string += filter_expression[x]
    if x + 1 != length_of_filter_expression:
      filter_expression_to_string += ' and '
  return filter_expression_to_string

def get_user_meta_data(user_id):
  try:
    table = dynamodb.Table('user_profile')
  except botocore.exceptions.ClientError as e:
    # http://stackoverflow.com/questions/33068055/boto3-python-and-how-to-handle-errors
    return 'failed'
  else:
    response = table.get_item(
      Key={
        'user_id' : user_id
      }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
      try:
        item = response['Item']
      except KeyError:
        return None
      return item