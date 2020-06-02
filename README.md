# Python Cypher Module for Morpheus

## Usage

```
pip install morpheus-cypher

python
>>> from morpheuscypher import Cypher
>>> c = Cypher(url="<Morpheus URL>", token="<token>")
>>> c.get("<secretid>")
>>> c.get("secret/test")
```