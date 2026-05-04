FROM python:3.10

# Set working directory
WORKDIR /app

# Copy semua file aplikasi
COPY . /app

# Install dependency
RUN pip install flask flask-talisman

# Buat user non-root (security requirement)
RUN useradd -m appuser
RUN chown -R appuser:appuser /app

# Pindah ke user non-root
USER appuser

# Expose port Flask
EXPOSE 8080

# Jalankan aplikasi
CMD ["python", "app.py"]