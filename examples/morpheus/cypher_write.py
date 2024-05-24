from morpheuscypher import Cypher
print(f"Cypher value:  {Cypher(morpheus=morpheus,ssl_verify=False).write('secret/cypherTest','myValue',120)}")