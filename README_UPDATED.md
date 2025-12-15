# CodeBloom AI Hub - Updated with Hugging Face Integration

## 🎯 What's New

This is the **updated version** of CodeBloom Core with:

✅ **Python FastAPI Backend** - Fast, scalable API for image generation
✅ **Hugging Face Integration** - Access to Stable Diffusion models
✅ **Real Image Generation** - Actually generates images (not mocked)
✅ **Production Ready** - Ready to deploy online

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  React Frontend (Vite)                  │
│              http://localhost:5173                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ HTTP/REST API
                     │
┌────────────────────▼────────────────────────────────────┐
│              Python FastAPI Backend                     │
│              http://localhost:8000                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ API Calls
                     │
┌────────────────────▼────────────────────────────────────┐
│            Hugging Face Inference API                   │
│        (Stable Diffusion Models)                        │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install Node packages
npm install

# Create and activate Python virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Python packages
pip install -r requirements.txt
```

### 2. Get Hugging Face Token

1. Go to https://huggingface.co/
2. Sign up (free account)
3. Go to Settings → Access Tokens
4. Create a new token (type: read)
5. Copy the token

### 3. Configure Environment

Update `.env` file:
```env
HUGGING_FACE_TOKEN="hf_your_token_here"
VITE_BACKEND_URL="http://localhost:8000"
```

### 4. Run Locally

**Terminal 1 - Backend:**
```bash
source venv/bin/activate
python backend.py
```

**Terminal 2 - Frontend:**
```bash
npm run dev
```

Visit http://localhost:5173

## 📦 Project Structure

```
codebloom-core-main/
├── backend.py                 # FastAPI backend
├── requirements.txt           # Python dependencies
├── src/
│   ├── components/
│   │   └── ai-hub/
│   │       └── ImageGenerator.tsx  # Image generation UI
│   ├── hooks/
│   │   └── useAIImage.ts      # API integration hook
│   └── lib/
│       └── ai-models.ts       # Model definitions
├── dist/                      # Built frontend
├── venv/                      # Python virtual environment
├── DEPLOYMENT.md              # Deployment guide
└── start.sh                   # Startup script
```

## 🎨 Features

### Image Generation
- **Multiple Models**: Stable Diffusion XL, Stable Diffusion 3.5, DreamShaper
- **Customization**: Style, quality, size options
- **Real-time**: Generates actual images using Hugging Face API

### UI Components
- Modern React interface with Tailwind CSS
- Real-time loading states
- Image history and management
- Model selection
- Quality and style customization

## 🔧 Available Models

1. **Stable Diffusion XL** - High-quality, versatile
2. **Stable Diffusion 3.5** - Latest version, better quality
3. **DreamShaper** - Artistic, creative outputs

## 📡 API Endpoints

### Health Check
```bash
curl http://localhost:8000/health
```

### Generate Image
```bash
curl -X POST http://localhost:8000/api/generate-image \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A beautiful sunset over mountains",
    "model": "stable-diffusion-xl",
    "quality": "high"
  }'
```

### List Models
```bash
curl http://localhost:8000/api/models
```

## 🌐 Deploy Online

### Option 1: Render.com (Easiest)
1. Push code to GitHub
2. Create new Web Service on Render
3. Connect repository
4. Add `HUGGING_FACE_TOKEN` environment variable
5. Deploy!

### Option 2: Railway.app
1. Connect GitHub
2. Add environment variables
3. Deploy automatically

### Option 3: Heroku
```bash
heroku create your-app-name
heroku config:set HUGGING_FACE_TOKEN="your_token"
git push heroku main
```

See `DEPLOYMENT.md` for detailed instructions.

## ⚙️ Configuration

### Backend Settings (backend.py)
- `HF_TOKEN`: Hugging Face API token
- `HF_API_URL`: API endpoint
- `MODELS`: Available models

### Frontend Settings (.env)
- `VITE_BACKEND_URL`: Backend API URL
- `VITE_SUPABASE_*`: Supabase configuration (optional)

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill the process if needed
kill -9 <PID>
```

### Image generation fails
- Check Hugging Face token is valid
- Ensure token has read permissions
- Check internet connection
- Try a simpler prompt

### CORS errors
- Backend has CORS enabled for all origins
- Check `VITE_BACKEND_URL` is correct

### Rate limiting
- Hugging Face has rate limits
- Wait a moment and retry
- Upgrade Hugging Face account for higher limits

## 📊 Performance

- **Image Generation**: 30-60 seconds (depends on model and quality)
- **API Response**: < 1 second (excluding generation time)
- **Frontend Load**: < 2 seconds

## 🔐 Security

- Never commit `.env` file
- Use environment variables for secrets
- Rotate tokens regularly
- Monitor API usage

## 📚 Resources

- [Hugging Face Docs](https://huggingface.co/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [React Docs](https://react.dev)
- [Vite Docs](https://vitejs.dev)

## 📝 License

MIT

## 🤝 Support

For issues:
1. Check the logs
2. Review DEPLOYMENT.md
3. Check Hugging Face status page
4. Open an issue on GitHub

---

**Happy generating! 🎨**
