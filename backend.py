from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import requests
import base64
import os
from io import BytesIO

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
HF_TOKEN = os.getenv("HUGGING_FACE_TOKEN", "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")
HF_API_URL = "https://api-inference.huggingface.co/models"

# Models to use
MODELS = {
    "stable-diffusion-xl": "stabilityai/stable-diffusion-xl-base-1.0",
    "stable-diffusion-3": "stabilityai/stable-diffusion-3.5-large",
    "dreamshaper": "Lykon/dreamshaper-8",
}

class ImageRequest(BaseModel):
    prompt: str
    model: str = "stable-diffusion-xl"
    style: Optional[str] = None
    quality: Optional[str] = "high"
    size: Optional[str] = "768x768"

def enhance_prompt(prompt: str, style: Optional[str] = None, quality: Optional[str] = None) -> str:
    """Enhance the prompt with style and quality hints"""
    enhanced = prompt
    
    quality_guides = {
        "low": "Quick draft quality",
        "medium": "Good quality, balanced detail",
        "high": "Ultra high quality, maximum detail, professional grade, 8K resolution",
    }
    
    if quality and quality in quality_guides:
        enhanced += f". {quality_guides[quality]}"
    
    if style and style != "default":
        enhanced += f". Style: {style}"
    
    return enhanced

def generate_image_with_hf(prompt: str, model_name: str, style: Optional[str] = None, quality: Optional[str] = None) -> Optional[str]:
    """Generate image using Hugging Face Inference API"""
    
    if model_name not in MODELS:
        raise ValueError(f"Model {model_name} not found")
    
    model_id = MODELS[model_name]
    enhanced_prompt = enhance_prompt(prompt, style, quality)
    
    print(f"Generating image with {model_name}")
    print(f"Model ID: {model_id}")
    print(f"Prompt: {enhanced_prompt[:100]}...")
    
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
    }
    
    payload = {
        "inputs": enhanced_prompt,
        "parameters": {
            "negative_prompt": "blurry, low quality, distorted, ugly",
            "num_inference_steps": 50 if quality == "high" else 30 if quality == "medium" else 20,
            "guidance_scale": 7.5,
            "height": 768,
            "width": 768,
        }
    }
    
    try:
        # Try with the new router endpoint
        response = requests.post(
            f"https://router.huggingface.co/models/{model_id}",
            headers=headers,
            json=payload,
            timeout=120
        )
        
        print(f"Response Status: {response.status_code}")
        
        if response.status_code == 410:
            # Fall back to direct API
            print("Router endpoint deprecated, trying direct API...")
            response = requests.post(
                f"https://api-inference.huggingface.co/models/{model_id}",
                headers=headers,
                json=payload,
                timeout=120
            )
        
        if response.status_code == 200:
            # Convert image to base64
            image_data = base64.b64encode(response.content).decode('utf-8')
            return f"data:image/png;base64,{image_data}"
        else:
            error_text = response.text
            print(f"API Error: {response.status_code} - {error_text}")
            raise Exception(f"API Error: {response.status_code}")
            
    except requests.exceptions.Timeout:
        raise Exception("Request timeout - image generation took too long")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {str(e)}")

@app.get("/")
async def root():
    return {"message": "CodeBloom AI Hub Backend", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "codebloom-ai-hub"}

@app.post("/api/generate-image")
async def generate_image(request: ImageRequest):
    """Generate an image based on the prompt"""
    try:
        if not request.prompt:
            raise HTTPException(status_code=400, detail="Prompt is required")
        
        print(f"Image generation request: {request.prompt[:50]}...")
        
        image_url = generate_image_with_hf(
            prompt=request.prompt,
            model_name=request.model,
            style=request.style,
            quality=request.quality
        )
        
        if not image_url:
            raise HTTPException(status_code=500, detail="Failed to generate image")
        
        return {
            "success": True,
            "imageUrl": image_url,
            "model": request.model,
            "prompt": request.prompt
        }
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Image generation failed: {str(e)}")

@app.get("/api/models")
async def get_models():
    """Get list of available models"""
    return {
        "models": [
            {
                "id": "stable-diffusion-xl",
                "name": "Stable Diffusion XL",
                "description": "High-quality image generation"
            },
            {
                "id": "stable-diffusion-3",
                "name": "Stable Diffusion 3.5",
                "description": "Latest Stable Diffusion model"
            },
            {
                "id": "dreamshaper",
                "name": "DreamShaper",
                "description": "Artistic image generation"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
