from morpheuscypher import Cypher
print(f"Cypher value:  {Cypher(url='https://yourUrl',token='yourApiToken',ssl_verify=False).write('secret/cypherTest','myValue',120)}")
print(f"Cypher value:  {Cypher(url='https://yourUrl',token='yourApiToken',ssl_verify=False).write('uuid/cypherTest1')}")
print(f"Cypher value:  {Cypher(url='https://yourUrl',token='yourApiToken',ssl_verify=False).write('uuid/cypherTest2',ttl=120)}")