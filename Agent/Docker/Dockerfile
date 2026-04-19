# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (improves build caching)
# Point to the actual location relative to your root
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Command to run your script
# Replace 'main.py' with your actual filename
CMD ["python", "Agent/test_build_agent.py"]

# running this:
    # sudo docker build -t hackathon  -f Agent/Docker/Dockerfile .
    # sudo docker run --env-file Agent/.env hackathon
        # or sudo docker run --rm --env-file Agent/.env hackathon