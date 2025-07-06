from invoice.generator import InvoiceGenerator
from datetime import datetime

order_data = {
    "order_info": {
        "product_id": "PROD12345",
        "quantity": 2,
        "variants": {"size": "M", "color": "Red"},
        "price_per_unit": 150.00,
        "subtotal": 300.00,
        "tax": 30.00,
        "discount": 20.00,
        "total": 310.00,
    },
    "customer_info": {
        "full_name": "John Doe",
        "email": "john@example.com",
        "phone": "+880123456789",
        "user_id": "user_789",
    },
    "shipping_address": {
        "name": "John Doe",
        "house": "123A",
        "street": "Baker Street",
        "city": "Dhaka",
        "postcode": "1207",
        "district": "Dhaka",
        "country": "Bangladesh",
    },
    "billing_address": {
        "same_as_shipping": True
    },
    "payment_info": {
        "payment_id": "TXN123456",
        "status": "Success",
        "amount_paid": 310.00,
        "method": "bKash",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    "legal": {
        "invoice_number": "INV10001",
        "order_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
}

invoice = InvoiceGenerator(order_data, "output_invoice.pdf")
invoice.generate()
