# 💪 AI Workout Planner Agent

Generate personalized fitness routines based on your goals using AI! This Streamlit application uses OpenAI's GPT-4 to create customized workout plans tailored to your experience level, available equipment, and fitness objectives.

## ✨ Features

- 🎯 **Goal-Based Planning**: Build muscle, lose weight, increase strength, improve endurance, and more
- 📊 **Experience Levels**: Plans adapted for beginners, intermediate, and advanced fitness levels
- 🏋️ **Equipment Flexibility**: Works with no equipment, home gym, or full gym access
- 📅 **Customizable Schedule**: 2-7 workout days per week with adjustable session duration
- 🎯 **Target Specific Areas**: Focus on specific muscle groups or full-body training
- ⚠️ **Injury Considerations**: Accounts for limitations and previous injuries
- 📥 **Download Plans**: Save your workout plans as text files
- 📜 **History Tracking**: Keep track of all generated workout plans
- 💡 **Exercise Tips**: Get detailed form guidance for specific exercises

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Navigate to the project directory**
   ```bash
   cd ai_workout_planner_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
   
   Create a `.env` file:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file and add your API key:
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

### Step 1: Define Your Fitness Goal
Select your primary objective from the dropdown:
- Build Muscle (Hypertrophy)
- Lose Weight (Fat Loss)
- Increase Strength
- Improve Endurance
- General Fitness
- Athletic Performance
- Flexibility & Mobility
- Body Recomposition

### Step 2: Set Your Profile

- **Experience Level**: Choose from Beginner, Intermediate, or Advanced
- **Workout Days**: Select how many days per week you can train (2-7 days)
- **Session Duration**: Pick your preferred workout length (20-90 minutes)
- **Equipment**: Select all available equipment (or choose bodyweight only)
- **Target Areas**: Optionally focus on specific muscle groups
- **Limitations**: Mention any injuries or physical limitations

### Step 3: Generate Your Plan

Click the **"🔥 Generate Workout Plan"** button and receive:
- Complete weekly workout schedule
- Detailed exercise instructions
- Sets, reps, and rest periods
- Warm-up and cool-down routines
- Form tips and safety guidelines
- Progress tracking recommendations
- Nutrition tips

### Step 4: Use Your Plan

- **Download**: Save your plan as a text file
- **Exercise Tips**: Get detailed form guidance for any exercise
- **Track Progress**: Monitor your workout history

## 🎯 Example Use Cases

### Scenario 1: Beginner at Home
```
Goal: General Fitness
Level: Beginner
Days: 3 per week
Duration: 30 minutes
Equipment: No Equipment (Bodyweight)
Result: Simple bodyweight circuit training plan
```

### Scenario 2: Gym Muscle Building
```
Goal: Build Muscle
Level: Intermediate
Days: 5 per week
Duration: 60 minutes
Equipment: Full Gym Access
Result: Progressive push/pull/legs split routine
```

### Scenario 3: Weight Loss with Home Equipment
```
Goal: Lose Weight (Fat Loss)
Level: Beginner
Days: 4 per week
Duration: 45 minutes
Equipment: Dumbbells, Resistance Bands
Result: HIIT and strength training combination
```

### Scenario 4: Athletic Performance
```
Goal: Athletic Performance
Level: Advanced
Days: 6 per week
Duration: 75 minutes
Equipment: Full Gym Access
Target: Legs, Core
Result: Sport-specific power and agility training
```

## 🔧 Configuration

### Model Selection
By default, the app uses `gpt-4o-mini` for cost-effectiveness. To use GPT-4:

Open `app.py` and change line 77:
```python
model="gpt-4"  # or "gpt-4-turbo" for faster responses
```

### Temperature Adjustment
Adjust creativity by changing the temperature parameter (line 79):
```python
temperature=0.7  # Range: 0.0 (focused) to 1.0 (creative)
```

## 📁 Project Structure

```
ai_workout_planner_agent/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variable template
├── .env                  # Your API keys (create this)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🛠️ Troubleshooting

### "OpenAI API key not found" Error
- Ensure you've created a `.env` file with your API key
- Or set the `OPENAI_API_KEY` environment variable
- Restart the Streamlit app after setting the key

### Rate Limit Errors
- You may have exceeded your OpenAI API quota
- Check your usage at [OpenAI Platform](https://platform.openai.com/usage)
- Consider upgrading your plan or waiting a bit

### Slow Response Times
- GPT-4 can be slower; consider using `gpt-4o-mini` or `gpt-4-turbo`
- Check your internet connection
- OpenAI servers might be experiencing high traffic

### Workout Plan Quality Issues
- Be specific about your goals and limitations
- Provide accurate information about your experience level
- Adjust the temperature parameter for more/less creativity

## 💰 Cost Considerations

**Model Costs** (approximate, as of 2024):
- `gpt-4o-mini`: ~$0.15 per 1M input tokens, ~$0.60 per 1M output tokens
- `gpt-4-turbo`: ~$10 per 1M input tokens, ~$30 per 1M output tokens
- `gpt-4`: ~$30 per 1M input tokens, ~$60 per 1M output tokens

**Per Workout Plan** (estimated):
- Input: ~800 tokens
- Output: ~2,000 tokens
- Cost with gpt-4o-mini: ~$0.001 per plan
- Cost with gpt-4: ~$0.15 per plan

## 🎨 Customization Ideas

### Add New Features
1. **Video Demonstrations**: Link to exercise videos
2. **Workout Timer**: Built-in interval timer
3. **Progress Photos**: Upload and track transformation photos
4. **Calorie Calculator**: Estimate calories burned
5. **Meal Plans**: Integrate nutrition planning
6. **Social Sharing**: Share workouts with friends
7. **Mobile App**: Create a mobile version
8. **Workout Calendar**: Visual workout schedule

### Modify UI
- Change colors in the CSS section
- Add more metrics and visualizations
- Rearrange layout for different workflows
- Add animations and transitions

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Exercise Form Videos](https://www.youtube.com/@athleanx)
- [Nutrition Basics](https://www.nutrition.gov/)
- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

## ⚠️ Important Disclaimers

- **Consult a Professional**: Always consult with a healthcare provider before starting a new exercise program
- **Listen to Your Body**: Stop immediately if you experience pain or discomfort
- **Proper Form**: Focus on technique over weight or speed
- **Progressive Overload**: Increase intensity gradually
- **Rest and Recovery**: Allow adequate rest between workouts
- **Nutrition Matters**: Exercise alone is not enough; proper nutrition is essential

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share your workout success stories

## 📄 License

This project is open source and available under the MIT License.

## 📧 Support

If you encounter any issues:
1. Check the Troubleshooting section
2. Review OpenAI API documentation
3. Check Streamlit documentation
4. Open an issue on GitHub

---

Made with ❤️ for fitness enthusiasts and AI lovers

*Remember: The best workout is the one you actually do consistently!*
