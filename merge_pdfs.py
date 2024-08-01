import os
import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Отримання шляху до папки з PDF файлами
folder_path = '/Yevhenii/pdfs'

if not os.path.exists(folder_path):
    print(f"Папка {folder_path} не існує.")
    exit(1)

# Функція для створення порожньої сторінки
def create_blank_page(output_path, page_size=letter):
    c = canvas.Canvas(output_path, pagesize=page_size)
    c.showPage()
    c.save()

# Отримання списку файлів PDF
files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

# Отримання дат модифікації файлів
files_with_dates = []
for file in files:
    file_path = os.path.join(folder_path, file)
    modification_time = os.path.getmtime(file_path)
    files_with_dates.append((file, modification_time))

# Вивід для діагностики
print("Files with modification dates before sorting:")
for file, modification_time in files_with_dates:
    print(f"{file}: {modification_time}")

# Сортування файлів за датою модифікації
files_with_dates.sort(key=lambda x: x[1])

# Вивід для діагностики
print("Files with modification dates after sorting:")
for file, modification_time in files_with_dates:
    print(f"{file}: {modification_time}")

# Об'єднання файлів
pdf_writer = PyPDF2.PdfWriter()

for file, _ in files_with_dates:
    file_path = os.path.join(folder_path, file)
    pdf_reader = PyPDF2.PdfReader(file_path)
    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # Перевірка на непарну кількість сторінок і додавання білого аркуша
    if num_pages % 2 != 0:
        blank_page_path = os.path.join(folder_path, 'blank_page.pdf')
        create_blank_page(blank_page_path)
        blank_pdf_reader = PyPDF2.PdfReader(blank_page_path)
        pdf_writer.add_page(blank_pdf_reader.pages[0])
        os.remove(blank_page_path)

# Збереження об'єднаного файлу в ту ж саму директорію
output_path = os.path.join(folder_path, 'Готовий-до-друку.pdf')
with open(output_path, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

print(f"Об'єднаний PDF файл збережено як {output_path}")
