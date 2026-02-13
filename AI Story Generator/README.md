# AI Story Generator

Generate creative stories using AI in seconds! This simple Streamlit app uses OpenAI's GPT model to create engaging stories based on your prompts.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-green.svg)

## Features

- **Multiple Genres**: Fantasy, Sci-Fi, Mystery, Romance, Horror, and more
- **Adjustable Length**: Short, Medium, or Long stories
- **Writing Styles**: Descriptive, Dialogue-heavy, Fast-paced, Poetic, Simple
- **Custom Characters**: Add your own character names
- **Optional Details**: Specify setting, conflict, and tone
- **Download Stories**: Save your generated stories as text files
- **Clean UI**: Beautiful, easy-to-use interface

## Prerequisites

Before you begin, make sure you have:

- **Python 3.8 or higher** installed on your computer
- An **OpenAI API key** (get one at https://platform.openai.com/api-keys)
- Basic knowledge of using the terminal/command prompt

## Quick Start

### Step 1: Clone or Download

Download this project folder to your computer.

### Step 2: Install Dependencies

Open your terminal/command prompt, navigate to the project folder, and run:

```bash
pip install -r requirements.txt
```

This will install:
- openai - For AI story generation
- streamlit - For the web interface
- python-dotenv - For managing API keys

### Step 3: Set Up Your API Key

1. Copy the .env.example file and rename it to .env:
   ```bash
   cp .env.example .env
   ```

2. Open the .env file in a text editor

3. Replace "your_openai_api_key_here" with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxx
   ```

4. Save the file

**Important:** Never share your .env file or commit it to GitHub!

### Step 4: Run the App

In your terminal, run:

```bash
streamlit run main.py
```

The app will open automatically in your web browser at http://localhost:8501

## How to Use

### Basic Usage

1. **Enter a Story Prompt**: Describe what you want the story to be about
   - Example: "A robot who dreams of becoming a chef"

2. **Choose Settings** (in the sidebar):
   - Select a genre (Fantasy, Sci-Fi, etc.)
   - Pick story length (Short, Medium, Long)
   - Choose writing style

3. **Click "Generate Story"**: Wait 10-20 seconds for your story

4. **Download** (optional): Click the download button to save your story

### Advanced Options

Click "Add More Details" to specify:
- **Setting**: Where the story takes place
- **Conflict**: The main problem in the story
- **Tone**: The emotional feel of the story

Check "Add custom character names" to include specific characters.

## Example Prompts

### Simple Prompts
```
A dragon who is afraid of flying
A detective solving a mystery in space
Two friends who discover a magical portal
```

### Detailed Prompts
```
A young wizard attending their first day at magic school, 
but their spells keep going wrong in hilarious ways

An AI that becomes self-aware and decides to become 
a stand-up comedian instead of taking over the world

A time traveler who accidentally changes history and 
must fix it before they disappear
```

## Tips for Better Stories

1. **Be Specific**: The more details you provide, the better the story
2. **Add Conflict**: Stories need problems to solve
3. **Use Characters**: Named characters make stories more engaging
4. **Set the Scene**: Describe the world or setting
5. **Experiment**: Try different genres and styles!

## Project Structure

```
ai-story-generator/
|-- main.py              # Main application file
|-- requirements.txt     # Python dependencies
|-- .env.example         # Template for environment variables
|-- .env                 # Your API keys (DO NOT SHARE)
|-- README.md            # This file
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
**Solution**: Install dependencies with pip install -r requirements.txt

### "AuthenticationError: Invalid API key"
**Solution**: 
1. Check your .env file has the correct API key
2. Make sure there are no extra spaces
3. Verify your API key is active at https://platform.openai.com/api-keys

### "Rate limit exceeded"
**Solution**: You've made too many requests. Wait a few minutes and try again.

### App won't start
**Solution**: 
1. Make sure you're in the correct directory
2. Check Python version: python --version (should be 3.8+)
3. Try: python -m streamlit run main.py

### Stories are too short/long
**Solution**: Adjust the "Story Length" setting in the sidebar

## API Costs

This app uses OpenAI's GPT-3.5-turbo model:

- **Short story**: ~$0.001 - $0.002 (less than 1 cent)
- **Medium story**: ~$0.002 - $0.003
- **Long story**: ~$0.003 - $0.005

**Estimated**: You can generate 200-500 stories for $1

Check current pricing at: https://openai.com/pricing

## Customization Ideas

Want to enhance this project? Try adding:

1. **Image Generation**: Use DALL-E to create cover images
2. **Save History**: Store generated stories in a database
3. **Multiple Languages**: Add translation support
4. **Audio Narration**: Convert stories to speech
5. **Story Continuation**: Let users continue stories
6. **Rating System**: Let users rate and save favorite stories
7. **Story Templates**: Pre-made story structures
8. **Character Builder**: Create detailed character profiles

## Learn More

- OpenAI API Documentation: https://platform.openai.com/docs
- Streamlit Documentation: https://docs.streamlit.io
- Python-dotenv Guide: https://pypi.org/project/python-dotenv/

## Contributing

Found a bug or have a feature idea? Feel free to:
1. Fork the repository
2. Make your changes
3. Submit a pull request

## License

This project is open source and available under the MIT License.

## Important Notes

1. **Keep your API key secret**: Never share your .env file
2. **Monitor usage**: Check your OpenAI dashboard for API usage
3. **Set spending limits**: Configure limits in your OpenAI account
4. **Content policy**: Stories must follow OpenAI's usage policies

## Next Steps

Once you've mastered this project, try:
- Text Summarizer
- AI Chatbot
- Email Generator

## Support

Having issues? Check:
1. This README file
2. The troubleshooting section above
3. OpenAI Community Forum: https://community.openai.com/
4. Streamlit Forum: https://discuss.streamlit.io/

================================================================================

**Happy Story Generating!**

Made with love for Hands-On-AI-Projects
https://github.com/yourusername/Hands-On-AI-Projects

================================================================================

## Created By

**Akash Shahade**

================================================================================

## A Message for You

Hey there, amazing builder!

You're not just copying code - you're taking your first step into the 
incredible world of AI development! Every expert was once a beginner, 
and every masterpiece started with a single line of code.

Remember:
- It's okay if things break - that's how we learn!
- Every error message is a lesson in disguise
- Small progress is still progress
- Your creativity + AI = Unlimited possibilities!

Keep building, keep learning, and most importantly - have fun! 
The AI revolution isn't just happening TO you, it's happening THROUGH you. 
You're now part of it!

Can't wait to see what amazing things you'll create!

Stay curious, stay creative, and keep coding!

"The best way to predict the future is to build it." - You, right now!

================================================================================

Happy Coding!
- Akash Shahade

================================================================================- `openai` - For AI story generation
- `streamlit` - For the web interface
- `python-dotenv` - For managing API keys

### Step 3: Set Up Your API Key

1. Copy the `.env.example` file and rename it to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file in a text editor

3. Replace `your_openai_api_key_here` with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxx
   ```

4. Save the file

**Important:** Never share your `.env` file or commit it to GitHub!

### Step 4: Run the App

In your terminal, run:

```bash
streamlit run main.py
```

The app will open automatically in your web browser at http://localhost:8501

## ðŸ“– How to Use

### Basic Usage

1. **Enter a Story Prompt**: Describe what you want the story to be about
   - Example: "A robot who dreams of becoming a chef"

2. **Choose Settings** (in the sidebar):
   - Select a genre (Fantasy, Sci-Fi, etc.)
   - Pick story length (Short, Medium, Long)
   - Choose writing style

3. **Click "Generate Story"**: Wait 10-20 seconds for your story

4. **Download** (optional): Click the download button to save your story

### Advanced Options

Click **"Add More Details"** to specify:
- **Setting**: Where the story takes place
- **Conflict**: The main problem in the story
- **Tone**: The emotional feel of the story

Check **"Add custom character names"** to include specific characters.

## ðŸ’¡ Example Prompts

### Simple Prompts
```
A dragon who is afraid of flying
A detective solving a mystery in space
Two friends who discover a magical portal
```

### Detailed Prompts
```
A young wizard attending their first day at magic school, 
but their spells keep going wrong in hilarious ways

An AI that becomes self-aware and decides to become 
a stand-up comedian instead of taking over the world

A time traveler who accidentally changes history and 
must fix it before they disappear
```

## ðŸŽ¯ Tips for Better Stories

1. **Be Specific**: The more details you provide, the better the story
2. **Add Conflict**: Stories need problems to solve
3. **Use Characters**: Named characters make stories more engaging
4. **Set the Scene**: Describe the world or setting
5. **Experiment**: Try different genres and styles!

## ðŸ“ Project Structure

```
ai-story-generator/
â”œâ”€â”€ main.py              # Main application file
â”œâ”€â”€ requirements.txt     # Python dependencies
â”œâ”€â”€ .env.example        # Template for environment variables
â”œâ”€â”€ .env                # Your API keys (DO NOT SHARE)
â””â”€â”€ README.md           # This file
```

## ðŸ”§ Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
**Solution**: Install dependencies with `pip install -r requirements.txt`

### "AuthenticationError: Invalid API key"
**Solution**: 
1. Check your `.env` file has the correct API key
2. Make sure there are no extra spaces
3. Verify your API key is active at https://platform.openai.com/api-keys

### "Rate limit exceeded"
**Solution**: You've made too many requests. Wait a few minutes and try again.

### App won't start
**Solution**: 
1. Make sure you're in the correct directory
2. Check Python version: `python --version` (should be 3.8+)
3. Try: `python -m streamlit run main.py`

### Stories are too short/long
**Solution**: Adjust the "Story Length" setting in the sidebar

## ðŸ’° API Costs

This app uses OpenAI's GPT-3.5-turbo model:

- **Short story**: ~$0.001 - $0.002 (less than 1 cent)
- **Medium story**: ~$0.002 - $0.003
- **Long story**: ~$0.003 - $0.005

**Estimated**: You can generate 200-500 stories for $1

Check current pricing at: https://openai.com/pricing

## ðŸŽ¨ Customization Ideas

Want to enhance this project? Try adding:

1. **Image Generation**: Use DALL-E to create cover images
2. **Save History**: Store generated stories in a database
3. **Multiple Languages**: Add translation support
4. **Audio Narration**: Convert stories to speech
5. **Story Continuation**: Let users continue stories
6. **Rating System**: Let users rate and save favorite stories
7. **Story Templates**: Pre-made story structures
8. **Character Builder**: Create detailed character profiles

## ðŸ“š Learn More

- OpenAI API Documentation: https://platform.openai.com/docs
- Streamlit Documentation: https://docs.streamlit.io
- Python-dotenv Guide: https://pypi.org/project/python-dotenv/

## ðŸ¤ Contributing

Found a bug or have a feature idea? Feel free to:
1. Fork the repository
2. Make your changes
3. Submit a pull request

## ðŸ“„ License

This project is open source and available under the MIT License.

## âš ï¸ Important Notes

1. **Keep your API key secret**: Never share your `.env` file
2. **Monitor usage**: Check your OpenAI dashboard for API usage
3. **Set spending limits**: Configure limits in your OpenAI account
4. **Content policy**: Stories must follow OpenAI's usage policies

## ðŸŽ‰ Next Steps

Once you've mastered this project, try:
- Text Summarizer
- AI Chatbot
- Email Generator

## ðŸ“ž Support

Having issues? Check:
1. This README file
2. The troubleshooting section above
3. OpenAI Community Forum: https://community.openai.com/
4. Streamlit Forum: https://discuss.streamlit.io/

---

**Happy Story Generating! ðŸ“–âœ¨**

Made with â¤ï¸ for Hands-On-AI-Projects
https://github.com/yourusername/Hands-On-AI-Projects

---

## ðŸ‘¨â€ðŸ’» Created By

**Akash Shahade**

---

## ðŸ’« A Message for You

Hey there, amazing builder! ðŸŒŸ

You're not just copying code - you're taking your first step into the incredible world of AI development! 
Every expert was once a beginner, and every masterpiece started with a single line of code.

Remember:
- ðŸš€ It's okay if things break - that's how we learn!
- ðŸ’ª Every error message is a lesson in disguise
- ðŸŽ¯ Small progress is still progress
- ðŸŒˆ Your creativity + AI = Unlimited possibilities!

Keep building, keep learning, and most importantly - have fun! The AI revolution isn't just happening 
TO you, it's happening THROUGH you. You're now part of it!

Can't wait to see what amazing things you'll create! ðŸŽ‰

Stay curious, stay creative, and keep coding! ðŸ’»âœ¨

"The best way to predict the future is to build it." - You, right now! ðŸš€

---

Happy Coding! ðŸŽŠ
- Akash Shahade
