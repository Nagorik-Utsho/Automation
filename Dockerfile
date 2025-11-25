# Use a base image with Appium, Android emulator, and tools (for Android 8.1; change as needed)
FROM budtmo/docker-android-x86-8.1

# Set environment variables for Python and Appium
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APPIUM=true
ENV APPIUM_HOST="127.0.0.1"
ENV APPIUM_PORT=4723
ENV DEVICE="Samsung Galaxy S6"  # Emulator device; ignore for real devices

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy your scripts and APK (if any)
COPY tests/ /app/tests/
COPY app.apk /app/app.apk  # Optional: Your APK

# Expose ports: Appium (4723), VNC for emulator UI (6080), ADB (5554-5555)
EXPOSE 4723 6080 5554 5555

# Default command: Start Appium and run your Python script/tests
CMD ["sh", "-c", "appium & sleep 10 && pytest /app/tests -v"]

# Use a base image with Appium, Android emulator, and tools (for Android 8.1; change as needed)
FROM budtmo/docker-android-x86-8.1

# Set environment variables for Python and Appium
ENV PYTHONDONTWRITEBYTECODE=13
ENV PYTHONUNBUFFERED=1
ENV APPIUM=true
ENV APPIUM_HOST="127.0.0.1"
ENV APPIUM_PORT=4723
ENV DEVICE="Samsung Galaxy S6"  # Emulator device; ignore for real devices

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy your scripts and APK (if any)
COPY tests/ /app/tests/
COPY app.apk /app/app.apk  # Optional: Your APK

# Expose ports: Appium (4723), VNC for emulator UI (6080), ADB (5554-5555)
EXPOSE 4723 6080 5554 5555

# Default command: Start Appium and run your Python script/tests
CMD ["sh", "-c", "appium & sleep 10 && pytest /app/tests -v"]