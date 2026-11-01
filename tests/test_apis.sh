#!/bin/bash
set -e

echo "Testing Product API..."
curl -fsS http://localhost:5001/products
echo

echo "Testing Order API..."
curl -fsS http://localhost:5002/orders
echo

echo "Creating a test order..."
curl -fsS -X POST http://localhost:5002/orders \
  -H "Content-Type: application/json" \
  -d '{"product_id":1,"quantity":1}'
echo

echo "All API checks passed!"
