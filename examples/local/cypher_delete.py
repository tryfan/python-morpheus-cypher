from morpheuscypher import Cypher
print(f"Cypher value:  {Cypher(url='https://yourUrl',token='yourApiToken',ssl_verify=False).delete('secret/cypherTest')}")