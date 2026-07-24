#!/bin/bash

echo "Running GST App Tests..."
echo "======================"

pytest tests/ -v --tb=short

echo ""
echo "======================"
echo "Tests Complete!"
echo "======================"
