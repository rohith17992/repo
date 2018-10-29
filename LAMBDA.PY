import json
import boto3

namef=[]
def add ( str ):
    clien = boto3.client('lambda')
    response=clien.list_functions(Marker='{0}'.format(str))
    for i in response['Functions']:
        namef.append('{0}'.format(i['FunctionName']))
    try:
        marker=response['NextMarker']
        return marker
    except Exception, e:
        raise e
        return 'No'
    
    


def lambda_handler(event, context):
    
    clien = boto3.client('lambda')
    response=clien.list_functions()
    for i in response['Functions']:
        namef.append('{0}'.format(i['FunctionName']))
    
    try:
        marker=response['NextMarker']
        response=clien.list_functions(Marker='{0}'.format(marker))
        ds=add("{0}".format(marker))
        print (ds)
        while (ds != 'No'):
            add ('{0}'.format(ds))
    except Exception, e:
        print ("Not Too much functions")
   
    
    # TODO implement
    for i in namef:
        client = boto3.client('cloudwatch')
        response = client.put_metric_alarm(AlarmName='Non-Prod ErrorLambda-{0}'.format(i),
            AlarmDescription='Trigger Notification when lammda fails',
            ActionsEnabled=False,
            AlarmActions=[
                'arn:aws:sns:us-west-2:937385968647:CLoudwatch',
            ],
            MetricName='Errors',
            Namespace='AWS/Lambda',
            Statistic='Average',
            Period=60,
            EvaluationPeriods=1,
            DatapointsToAlarm=1,
            Threshold=1,
            Dimensions=[
                            {
                                'Name': 'FunctionName',
                                'Value': '{0}'.format(i)
                            }
                        ],
            ComparisonOperator='GreaterThanOrEqualToThreshold'
        )
