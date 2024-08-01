# Використання базового образу Python
FROM python:3.10-slim

# Встановлення необхідних бібліотек
RUN pip install PyPDF2 reportlab

# Створення робочої директорії
WORKDIR /app

# Копіювання вашого скрипта в робочу директорію
COPY merge_pdfs.py .

# Команда за замовчуванням для запуску контейнера
CMD ["python", "merge_pdfs.py"]

