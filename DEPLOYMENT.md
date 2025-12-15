# CodeBloom AI Hub - Deployment Guide

## Overview

This is a full-stack application with:
- **Frontend**: React + TypeScript (Vite)
- **Backend**: Python FastAPI with Hugging Face integration
- **Image Generation**: Stable Diffusion models via Hugging Face API

## Prerequisites

1. **Node.js** (v18+)
2. **Python** (v3.9+)
3. **Hugging Face Token** (free account at https://huggingface.co)

## Setup Instructions

### 1. Install Dependencies

```bash
# Install Node dependencies
npm install

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Frontend Configuration
VITE_SUPABASE_PROJECT_ID="obzioxpqwjteudusfjat"
VITE_SUPABASE_PUBLISHABLE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9iemlveHBxd2p0ZXVkdXNmamF0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjU1ODk0MjUsImV4cCI6MjA4MTE2NTQyNX0.tfEbfqjV_tG0LaDM8o_RZzSGzRgJDH82kIN7N5pj6nw"
VITE_SUPABASE_URL="https://obzioxpqwjteudusfjat.supabase.co"

# Backend Configuration
VITE_BACKEND_URL="http://localhost:8000"  # For local development
# For production, change to your deployed backend URL

# Hugging Face Token (get from https://huggingface.co/settings/tokens)
HUGGING_FACE_TOKEN="your_hf_token_here"
```

### 3. Local Development

**Terminal 1 - Start Backend:**
```bash
source venv/bin/activate
python backend.py
# Backend runs on http://localhost:8000
```

**Terminal 2 - Start Frontend:**
```bash
npm run dev
# Frontend runs on http://localhost:5173
```

Visit http://localhost:5173 in your browser.

### 4. Build for Production

```bash
npm run build
# Creates optimized build in `dist/` directory
```

## Deployment Options

### Option 1: Deploy on Render.com (Recommended)

1. **Create Render account** at https://render.com
2. **Connect GitHub repository**
3. **Create Web Service:**
   - **Build Command**: `npm install && npm run build && pip install -r requirements.txt`
   - **Start Command**: `npm run build && python backend.py`
   - **Environment Variables**: Add `HUGGING_FACE_TOKEN`

### Option 2: Deploy on Railway.app

1. **Create Railway account** at https://railway.app
2. **Connect GitHub repository**
3. **Set environment variables** in Railway dashboard
4. **Deploy** - Railway auto-detects and deploys

### Option 3: Deploy on Heroku

```bash
heroku create your-app-name
heroku config:set HUGGING_FACE_TOKEN="your_token"
git push heroku main
```

### Option 4: Deploy on AWS/GCP/Azure

Use Docker to containerize the application:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install Node
RUN apt-get update && apt-get install -y nodejs npm

# Copy files
COPY package*.json ./
COPY requirements.txt ./
COPY . .

# Install dependencies
RUN npm install
RUN pip install -r requirements.txt

# Build frontend
RUN npm run build

# Expose ports
EXPOSE 8000 3000

# Start backend
CMD ["python", "backend.py"]
```

## API Endpoints

### Health Check
```
GET /health
```

### Generate Image
```
POST /api/generate-image
Content-Type: application/json

{
  "prompt": "A beautiful sunset over mountains",
  "model": "stable-diffusion-xl",
  "style": "photorealistic",
  "quality": "high",
  "size": "768x768"
}
```

**Response:**
```json
{
  "success": true,
  "imageUrl": "data:image/png;base64,...",
  "model": "stable-diffusion-xl",
  "prompt": "A beautiful sunset over mountains"
}
```

### Get Available Models
```
GET /api/models
```

## Troubleshooting

### Backend not responding
- Check if backend is running: `curl http://localhost:8000/health`
- Check logs for errors
- Ensure Python virtual environment is activated

### Image generation fails
- Verify Hugging Face token is valid
- Check if token has sufficient credits
- Try with a simpler prompt

### CORS errors
- Backend CORS is configured for all origins (`*`)
- Ensure frontend URL is correct in `VITE_BACKEND_URL`

### Rate limiting
- Hugging Face API has rate limits
- Wait a moment and retry
- Consider upgrading Hugging Face account for higher limits

## Performance Tips

1. **Use production builds**: `npm run build`
2. **Enable caching** on your hosting platform
3. **Optimize images** before uploading
4. **Monitor API usage** on Hugging Face dashboard
5. **Use CDN** for static assets

## Security Notes

- Never commit `.env` file to git
- Use environment variables for sensitive data
- Rotate Hugging Face token regularly
- Monitor API usage for unusual activity
- Use HTTPS in production

## Support

For issues or questions:
1. Check Hugging Face documentation: https://huggingface.co/docs
2. Review FastAPI docs: https://fastapi.tiangolo.com
3. Check React/Vite docs: https://vitejs.dev

## License

MIT
