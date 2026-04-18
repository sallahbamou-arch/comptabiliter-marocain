import pytesseract
import re
from pdf2image import convert_from_path

class OCRService:
    def extraire_texte(self, file_path):
        # Check if file is a PDF and convert to images
        if file_path.endswith('.pdf'):
            images = convert_from_path(file_path)
            extracted_text = ''
            for image in images:
                extracted_text += pytesseract.image_to_string(image) + '\n'
            return extracted_text
        # If the file is an image
        elif file_path.endswith(('.png', '.jpg', '.jpeg')):
            return pytesseract.image_to_string(file_path)
        else:
            raise ValueError("Unsupported file type. Please provide a PDF or an image file.")

    def extraire_informations_facture(self, text):
        numero_facture_pattern = r'(?i)numero\s*facture[:\s]*(\w+)'
        date_pattern = r'(?i)date[:\s]*(\d{2}/\d{2}/\d{4})'
        montant_ht_pattern = r'(?i)montant\s*ht[:\s]*(\d+(?:[,\.]\d{1,2})?)'
        montant_tva_pattern = r'(?i)montant\s*tva[:\s]*(\d+(?:[,\.]\d{1,2})?)'
        montant_ttc_pattern = r'(?i)montant\s*ttc[:\s]*(\d+(?:[,\.]\d{1,2})?)'

        numero_facture = re.search(numero_facture_pattern, text)
        date = re.search(date_pattern, text)
        montant_ht = re.search(montant_ht_pattern, text)
        montant_tva = re.search(montant_tva_pattern, text)
        montant_ttc = re.search(montant_ttc_pattern, text)

        return {
            'numero_facture': numero_facture.group(1) if numero_facture else None,
            'date': date.group(1) if date else None,
            'montant_ht': montant_ht.group(1) if montant_ht else None,
            'montant_tva': montant_tva.group(1) if montant_tva else None,
            'montant_ttc': montant_ttc.group(1) if montant_ttc else None,
        }