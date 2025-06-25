<!-- ```
Assistant: 🙏 Namaste! Main aapka AI travel assistant hoon. Chaliye aapka trip plan karte hain. 😊

User: medium
Assistant: Perfect! Medium budget (₹10,000 – ₹25,000) noted.

User: beach, mountains
Assistant: Great choices! Beach aur mountains dono amazing hain.

User: 5
Assistant: 5 din ka trip - perfect duration!

User: haan
Assistant: 🧠 AI trip plan kar raha hai...

 **Destination:** Goa
 **Itinerary:**
Day 1: Arrive in Panaji, explore Miramar Beach
Day 2: North Goa - Baga Beach, Calangute Beach
Day 3: Adventure day - Water sports, Dudhsagar Falls
Day 4: South Goa - Palolem Beach, Cabo de Rama Fort
Day 5: Shopping at Anjuna Flea Market, departure

 **Weather & Attractions:**
Current weather: Sunny, 28°C
Top attractions: Basilica of Bom Jesus, Fort Aguada, Spice Plantations

 **Visuals:** [Images and hotel recommendations displayed]
```

##  Data Structure

### Destination Database
The system uses a comprehensive JSON database (`destination.json`) containing 100+ destinations with:

- **Name**: Destination name
- **Type**: Category (beach, mountain, city, history, nature, etc.)
- **Country**: Location country
- **Tags**: Descriptive keywords for matching

### Sample Data Entry
```json
{
  "name": "Goa",
  "type": "beach",
  "country": "India",
  "tags": ["beach", "relax", "nightlife", "culture"]
}
```

## 🔧 Configuration

### Agent Configuration
The main agent is configured with:
- **Model**: Llama3-70B via Groq API
- **Temperature**: 0.2 (balanced creativity/consistency)
- **Memory**: Conversation buffer memory
- **Tools**: Weather, Attractions, Images, Destination Search

### Prompt Template
Custom Hinglishprompt template ensures:
- Natural conversation flow
- Step-by-step preference collection
- Tool usage only when necessary
- Warm, professional tone

##  API Integrations

### Required APIs
1. **Groq API** - LLM inference
2. **OpenWeatherMap** - Weather data
3. **Unsplash** - Destination images
4. **Wikipedia** - Attraction information

### API Rate Limits
- Groq: 6000 requests/minute
- OpenWeatherMap: 1000 calls/day (free tier)
- Unsplash: 50 requests/hour

## 📱 User Interface

### Streamlit Features
- **Session State Management**: Maintains conversation context
- **Progressive Form Filling**: Step-by-step user input
- **Real-time Processing**: Live AI responses
- **Visual Content Display**: Images and formatted text
- **Error Handling**: Graceful error messages

### UI Components
- Chat interface with message history
- Input validation and error messaging
- Loading spinners for AI processing
- Image galleries for visual content

## 🔍 Technical Details

### Vector Search Implementation
- **Embedding Model**: all-MiniLM-L6-v2 (HuggingFace)
- **Vector Store**: FAISS for efficient similarity search
- **Chunk Size**: 300 characters with 20 character overlap
- **Search Results**: Top 10 similar destinations

### Memory Management
- **Conversation Memory**: Stores full chat history
- **Session State**: Preserves user preferences
- **Tool Memory**: Caches API responses where possible

### Error Handling
- API timeout handling
- Invalid input validation
- Graceful fallbacks for failed API calls
- User-friendly error messages

##  Deployment

### Local Development
```bash
streamlit run app.py
```

### Production Deployment Options
1. **Streamlit Cloud**: Direct GitHub integration
2. **Heroku**: Container-based deployment
3. **AWS/GCP**: Cloud platform deployment
4. **Docker**: Containerized deployment

### Environment Variables
Ensure all API keys are properly configured in production environment.

##  Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Authors

- **Your Name** - Initial work and development

##  Acknowledgments

- LangChain community for excellent documentation
- Streamlit team for the intuitive UI framework
- Groq for fast LLM inference
- OpenWeatherMap, Unsplash, and Wikipedia for API services

##  Support

For support, email your-email@domain.com or create an issue in the GitHub repository.

---

