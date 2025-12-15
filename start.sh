#!/bin/bash

# CodeBloom AI Hub - Startup Script

echo "🚀 Starting CodeBloom AI Hub..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🐍 Activating Python virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📚 Installing Python dependencies..."
pip install -q -r requirements.txt

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📚 Installing Node dependencies..."
    npm install
fi

# Build frontend if dist doesn't exist
if [ ! -d "dist" ]; then
    echo "🔨 Building frontend..."
    npm run build
fi

# Start the application
echo ""
echo "✅ Starting application..."
echo "📱 Frontend: http://localhost:3000"
echo "🔌 Backend API: http://localhost:8000"
echo "📖 API Docs: http://localhost:8000/docs"
echo ""

# Start backend in background
echo "Starting backend..."
python backend.py &
BACKEND_PID=$!

# Start frontend server
echo "Starting frontend..."
npm run preview

# Cleanup on exit
trap "kill $BACKEND_PID" EXIT
