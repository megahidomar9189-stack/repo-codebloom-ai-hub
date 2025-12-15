const apiKey = "AIzaSyAxyq9bM7hzh4E864wcCQI4vTP3nqbGrxo";

async function testGeminiAPI() {
  console.log("Testing Google Gemini API...");
  console.log("API Key:", apiKey.substring(0, 20) + "...");

  try {
    const response = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          contents: [
            {
              parts: [
                {
                  text: "Write a short poem about technology",
                },
              ],
            },
          ],
          generationConfig: {
            temperature: 0.7,
            topK: 40,
            topP: 0.95,
            maxOutputTokens: 200,
          },
        }),
      }
    );

    console.log("Response Status:", response.status);
    const data = await response.json();
    
    if (response.ok) {
      console.log("✓ API Connection: SUCCESS");
      console.log("Generated Content:", data.candidates?.[0]?.content?.parts?.[0]?.text || "No content");
    } else {
      console.log("✗ API Error:", data.error?.message);
    }
  } catch (error) {
    console.error("✗ Test Failed:", error.message);
  }
}

testGeminiAPI();
