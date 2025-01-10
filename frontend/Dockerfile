# Base image with Node.js
FROM node:18-alpine

# Set working directory in the container
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy only package.json and pnpm-lock.yaml for caching dependencies
COPY package.json pnpm-lock.yaml ./

# Install dependencies using pnpm
RUN pnpm install

# Copy the entire project to the container
COPY . .

# Expose the development server port (default Vite port: 5173)
EXPOSE 3000

# Start the development server
CMD ["pnpm", "dev", "--host", "0.0.0.0"]