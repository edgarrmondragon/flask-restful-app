# flask-restful-app

A simple Flask RESTful app based on a Udemy course by Jośe Salvatierra.

## Table of contents

- [Retrieve items](#Retrieve-items)
- [Retrieve stores](#Retrieve-stores)

## Retrieve items

### Request

```console
curl http://mydomain.com/items
```

### Response

```json
{
  "items": [
    {
      "name": "guitar",
      "price": 74.99
    },
    {
      "name": "piano",
      "price": 399.99
    }
  ]
}
```

## Retrieve stores

### Request

```console
curl http://mydomain.com/stores
```

### Response

```json
{
  "stores": [
    {
      "name": "walmart",
      "items": [
        {
          "name": "guitar",
          "price": 74.99
        },
        {
          "name": "piano",
          "price": 399.99
        }
      ]
    }
  ]
}
```
