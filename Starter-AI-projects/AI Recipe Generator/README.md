# 👨‍🍳 AI Recipe Generator Agent

Create personalized recipes based on your available ingredients using AI! This Streamlit application uses OpenAI's GPT-4 to generate customized recipes that match your dietary restrictions, cuisine preferences, skill level, and time constraints.

## ✨ Features

- 🥘 **Personalized Recipes**: Generate recipes based on YOUR available ingredients
- 🥗 **Dietary Restrictions**: Support for vegetarian, vegan, gluten-free, keto, and more
- 🌍 **Cuisine Preferences**: Choose from 14+ cuisine styles
- 👨‍🍳 **Skill Level Adaptation**: Recipes adapted to your cooking experience
- ⏱️ **Time Management**: Set maximum cooking time
- 💡 **Quick Ideas**: Get instant recipe suggestions
- 📖 **Recipe History**: Keep track of previously generated recipes
- 📥 **Download Recipes**: Save recipes as text files

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone or download this project**
   ```bash
   cd ai_recipe_generator_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
   
   Create a `.env` file in the project directory:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```
   
   **Alternative**: Set environment variable directly
   ```bash
   # On Linux/Mac
   export OPENAI_API_KEY='your_actual_api_key_here'
   
   # On Windows (Command Prompt)
   set OPENAI_API_KEY=your_actual_api_key_here
   
   # On Windows (PowerShell)
   $env:OPENAI_API_KEY='your_actual_api_key_here'
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

## 📖 How to Use

### Step 1: Enter Your Ingredients
In the sidebar, list all available ingredients (comma-separated):
```
chicken breast, tomatoes, onions, garlic, olive oil, basil
```

### Step 2: Set Your Preferences

- **Dietary Restrictions**: Select any dietary needs (vegetarian, vegan, gluten-free, etc.)
- **Cuisine Preference**: Choose a cuisine style (Italian, Mexican, Chinese, etc.) or leave as "Any"
- **Skill Level**: Select from Beginner to Professional
- **Cooking Time**: Set maximum time you want to spend (15-180 minutes)

### Step 3: Generate Your Recipe

Click the **"🔥 Generate Recipe"** button and watch as AI creates a personalized recipe just for you!

### Step 4: Explore Features

- **💡 Quick Ideas**: Click to get 5 quick recipe suggestions
- **📖 Recipe History**: View previously generated recipes
- **📥 Download**: Save your favorite recipes as text files

## 🎯 Example Use Cases

### Scenario 1: Quick Weeknight Dinner
```
Ingredients: pasta, ground beef, tomato sauce, cheese
Restrictions: None
Cuisine: Italian
Skill: Beginner
Time: 30 minutes
Result: Simple Bolognese Pasta
```

### Scenario 2: Healthy Meal Prep
```
Ingredients: chicken breast, quinoa, broccoli, bell peppers
Restrictions: Gluten-Free, Low-Carb
Cuisine: Mediterranean
Skill: Intermediate
Time: 45 minutes
Result: Mediterranean Chicken Bowl
```

### Scenario 3: Vegan Dinner Party
```
Ingredients: chickpeas, coconut milk, spinach, curry spices
Restrictions: Vegan, Gluten-Free
Cuisine: Indian
Skill: Advanced
Time: 60 minutes
Result: Creamy Chickpea Curry
```

## 🔧 Configuration

### Model Selection
By default, the app uses `gpt-4o-mini` for cost-effectiveness. To use GPT-4:

Open `app.py` and change line 61:
```python
model="gpt-4"  # or "gpt-4-turbo" for faster responses
```

### Temperature Adjustment
Adjust creativity by changing the temperature parameter (line 63):
```python
temperature=0.8  # Range: 0.0 (focused) to 1.0 (creative)
```

## 📁 Project Structure

```
ai_recipe_generator_agent/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variable template
├── .env                  # Your API keys (create this)
└── README.md             # This file
```

## 🛠️ Troubleshooting

### "OpenAI API key not found" Error
- Make sure you've created a `.env` file with your API key
- Or set the `OPENAI_API_KEY` environment variable
- Restart the Streamlit app after setting the key

### Rate Limit Errors
- You may have exceeded your OpenAI API quota
- Check your usage at [OpenAI Platform](https://platform.openai.com/usage)
- Consider upgrading your plan or adding credits

### Slow Response Times
- GPT-4 can be slower; consider using `gpt-4o-mini` or `gpt-4-turbo`
- Check your internet connection
- OpenAI servers might be experiencing high traffic

### Recipe Quality Issues
- Provide more specific ingredients
- Be clearer about dietary restrictions
- Adjust the temperature parameter for more/less creativity

## 💰 Cost Considerations

**Model Costs** (approximate, as of 2024):
- `gpt-4o-mini`: ~$0.15 per 1M input tokens, ~$0.60 per 1M output tokens
- `gpt-4-turbo`: ~$10 per 1M input tokens, ~$30 per 1M output tokens
- `gpt-4`: ~$30 per 1M input tokens, ~$60 per 1M output tokens

**Per Recipe** (estimated):
- Input: ~500 tokens
- Output: ~1,000 tokens
- Cost with gpt-4o-mini: ~$0.001 per recipe
- Cost with gpt-4: ~$0.08 per recipe

## 🎨 Customization Ideas

### Add New Features
1. **Nutrition Calculator**: Integrate with nutrition APIs
2. **Shopping List Generator**: Create grocery lists from recipes
3. **Recipe Scaling**: Adjust servings automatically
4. **Meal Planning**: Generate weekly meal plans
5. **Image Generation**: Add AI-generated food images
6. **Voice Input**: Use speech-to-text for ingredients
7. **Recipe Rating**: Allow users to rate recipes
8. **Social Sharing**: Share recipes on social media

### Modify UI
- Change color scheme in `st.set_page_config()`
- Add custom CSS with `st.markdown()`
- Rearrange sidebar elements
- Add more visualization with charts

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share your custom recipes

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Inspired by [Shubham Saboo's Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI GPT-4](https://openai.com/)

## 📧 Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Review OpenAI API documentation
3. Check Streamlit documentation
4. Open an issue on GitHub

---

**Happy Cooking! 👨‍🍳✨**

Made with ❤️ for food lovers and AI enthusiasts
