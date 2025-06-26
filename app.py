from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        print("=== Chat endpoint called ===")
        user_message = request.json.get('message')
        print(f"User message: {user_message}")
        print(f"OpenAI API key exists: {bool(os.getenv('OPENAI_API_KEY'))}")
        
        # Check if we should use mock responses (set this to True when OpenAI quota is exceeded)
        use_mock_responses = True  # Set to False when your OpenAI billing is resolved
        
        if use_mock_responses:
            print("Using mock responses due to OpenAI quota limitation")
            # Mock responses about Manipur's art and culture
            mock_responses = {
                'dance': "Manipuri dance is one of the eight classical dance forms of India, known for its graceful movements and spiritual themes. It often depicts stories from Hindu mythology, particularly those of Radha and Krishna.",
                'art': "Manipur is renowned for its vibrant art forms including traditional paintings, pottery, and handicrafts. The state's artists are skilled in creating beautiful textiles and intricate designs.",
                'culture': "Manipuri culture is rich and diverse, blending Hindu and indigenous traditions. The state is famous for its festivals, traditional music, and the beautiful Manipuri language.",
                'handloom': "Manipuri handloom textiles are famous for their intricate designs and fine quality. The traditional Manipuri shawls and fabrics are highly prized for their craftsmanship.",
                'pottery': "Traditional Manipuri pottery showcases the artistic skills of local artisans, with beautiful ceramic works that reflect the cultural heritage of the region.",
                'hello': "Hello! Welcome to the Manipur Virtual Art Gallery. I'm here to help you learn about the rich artistic heritage of Manipur, a beautiful state in Northeast India.",
                'default': "Thank you for your interest in Manipur's art and culture! Manipur, known as the 'Jewel of India,' is a northeastern state rich in artistic traditions including classical dance, handloom textiles, pottery, and paintings. What specific aspect would you like to know more about?"
            }
            
            # Simple keyword matching for responses
            user_lower = user_message.lower()
            if any(word in user_lower for word in ['hi', 'hello', 'hey']):
                bot_response = mock_responses['hello']
            elif any(word in user_lower for word in ['dance', 'dancing', 'manipuri dance']):
                bot_response = mock_responses['dance']
            elif any(word in user_lower for word in ['art', 'painting', 'artwork']):
                bot_response = mock_responses['art']
            elif any(word in user_lower for word in ['culture', 'tradition', 'heritage']):
                bot_response = mock_responses['culture']
            elif any(word in user_lower for word in ['handloom', 'textile', 'fabric', 'weaving']):
                bot_response = mock_responses['handloom']
            elif any(word in user_lower for word in ['pottery', 'ceramic', 'clay']):
                bot_response = mock_responses['pottery']
            else:
                bot_response = mock_responses['default']
            
            print(f"Mock response: {bot_response}")
            return jsonify({'response': bot_response})
        
        else:
            # Original OpenAI API call
            system_prompt = """You are a knowledgeable guide for the Manipur Virtual Art Gallery. 
            Manipur is a beautiful state in Northeast India known for its rich cultural heritage, 
            traditional dances like Manipuri classical dance, handloom textiles, pottery, 
            paintings, and crafts. You should provide informative and engaging responses about 
            Manipur's art, culture, history, and traditions. Keep responses concise but informative."""
            
            print("Making OpenAI API call...")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            bot_response = response.choices[0].message.content
            print(f"OpenAI response: {bot_response}")
            return jsonify({'response': bot_response})
    
    except Exception as e:
        print(f"ERROR in chat endpoint: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Run on all interfaces in production, localhost in development
    host = '0.0.0.0' if os.environ.get('RENDER') else '127.0.0.1'
    app.run(debug=False if os.environ.get('RENDER') else True, host=host, port=port)
