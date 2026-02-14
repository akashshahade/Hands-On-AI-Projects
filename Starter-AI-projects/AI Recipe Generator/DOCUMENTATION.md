# AI Recipe Generator Agent - Project Documentation

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [File Structure](#file-structure)
5. [Setup Instructions](#setup-instructions)
6. [Usage Guide](#usage-guide)
7. [API Reference](#api-reference)
8. [Customization](#customization)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)

---

## 🎯 Project Overview

The AI Recipe Generator Agent is an intelligent cooking assistant that creates personalized recipes based on available ingredients, dietary restrictions, and cooking preferences. Built with Streamlit and powered by OpenAI's GPT-4, it provides an intuitive interface for home cooks of all skill levels.

### Key Technologies
- **Frontend:** Streamlit
- **AI Model:** OpenAI GPT-4 / GPT-4o-mini
- **Language:** Python 3.8+
- **Deployment:** Can run locally or on cloud platforms

---

## ✨ Features

### Basic Version (app.py)
- ✅ Generate personalized recipes from ingredients
- ✅ Support for 10+ dietary restrictions
- ✅ 14+ cuisine styles
- ✅ Skill level adaptation (Beginner to Professional)
- ✅ Time-based recipe filtering
- ✅ Quick recipe idea suggestions
- ✅ Recipe history tracking
- ✅ Download recipes as text files

### Advanced Version (app_advanced.py)
- ✅ All basic features plus:
- ✅ Nutritional information
- ✅ Multiple meal types (breakfast, lunch, dinner, etc.)
- ✅ Servings adjustment
- ✅ Weekly meal planner
- ✅ Favorites system
- ✅ Virtual pantry management
- ✅ Smart shopping list generation
- ✅ Wine/beverage pairing suggestions
- ✅ Recipe variations and substitutions
- ✅ Enhanced UI with custom styling

---

## 🏗️ Architecture

### System Components

```
┌─────────────┐
│   User UI   │
│ (Streamlit) │
└──────┬──────┘
       │
       ↓
┌──────────────┐
│  Application │
│    Logic     │
└──────┬───────┘
       │
       ↓
┌──────────────┐
│  OpenAI API  │
│   (GPT-4)    │
└──────────────┘
```

### Data Flow

1. **User Input** → User enters ingredients and preferences
2. **Processing** → Application formats prompt for AI
3. **AI Generation** → OpenAI generates recipe
4. **Display** → Recipe rendered in Streamlit UI
5. **Storage** → Recipe saved in session state

### Session State Management

```python
st.session_state.messages        # Recipe history
st.session_state.generated_recipe # Current recipe
st.session_state.favorites        # Saved favorites (advanced)
st.session_state.ingredient_pantry # Pantry items (advanced)
```

---

## 📁 File Structure

```
ai_recipe_generator_agent/
│
├── app.py                 # Main application (basic version)
├── app_advanced.py        # Advanced version with extra features
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your API keys (create this)
├── .gitignore           # Git ignore rules
├── README.md            # User documentation
├── DOCUMENTATION.md     # This file (technical docs)
├── setup.sh            # Linux/Mac setup script
├── setup.bat           # Windows setup script
│
└── (future additions)
    ├── tests/          # Unit tests
    ├── assets/         # Images, icons
    └── data/           # Sample data, templates
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key

### Quick Setup

#### Option 1: Automated Setup (Recommended)

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows:**
```cmd
setup.bat
```

#### Option 2: Manual Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Configure environment:**
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

3. **Run the application:**
```bash
streamlit run app.py
```

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 📖 Usage Guide

### Basic Workflow

1. **Launch the app:**
   ```bash
   streamlit run app.py
   ```

2. **Enter ingredients:**
   - Type in sidebar: "chicken, rice, tomatoes, onions"

3. **Set preferences:**
   - Dietary: Gluten-Free
   - Cuisine: Italian
   - Skill: Intermediate
   - Time: 45 minutes

4. **Generate recipe:**
   - Click "Generate Recipe" button

5. **View and save:**
   - Read recipe
   - Download if desired
   - Recipe auto-saved to history

### Advanced Features (app_advanced.py)

#### Using the Meal Planner
1. Navigate to "Meal Planner" tab
2. Enter all available ingredients
3. Select number of days (1-7)
4. Choose dietary restrictions
5. Click "Generate Meal Plan"

#### Managing Favorites
1. Generate a recipe you like
2. Click "Add to Favorites"
3. Access favorites in "Favorites" tab
4. Download or remove as needed

#### Virtual Pantry
1. Go to "Pantry" tab
2. Add ingredients you always have
3. Use for quick recipe generation
4. Reduces shopping list items

---

## 🔌 API Reference

### Key Functions

#### `generate_recipe()`
Generates a personalized recipe based on inputs.

**Parameters:**
- `ingredients` (str): Comma-separated ingredient list
- `dietary_restrictions` (str): Dietary constraints
- `cuisine_preference` (str): Desired cuisine style
- `skill_level` (str): User's cooking skill
- `cooking_time` (int): Maximum cooking time in minutes

**Returns:**
- `str`: Formatted recipe text

**Example:**
```python
recipe = generate_recipe(
    ingredients="chicken, rice, vegetables",
    dietary_restrictions="Gluten-Free",
    cuisine_preference="Asian",
    skill_level="Intermediate",
    cooking_time=45
)
```

#### `get_recipe_suggestions()`
Gets quick recipe ideas from ingredients.

**Parameters:**
- `ingredients` (str): Available ingredients

**Returns:**
- `list`: List of recipe name suggestions

#### `generate_meal_plan()` (Advanced)
Creates multi-day meal plan.

**Parameters:**
- `ingredients` (str): All available ingredients
- `days` (int): Number of days (1-7)
- `dietary_restrictions` (str): Dietary needs

**Returns:**
- `str`: Formatted meal plan

#### `generate_shopping_list()` (Advanced)
Creates shopping list from recipe.

**Parameters:**
- `recipe_text` (str): Full recipe text
- `pantry_items` (list): Items already in pantry

**Returns:**
- `str`: Shopping list excluding pantry items

---

## 🎨 Customization

### Changing AI Model

Edit the model parameter in function calls:

```python
# In app.py or app_advanced.py
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Change this
    # Options: "gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-4-turbo"
    ...
)
```

### Adjusting Creativity

Modify the temperature parameter:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.8,  # Range: 0.0 (focused) to 1.0 (creative)
    ...
)
```

### Custom Styling

Add custom CSS in the `st.markdown()` section:

```python
st.markdown("""
<style>
    .recipe-card {
        background-color: #your-color;
        /* Your custom styles */
    }
</style>
""", unsafe_allow_html=True)
```

### Adding New Cuisines

Edit the cuisine list in the selectbox:

```python
cuisine_preference = st.selectbox(
    "Choose a cuisine style",
    ["Any", "Italian", "Mexican", 
     "Your New Cuisine",  # Add here
     ...]
)
```

### Modifying Prompts

Edit system and user prompts for different recipe styles:

```python
system_prompt = """Your custom chef personality and instructions"""
user_prompt = f"""Your custom recipe requirements"""
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. "OpenAI API key not found"

**Solution:**
```bash
# Check .env file exists
ls -la .env

# Verify key is set
cat .env

# Or set environment variable directly
export OPENAI_API_KEY='your-key-here'
```

#### 2. Rate Limit Errors

**Cause:** Exceeded API quota or requests per minute

**Solutions:**
- Wait a few minutes
- Check usage at platform.openai.com/usage
- Upgrade API plan
- Add rate limiting in code

#### 3. Slow Response Times

**Causes & Solutions:**
- Model is slow → Switch to faster model (gpt-4o-mini)
- Poor internet → Check connection
- High API traffic → Try again later

#### 4. Installation Fails

**Solution:**
```bash
# Upgrade pip
pip install --upgrade pip

# Install dependencies one by one
pip install streamlit
pip install openai
pip install python-dotenv
```

#### 5. Streamlit Not Found

**Solution:**
```bash
# Ensure it's installed
pip install streamlit

# Check Python PATH
which python
which streamlit

# Try with python -m
python -m streamlit run app.py
```

### Debug Mode

Enable debug output:

```python
# Add at top of app.py
import logging
logging.basicConfig(level=logging.DEBUG)

# Check API responses
print(response.choices[0].message.content)
```

---

## 🧪 Testing

### Manual Testing Checklist

- [ ] App launches without errors
- [ ] Ingredients input accepts text
- [ ] All dietary options work
- [ ] Recipe generates successfully
- [ ] Download button works
- [ ] History displays correctly
- [ ] Advanced features work (if using app_advanced.py)

### Unit Tests (Future)

```python
# tests/test_recipe_generator.py
def test_generate_recipe():
    recipe = generate_recipe(
        ingredients="chicken, rice",
        dietary_restrictions="None",
        cuisine_preference="Any",
        skill_level="Beginner",
        cooking_time=30
    )
    assert recipe is not None
    assert len(recipe) > 0
```

---

## 📈 Performance Optimization

### Token Usage Optimization

```python
# Use shorter prompts
# Cache repeated API calls
@st.cache_data(ttl=3600)
def cached_generate_recipe(...):
    return generate_recipe(...)
```

### Response Time Improvement

```python
# Use streaming responses
response = client.chat.completions.create(
    model="gpt-4o-mini",
    stream=True,
    ...
)

for chunk in response:
    # Display progressively
    st.write(chunk.choices[0].delta.content)
```

---

## 🚀 Deployment

### Streamlit Cloud

1. Push to GitHub
2. Connect at share.streamlit.io
3. Add secrets in dashboard
4. Deploy

### Docker Deployment

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

### Heroku Deployment

Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT
```

---

## 🤝 Contributing

### How to Contribute

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

### Code Style

- Follow PEP 8
- Add docstrings
- Comment complex logic
- Use type hints

```python
def generate_recipe(
    ingredients: str,
    dietary_restrictions: str,
    cuisine_preference: str,
    skill_level: str,
    cooking_time: int
) -> str:
    """
    Generate a personalized recipe.
    
    Args:
        ingredients: Comma-separated ingredient list
        dietary_restrictions: Dietary constraints
        cuisine_preference: Desired cuisine style
        skill_level: User's cooking skill
        cooking_time: Maximum time in minutes
    
    Returns:
        Formatted recipe text
    """
    ...
```

---

## 📝 License

MIT License - Feel free to use and modify for your projects.

---

## 📞 Support

- **Issues:** Open GitHub issue
- **Questions:** Check documentation
- **Updates:** Watch repository for changes

---

## 🗺️ Roadmap

### Version 1.1 (Current)
- ✅ Basic recipe generation
- ✅ Dietary restrictions
- ✅ Multiple cuisines

### Version 2.0 (app_advanced.py)
- ✅ Nutritional information
- ✅ Meal planning
- ✅ Favorites system
- ✅ Virtual pantry

### Version 3.0 (Planned)
- ⏳ Image generation for recipes
- ⏳ Voice input for ingredients
- ⏳ Recipe scaling calculator
- ⏳ Ingredient substitution suggestions
- ⏳ Community recipe sharing
- ⏳ Multi-language support
- ⏳ Mobile app version

---

**Last Updated:** February 2026  
**Version:** 2.0  
**Maintainer:** Awesome LLM Apps Community
