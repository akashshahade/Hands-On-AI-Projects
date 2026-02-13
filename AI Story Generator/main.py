"""
AI Story Generator - Generate creative stories using OpenAI GPT
"""

import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page configuration
st.set_page_config(
    page_title="AI Story Generator",
    page_icon="📖",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        height: 3em;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    .story-output {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and description
st.title("📖 AI Story Generator")
st.markdown("### Create amazing stories with AI in seconds!")
st.markdown("---")

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Story Settings")
    
    # Genre selection
    genre = st.selectbox(
        "Choose Genre:",
        ["Fantasy", "Science Fiction", "Mystery", "Romance", "Horror", 
         "Adventure", "Comedy", "Thriller", "Drama", "Children's Story"]
    )
    
    # Story length
    length = st.selectbox(
        "Story Length:",
        ["Short (100-200 words)", "Medium (300-500 words)", "Long (600-800 words)"]
    )
    
    # Writing style
    style = st.selectbox(
        "Writing Style:",
        ["Descriptive", "Dialogue-heavy", "Fast-paced", "Poetic", "Simple"]
    )
    
    # Add characters option
    add_characters = st.checkbox("Add custom character names")
    
    if add_characters:
        character_names = st.text_input("Character names (comma-separated):", 
                                       placeholder="e.g., Alice, Bob, Charlie")
    
    st.markdown("---")
    st.info("💡 **Tip:** Be specific with your prompt for better stories!")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎨 Story Prompt")
    
    # Story prompt input
    story_prompt = st.text_area(
        "What's your story about?",
        placeholder="Example: A dragon who discovers they're afraid of heights...",
        height=150,
        help="Describe the main idea, characters, or situation for your story"
    )
    
    # Additional details
    with st.expander("➕ Add More Details (Optional)"):
        setting = st.text_input("Setting/Location:", 
                               placeholder="e.g., Medieval castle, Mars colony, Modern city")
        conflict = st.text_input("Main Conflict:", 
                                placeholder="e.g., Must save the kingdom, Find lost treasure")
        tone = st.selectbox("Tone:", ["Happy", "Sad", "Mysterious", "Exciting", "Funny", "Dark"])
    
    # Generate button
    generate_button = st.button("✨ Generate Story", use_container_width=True)

with col2:
    st.subheader("📚 Generated Story")
    
    # Placeholder for story output
    story_container = st.empty()

# Function to generate story
def generate_story(prompt, genre, length, style, setting="", conflict="", tone="", characters=""):
    """Generate story using OpenAI API"""
    
    # Determine word count based on length
    word_counts = {
        "Short (100-200 words)": "150-200",
        "Medium (300-500 words)": "400-500",
        "Long (600-800 words)": "700-800"
    }
    word_count = word_counts[length]
    
    # Build the system prompt
    system_prompt = f"""You are a creative story writer. Write a {genre} story in a {style} style.
    The story should be approximately {word_count} words.
    Make it engaging, creative, and well-structured with a clear beginning, middle, and end."""
    
    # Build the user prompt
    user_prompt = f"Story idea: {prompt}\n\n"
    
    if setting:
        user_prompt += f"Setting: {setting}\n"
    if conflict:
        user_prompt += f"Main conflict: {conflict}\n"
    if tone:
        user_prompt += f"Tone: {tone}\n"
    if characters:
        user_prompt += f"Include these characters: {characters}\n"
    
    user_prompt += f"\nWrite a captivating {genre} story based on the above."
    
    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,  # Higher temperature for more creativity
            max_tokens=1000
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error generating story: {str(e)}"

# Generate story when button is clicked
if generate_button:
    if not story_prompt:
        st.warning("⚠️ Please enter a story prompt!")
    else:
        with story_container:
            with st.spinner("✍️ Writing your story... This may take 10-20 seconds..."):
                # Get optional parameters
                setting_text = setting if 'setting' in locals() else ""
                conflict_text = conflict if 'conflict' in locals() else ""
                tone_text = tone if 'tone' in locals() else ""
                characters_text = character_names if add_characters and 'character_names' in locals() else ""
                
                # Generate the story
                story = generate_story(
                    story_prompt, 
                    genre, 
                    length, 
                    style,
                    setting_text,
                    conflict_text,
                    tone_text,
                    characters_text
                )
                
                # Display the story
                st.markdown(f"""
                <div class="story-output">
                    <h4>📖 Your Story</h4>
                    <p style="line-height: 1.8; font-size: 16px;">{story}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Download button
                st.download_button(
                    label="💾 Download Story",
                    data=story,
                    file_name=f"ai_story_{genre.lower().replace(' ', '_')}.txt",
                    mime="text/plain"
                )
                
                # Word count
                word_count = len(story.split())
                st.success(f"✅ Story generated! ({word_count} words)")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Made with ❤️ using OpenAI GPT | <a href='https://github.com/yourusername/Hands-On-AI-Projects'>Hands-On-AI-Projects</a></p>
    </div>
    """, unsafe_allow_html=True)
