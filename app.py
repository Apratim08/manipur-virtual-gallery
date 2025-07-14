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
            # Enhanced mock responses about Manipur's art and culture
            mock_responses = {
                'dance': "Manipuri dance is one of India's eight classical forms, deeply rooted in Bhakti traditions. Key forms include Rasa Lila (celebrating Krishna and Radha, performed on full moon nights), Thang-Ta (martial dance with sword and spear), Pung Cholom (drum dancing with acrobatics), and Kartal Cholom (cymbal dance in Sankirtana). Renowned artists include Guru Bipin Singh, Darshana Jhaveri, and Rajkumar Singhajit Singh.",
                'art': "Manipur's art encompasses vibrant mythological paintings that preserve ancient oral traditions, intricate handloom textiles reflecting tribal and Vaishnavite heritage, and handicrafts supported by cultural preservation efforts. These living traditions are showcased in cultural museums and heritage villages.",
                'culture': "Manipuri culture beautifully blends tribal and Vaishnavite traditions, expressed through devotional arts performed during festivals like Lai Haraoba, Janmashtami, and Rath Yatra. The culture emphasizes spiritual devotion (bhakti rasa) and community preservation of ancient oral traditions.",
                'handloom': "Manipuri handloom textiles showcase generations of skilled craftsmanship, reflecting the cultural heritage passed down through tribal and Vaishnavite traditions. These textiles feature intricate designs that tell stories of devotion and community identity.",
                'pottery': "Manipuri pottery is unique - crafted without potter's wheels using paddle and anvil techniques. Famous villages include Andro (terracotta figures, ritual pots), Thongjao (red pottery), Sekmai (fermentation pots for rice beer), and Chairel (earthenware). Women from Purum and Tangkhul Naga tribes play central roles. Clay is mixed with powdered stone or serpentine stone for heat resistance, creating vessels for festivals like Lai Haraoba.",
                'villages': "Famous pottery villages: Andro specializes in terracotta figures and ritual pots, Thongjao creates red pottery for homes, Sekmai makes fermentation pots for local rice beer, and Chairel produces earthenware and cooking pots. These villages preserve ancient hand-crafting techniques without modern potter's wheels.",
                'hello': "Hello! Welcome to the Manipur Virtual Art Gallery. I'm here to help you explore the rich heritage of the 'Jewel of India' - from the devotional Rasa Lila dances to the ancient pottery villages of Andro and Thongjao. What would you like to discover?",
                'default': "Thank you for your interest in Manipur's heritage! Manipur, the 'Jewel of India,' preserves ancient traditions through its pottery villages (Andro, Thongjao, Sekmai, Chairel), devotional dance forms like Rasa Lila, handloom textiles, and mythological paintings. What specific aspect would you like to explore - pottery techniques, dance forms, or cultural festivals?"
            }
            
            # Simple keyword matching for responses
            user_lower = user_message.lower()
            if any(word in user_lower for word in ['hi', 'hello', 'hey']):
                bot_response = mock_responses['hello']
            elif any(word in user_lower for word in ['dance', 'dancing', 'manipuri dance', 'rasa lila', 'thang-ta', 'pung cholom']):
                bot_response = mock_responses['dance']
            elif any(word in user_lower for word in ['art', 'painting', 'artwork']):
                bot_response = mock_responses['art']
            elif any(word in user_lower for word in ['culture', 'tradition', 'heritage', 'bhakti', 'vaishnavite']):
                bot_response = mock_responses['culture']
            elif any(word in user_lower for word in ['handloom', 'textile', 'fabric', 'weaving']):
                bot_response = mock_responses['handloom']
            elif any(word in user_lower for word in ['pottery', 'ceramic', 'clay', 'andro', 'thongjao', 'sekmai', 'chairel']):
                bot_response = mock_responses['pottery']
            elif any(word in user_lower for word in ['village', 'villages', 'community', 'artisan']):
                bot_response = mock_responses['villages']
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
