import pdfplumber
import re


def extract_invoice_details_dynamic(pdf_path):
    details = {
        "vendor_info": None,
        "invoice_info": None,
        "items": [],
        "taxes": {},
        "total": None
    }

    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

        print(text)

        # Dynamically find Vendor Information (Assuming Address and GSTIN exist)
        vendor_match = re.search(
            r"(?i)(\bvendor\b|gstin.*?\b\d{15}\b)", text, re.DOTALL)
        if vendor_match:
            vendor_start = vendor_match.start()
            vendor_end = vendor_start + 300  # Limit the address search range
            vendor_text = text[vendor_start:vendor_end].splitlines()
            vendor_info = [line for line in vendor_text if line.strip() != ""]
            details["vendor_info"] = "\n".join(vendor_info)

        # Dynamically find Invoice Number and Date
        invoice_no_match = re.search(r"(?i)invoice\s*no\.?\s*(\d+)", text)
        invoice_date_match = re.search(
            r"(?i)(dated|date)\s*[:\s]*(\d{1,2}[-/][A-Za-z]{3}[-/]\d{2,4})", text)
        if invoice_no_match and invoice_date_match:
            details['invoice_info'] = {
                'invoice_no': invoice_no_match.group(1),
                'date': invoice_date_match.group(2)
            }

        # Dynamically extract items
        item_lines = re.findall(
            r"(\d+)\s+([a-zA-Z0-9 ]+)\s+([\d,]+\.\d{2})Kg\s+([\d,]+\.\d{2})", text)
        for line in item_lines:
            quantity = float(line[2].replace(",", ""))
            total_amount = float(line[3].replace(",", ""))
            item_name = line[1].strip()
            details['items'].append({
                "item": item_name,
                "quantity": quantity,
                "total_amount": total_amount
            })

        # Dynamically find CGST, SGST, and Total
        cgst_match = re.search(r"CGST\s*([\d,]+\.\d{2})", text)
        sgst_match = re.search(r"SGST\s*([\d,]+\.\d{2})", text)
        total_match = re.search(r"Total\s*₹\s*([\d,]+\.\d{2})", text)

        if cgst_match:
            details["taxes"]["CGST"] = float(
                cgst_match.group(1).replace(",", ""))
        if sgst_match:
            details["taxes"]["SGST"] = float(
                sgst_match.group(1).replace(",", ""))
        if total_match:
            details["total"] = float(total_match.group(1).replace(",", ""))

    return details


# Example usage
pdf_path = r"D:\IGS\PB Data Utils Scripts\ocr\ocr_sample_input.pdf"
invoice_details = extract_invoice_details_dynamic(pdf_path)
print(invoice_details)
