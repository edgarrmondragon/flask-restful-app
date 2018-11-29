# flask-restful-app

A simple Flask RESTful app based on a Udemy course by Jośe Salvatierra.

## Table of contents

- [Retrieve items](#Retrieve-items)
- [Retrieve stores](#Retrieve-stores)

## Retrieve items

### curl command

```console
curl <url>/items
```

### Output

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

### curl command

```console
curl <url>/stores
```

### Output

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
