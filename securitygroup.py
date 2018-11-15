import json
import boto3
def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('ec2')
    client1 = boto3.client('ec2', 'us-east-1')
    result=client.describe_security_groups()
    result1=client1.describe_security_groups()
    sec1=[]
    sec2=[]
    sec3=[]
    sec4=[]
    for r in result['SecurityGroups']:
        sec1.append(r['GroupName'])
    for i in sec1:
        x=i.replace("us-east-1", "us-west-2")
        sec2.append(x)
    for r in result1['SecurityGroups']:
        sec3.append(r['GroupName'])
    sec4=list(set(sec2)-set(sec3))
    print ("Thsese Sec Group not in DR region")
    print sec4
    sec5=list(set(sec2)-set(sec4))
    
    j=sec5.length
    k=0
    while k < j:
        data = client1.describe_security_groups(GroupNames=[sec1[i]])   
                
                for i in data['SecurityGroups']:
                        direction = 'Ingress'
                        description = i['Description']
                        #Ingress Data
                        finalingress1='-'
                        for ingress in i['IpPermissions']:
                        
                            source = ''
                            #IP Protocol
                            try:
                                ipprotocol = ingress['IpProtocol']
                            except Exception:
                                ipprotocol = '-'

                            #Ports
                            try:
                                fromport   = ingress['FromPort']
                            except Exception:
                                fromport = '-'

                            try:
                                toport     = ingress['ToPort']
                            except Exception:
                                toport = '-'

                            try:
                                for ini in ingress['IpRanges']:
                                    try:
                                        source = ini['CidrIp']
                                    except Exception as e:
                                        source = '-'
                                    finalingress1 += 'Ingress' + ',' + ipprotocol + ',' + str(fromport) + ',' + str(toport) + ',' + str(source) + ',' + description + ',' + str(GroupName) + ',' + str(ownerid) + '\n'
                                    
                            except Exception:
                                continue
                            
                            try:
                                for ini in ingress['Ipv6Ranges']:
                                    tryfinalin += str(hostname) + ',' + 'Ingress' + ',' + ipprotocol + ',' + str(fromport) + ',' + str(toport) + ',' + str(source) + ',' + description + ',' + '\n'                                        source = ini['CidrIpv6']
                                    except Exception as e:
                                        source = '-'
                                    finalingress1 += 'Ingress' + ',' + ipprotocol + ',' + str(fromport) + ',' + str(toport) + ',' + str(source) + ',' + description + ',' + str(GroupName) + ',' + str(ownerid) + '\n'
                            except Exception:
                                continue

        data1 = client.describe_security_groups(GroupNames=[sec2[i]])   
                
                for i in data['SecurityGroups']:
                        direction = 'Ingress'
                        description = i['Description']
                        #Ingress Data
                        finalingress=''
                        for ingress in i['IpPermissions']:
                        
                            source = ''
                            #IP Protocol
                            try:
                                ipprotocol = ingress['IpProtocol']
                            except Exception:
                                ipprotocol = '-'

                            #Ports
                            try:
                                fromport   = ingress['FromPort']
                            except Exception:
                                fromport = '-'

                            try:
                                toport     = ingress['ToPort']
                            except Exception:
                                toport = '-'

                            try:
                                for ini in ingress['IpRanges']:
                                    try:
                                        source = ini['CidrIp']
                                    except Exception as e:
                                        source = '-'
                                    finalingress += 'Ingress' + ',' + ipprotocol + ',' + str(fromport) + ',' + str(toport) + ',' + str(source) + ',' + description + ',' + str(GroupName) + ',' + str(ownerid) + '\n'
                                    
                            except Exception:
                                continue
                            
                            try:
                                for ini in ingress['Ipv6Ranges']:
                                    tryfinalin += str(hostname) + ',' + 'Ingress' + ',' + ipprotocol + ',' + str(fromport) + ',' + str(toport) + ',' + str(source) + ',' + description + ',' + '\n'                                        source = ini['CidrIpv6']
                                    except Exception as e:
                                        source = '-'
                                    finalingress += 'Ingress' + ',' + ipprotocol + ',' + str(fromport) + ',' + str(toport) + ',' + str(source) + ',' + description + ',' + str(GroupName) + ',' + str(ownerid) + '\n'
                            except Exception:
                                continue
        
        if finalingress == finalingress1:
            print ""
        else:
            print sec2[i]
        
        
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
