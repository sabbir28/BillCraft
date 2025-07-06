from .pdf_template import InvoicePDF
from .colors import *

class InvoiceGenerator:
    def __init__(self, order_data, filename="invoice.pdf"):
        self.order_data = order_data
        self.filename = filename
        self.pdf = InvoicePDF()
        self.pdf.add_page()

    def add_section_header(self, title):
        self.pdf.ln(6)
        self.pdf.set_font("Arial", "B", 11)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.set_fill_color(*ACCENT)
        self.pdf.cell(0, 9, title.upper(), ln=True, fill=True)
        self.pdf.set_draw_color(*ACCENT)
        self.pdf.set_line_width(0.7)
        self.pdf.line(10, self.pdf.get_y(), 200, self.pdf.get_y())
        self.pdf.ln(2)
        self.pdf.set_line_width(0.3)

    def add_two_column(self, left_title, left_value, right_title, right_value):
        self.pdf.set_text_color(*DARK_GRAY)
        self.pdf.set_font("Arial", "B", 10)
        self.pdf.set_fill_color(*LIGHT_GRAY)
        self.pdf.cell(45, 8, left_title, fill=True)
        self.pdf.set_font("Arial", "", 10)
        self.pdf.cell(50, 8, str(left_value), fill=True)
        self.pdf.set_font("Arial", "B", 10)
        self.pdf.cell(45, 8, right_title, fill=True)
        self.pdf.set_font("Arial", "", 10)
        self.pdf.cell(50, 8, str(right_value), ln=True, fill=True)
        self.pdf.ln(1)

    def add_key_values(self, data, col_count=2):
        keys = list(data.keys())
        for i in range(0, len(keys), col_count):
            row_keys = keys[i:i + col_count]
            for key in row_keys:
                self.pdf.set_font("Arial", "B", 10)
                self.pdf.set_text_color(*DARK_GRAY)
                self.pdf.set_fill_color(*LIGHT_GRAY)
                self.pdf.cell(45, 7, key.replace('_', ' ').capitalize(), fill=True)
                self.pdf.set_font("Arial", "", 10)
                self.pdf.cell(45, 7, str(data[key]), fill=True)
            self.pdf.ln(7)

    def add_price_table(self, item_data):
        self.pdf.set_font("Arial", "B", 10)
        headers = ["Item", "Qty", "Unit Price", "Total"]
        widths = [80, 30, 40, 40]
        self.pdf.set_fill_color(*PRIMARY)
        self.pdf.set_text_color(255, 255, 255)
        for i in range(len(headers)):
            self.pdf.cell(widths[i], 8, headers[i], align='C', fill=True)
        self.pdf.ln()

        self.pdf.set_font("Arial", "", 10)
        self.pdf.set_text_color(*DARK_GRAY)
        self.pdf.set_fill_color(*LIGHT_GRAY)
        self.pdf.cell(widths[0], 8, f"Product #{item_data['product_id']}", fill=True)
        self.pdf.cell(widths[1], 8, str(item_data["quantity"]), align='C', fill=True)
        self.pdf.cell(widths[2], 8, f"${item_data['price_per_unit']:.2f}", align='R', fill=True)
        total_price = item_data["quantity"] * item_data["price_per_unit"]
        self.pdf.cell(widths[3], 8, f"${total_price:.2f}", align='R', ln=1, fill=True)
        self.pdf.ln(2)

        self.pdf.set_font("Arial", "B", 10)
        for label, amount in [
            ("Subtotal", item_data["subtotal"]),
            ("Tax", item_data["tax"]),
            ("Discount", -item_data["discount"]),
            ("Total", item_data["total"]),
        ]:
            if label == "Total":
                self.pdf.set_fill_color(*ACCENT)
                self.pdf.set_text_color(255, 255, 255)
            else:
                self.pdf.set_fill_color(255)
                self.pdf.set_text_color(*DARK_GRAY)
            self.pdf.cell(150, 8, label, align='R', fill=True)
            self.pdf.cell(40, 8, f"${amount:.2f}", align='R', ln=1, fill=True)

    def generate(self):
        self.add_section_header("Customer & Order Info")
        self.add_two_column("Customer Name", self.order_data["customer_info"]["full_name"],
                            "Email", self.order_data["customer_info"]["email"])
        self.add_two_column("Phone", self.order_data["customer_info"]["phone"],
                            "Order Time", self.order_data["legal"]["order_time"])
        self.add_two_column("Invoice No", self.order_data["legal"]["invoice_number"],
                            "Payment ID", self.order_data["payment_info"]["payment_id"])

        self.add_section_header("Shipping Address")
        self.add_key_values(self.order_data["shipping_address"])

        self.add_section_header("Billing Address")
        if self.order_data["billing_address"].get("same_as_shipping"):
            self.pdf.set_font("Arial", "", 10)
            self.pdf.set_text_color(*DARK_GRAY)
            self.pdf.cell(0, 7, "Same as Shipping Address", ln=True)
        else:
            self.add_key_values(self.order_data["billing_address"])

        self.add_section_header("Payment Information")
        self.add_key_values(self.order_data["payment_info"])

        self.add_section_header("Order Details")
        self.add_price_table(self.order_data["order_info"])

        self.pdf.output(self.filename)
