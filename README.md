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

Examples can be found in the [examples](examples) directory, for both local testing and Morpheus testing.

## Variables
When creating connection:
- `url`: Morpheus URL
- `token`: Morpheus token
- `morpheus`: Morpheus variable when running from the Morpheus python task type.  Pass this in as morpheus=morpheus
- `ssl_verify`: Specify strict SSL verification, default is True
- `cypher_endpoint`: If using Morpheus version < 5.3.3, set this to `/api/cypher/v1/`

## Get
When getting a secret, use `<type>/<name>` eg. `secret/test`

Elements within the secret can also be selected by using `secret/test:element`

## Write
When writing a secret, use `<type>/<name>` for the `secret_key` eg. `secret/test`

The `secret_value` may be supplied or the secret will be be created with a `null` value.

The `ttl` can be set for a lease time, which the secret will be automatically deleted once the TTL expires.  By default,
if omitted, the TTL is `0`, which is unlimited. The TTL is in seconds but can also be submitted using abbreviated
duration format, such as:
* 5m
* 2h
* 1d
* 5y

When writing generated Cypher types, only the key is required:  `<type>/<name>` eg. `secret/test`
Optionally, the TTL can also be specified.  Generated Cypher types include:
* password
* uuid
* key

The value set in the Cypher will be returned upon successful completion.

## Delete
When deleting a secret, use `<type>/<name>` for the `secret_key` eg. `secret/test`

No other arguments are required, except for the `secret_key`.

A boolean from successful completion will be returned.