from morpheuscypher import Cypher
print(f"Cypher value:  {Cypher(morpheus=morpheus,ssl_verify=False).get('secret/cypherTest')}")