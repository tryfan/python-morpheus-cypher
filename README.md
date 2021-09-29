# Python Cypher Module for Morpheus


## Installation
`pip install morpheus-cypher`
## Usage

```
python
>>> from morpheuscypher import Cypher
>>> c = Cypher(url="<Morpheus URL>", token="<token>")
>>> c.get("<secretid>")
>>> c.get("secret/test")
```

## Variables
When creating connection:
- `url`: Morpheus URL
- `token`: Morpheus token
- `morpheus`: Morpheus variable when running from the Morpheus python task type.  Pass this in as morpheus=morpheus
- `ssl_verify`: Specify strict SSL verification, default is True

When getting a secret, use `<type>/<name>` eg. `secret/test`

Elements within the secret can also be selected by using `secret/test:element`