**Happy Traveling! 🧳✈️**```
Assistant:  Namaste! Main aapka AI travel assistant hoon. Chaliye aapka trip plan karte hain. 

User: medium#  Travel Chat Assistant

## Overview
**Travel Chat Assistant** is an AI-powered travel planning application that helps users plan perfect short trips anywhere in the world. The system uses a conversational approach with Hinglish (Hindi-English mix) to make travel planning more engaging and natural for Indian users.

##  Features

### Core Functionality
- **Interactive Trip Planning**: Step-by-step conversation to understand user preferences
- **Smart Destination Suggestions**: AI-powered recommendations based on budget, interests, and duration
- **Weather Information**: Real-time weather data for destinations
- **Attraction Discovery**: Dynamic fetching of top tourist attractions
- **Visual Content**: Destination images and hotel previews
- **Multi-language Support**: Natural Hinglish conversation flow

### Technical Features
- **LangChain Integration**: Advanced AI agent with memory and tool usage
- **Vector Search**: FAISS-based semantic search for destinations
- **Graph Workflow**: LangGraph for structured conversation flow
- **API Integrations**: Weather, Images, and Wikipedia data
- **Streamlit UI**: Interactive web interface

##  Architecture

### Core Components

1. **Agent System** (`agent_config.py`)
   - Main AI agent with conversational memory
   - Tool integration for weather, attractions, and images
   - Custom prompt template for Hinglish responses

2. **Workflow Management** (`graph.py`)
   - LangGraph-based state management
   - Sequential workflow: Input → Suggest → Itinerary → Support → Visuals

3. **Streamlit App** (`app.py`)
   - Interactive web interface
   - Step-by-step user preference collection
   - Real-time AI response display

4. **RAG System** (`rag.py`)
   - Vector store creation and management
   - FAISS integration with HuggingFace embeddings
   - Semantic search for destinations

### Tools & APIs

1. **Weather Tool** (`weather.py`)
   - OpenWeatherMap API integration
   - Real-time weather data

2. **Attractions Tool** (`attraction.py`)
   - Wikipedia API integration
   - Dynamic attraction discovery

3. **Image Tool** (`place.py`)
   - Unsplash API integration
   - Destination and hotel image fetching

4. **Destination Search** (`rag.py`)
   - Vector-based destination matching
   - JSON data processing

##  Installation

### Prerequisites
- Python 3.8+
- API Keys for:
  - Groq (LLM)
  - OpenWeatherMap
  - Unsplash

### Setup Steps

1. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd travel-chat-assistant
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   Create `.env` file with:
   ```env
   GROQ_API_KEY=your_groq_api_key
   OPENWEATHER_API_KEY=your_openweather_api_key
   UNSPLASH_ACCESS_KEY=your_unsplash_access_key
   ```

4. **Initialize Vector Store**
   ```python
   from rag import create_vector_store
   create_vector_store()
   ```

5. **Run Application**
   ```bash
   streamlit run app.py
   ```

##  Usage

### Web Interface Flow

1. **Greeting**: System welcomes user in Hinglish
2. **Budget Selection**: User chooses from Low/Medium/High budget
3. **Interest Collection**: User specifies travel interests (beach, mountains, etc.)
4. **Duration Input**: Number of days for the trip
5. **Plan Generation**: AI creates comprehensive travel plan
6. **Results Display**: 
   - Destination suggestion
   - Day-wise itinerary
   - Weather information
   - Top attractions
   - Visual content (images + hotels)
 -->
# 🧳 AI Travel Assistant 🌍

An intelligent travel planner built with LangChain, Groq LLaMA 3, and Streamlit.

---

## 🚀 Features

- Chat-based travel Q&A
- Step-by-step guided itinerary planner
- Supports destinations across the world
- Tools: Weather, Attractions, Destination Search

---

## 🛠️ Tech Stack

- LangChain
- Groq (LLaMA 3)
- Streamlit
- Open APIs (RapidAPI, etc.)

---

## 🔧 Setup Instructions

1. Clone the repo  
   `git clone https://github.com/your-username/travel-assistant-ai.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Create `.env` file with keys:
```env
GROQ_API_KEY=your_groq_key
RAPIDAPI_KEY=your_rapidapi_key
