'''
I have used AWS CLI (with Programmatic access) to run the next code on my Mac, 
and already installed boto3 using 'pip'

don't forget to change the next parameters:
1) region_name
2) DeliveryStreamName
'''

import requests
import boto3
import time
import random
import json

client = boto3.client('firehose',region_name='<PUT_HERE_THE_NAME_OF_THE_REGION_YOU_CREATED_THE_FIREHOSE>')
users_limit=500

i=0
while i<users_limit:
	r=requests.get('https://randomuser.me/api/?exc=login')
	data=json.dumps(r.json())
	client.put_record(
		DeliveryStreamName='<PUT_HERE_THE_NAME_OF_THE_FIREHOSE>',
		Record={'Data':data}
	)
	time.sleep(random.uniform(0,1))
	print(i,{'Data':data})
	i+=1
