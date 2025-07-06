# BillCraft

**BillCraft** is a lightweight modular invoice generator built with FPDF for generating professional PDFs for e-commerce use cases.

## Features

- Clean layout with branding
- Modular class-based API
- Easily customizable color themes
- Shipping, billing, product, and payment info sections



## Usage

```python
from invoice.generator import InvoiceGenerator
from datetime import datetime

# Provide your `order_data` dictionary...
invoice = InvoiceGenerator(order_data, "output.pdf")
invoice.generate()
