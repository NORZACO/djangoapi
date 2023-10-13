#!/bin/bash

# Prompt for user input
read -p "Enter the price: " price
read -p "Enter the product name: " name
read -p "Enter the product description: " description

# Make the API request using curl
curl -X POST http://127.0.0.1:8000/api/v1/products/create -d "price=$price" -d "name=$name" -d "description=$description"
