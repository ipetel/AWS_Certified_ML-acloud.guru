'''
this code is based on AWS lambda blueprint 'kinesis-firehose-process-record-python'
I have used runtime Python 3.7 but I'm sure Python 2.7 will work too.
'''

import json
import base64

def lambda_handler(event, context):
	output = []
	
	for record in event['records']:
		print(record['recordId'])
		payload = json.loads(base64.b64decode(record['data']))
		
		for user in payload['results']:
			if int(user['dob']['age'])>=21:
				res={}
				res['first_name']=user['name']['first']
				res['last_name']=user['name']['last']
				res['age']=user['dob']['age']
				res['gender']=user['gender']
				res['latitude']=user['location']['coordinates']['latitude']
				res['longitude']=user['location']['coordinates']['longitude']

				output_record = {
					'recordId': record['recordId'],
					'result': 'Ok',
					'data': base64.b64encode(json.dumps(res).encode('utf-8')).decode('utf-8')
				}
				
				output.append(output_record)

	print('Successfully processed {} records.'.format(len(event['records'])))
	return {'records': output}
