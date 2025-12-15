const token = "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";

async function testHFAPI() {
  console.log("Testing Hugging Face API with Stable Diffusion XL...");
  console.log("Token:", token.substring(0, 20) + "...");

  try {
    const response = await fetch(
      "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        method: "POST",
        body: JSON.stringify({
          inputs: "A beautiful sunset over mountains, high quality, 8K",
        }),
      }
    );

    console.log("Response Status:", response.status);
    
    if (response.ok) {
      const blob = await response.blob();
      console.log("✓ Image Generated Successfully!");
      console.log("Image Size:", blob.size, "bytes");
    } else {
      const errorText = await response.text();
      console.log("✗ API Error:", errorText);
    }
  } catch (error) {
    console.error("✗ Test Failed:", error.message);
  }
}

testHFAPI();
