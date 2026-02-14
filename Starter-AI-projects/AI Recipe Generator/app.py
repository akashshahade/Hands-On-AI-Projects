import streamlit as st
import os
from openai import OpenAI
import json

# Page configuration
st.set_page_config(
    page_title="AI Recipe Generator Agent",
    page_icon="👨‍🍳",
    layout="wide"
)

# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("⚠️ OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
        st.stop()
    return OpenAI(api_key=api_key)

client = get_openai_client()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "generated_recipe" not in st.session_state:
    st.session_state.generated_recipe = None

def generate_recipe(ingredients, dietary_restrictions, cuisine_preference, skill_level, cooking_time):
    """Generate a personalized recipe using OpenAI GPT-4"""
    
    system_prompt = """You are a professional chef and recipe developer with expertise in creating 
    delicious, personalized recipes. You excel at working with available ingredients and adapting 
    recipes to dietary needs and preferences. 
    
    When generating recipes, provide:
    1. A creative recipe name
    2. Brief description
    3. Preparation time and cooking time
    4. Difficulty level
    5. Servings
    6. Detailed ingredient list with measurements
    7. Step-by-step cooking instructions
    8. Helpful cooking tips
    9. Nutritional information (approximate)
    10. Possible variations or substitutions
    
    Format your response in a clear, structured way using markdown."""
    
    user_prompt = f"""Create a personalized recipe based on the following:

Available Ingredients: {ingredients}
Dietary Restrictions: {dietary_restrictions if dietary_restrictions else 'None'}
Cuisine Preference: {cuisine_preference if cuisine_preference else 'Any'}
Skill Level: {skill_level}
Maximum Cooking Time: {cooking_time} minutes

Please create a recipe that:
- Primarily uses the available ingredients
- Respects all dietary restrictions
- Matches the cuisine preference if specified
- Is appropriate for the skill level
- Can be completed within the time limit
- Suggests any additional common ingredients that might enhance the dish"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=2000
        )
        
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating recipe: {str(e)}")
        return None

def get_recipe_suggestions(ingredients):
    """Get quick recipe ideas based on ingredients"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful chef assistant. Suggest 5 quick recipe ideas based on given ingredients. Return only the recipe names, one per line."},
                {"role": "user", "content": f"Suggest 5 recipe ideas using these ingredients: {ingredients}"}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        suggestions = response.choices[0].message.content.strip().split('\n')
        return [s.strip('1234567890. -') for s in suggestions if s.strip()]
    except Exception as e:
        return []

# App Header
st.title("👨‍🍳 AI Recipe Generator Agent")
st.markdown("### Create personalized recipes based on your available ingredients")
st.markdown("---")

# Sidebar for inputs
with st.sidebar:
    st.header("🥘 Recipe Preferences")
    
    # Ingredients input
    st.subheader("Available Ingredients")
    ingredients = st.text_area(
        "Enter your ingredients (comma-separated)",
        placeholder="e.g., chicken, tomatoes, onions, garlic, olive oil",
        height=100,
        help="List all the ingredients you have available"
    )
    
    # Dietary restrictions
    st.subheader("Dietary Restrictions")
    dietary_options = st.multiselect(
        "Select any dietary restrictions",
        ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Nut-Free", "Keto", "Paleo", "Low-Carb", "Halal", "Kosher"],
        help="Select all that apply"
    )
    dietary_restrictions = ", ".join(dietary_options) if dietary_options else "None"
    
    # Cuisine preference
    st.subheader("Cuisine Preference")
    cuisine_preference = st.selectbox(
        "Choose a cuisine style",
        ["Any", "Italian", "Mexican", "Chinese", "Indian", "Japanese", "Thai", "Mediterranean", 
         "American", "French", "Korean", "Middle Eastern", "Greek", "Spanish"]
    )
    
    # Skill level
    st.subheader("Cooking Skill Level")
    skill_level = st.select_slider(
        "Select your skill level",
        options=["Beginner", "Intermediate", "Advanced", "Professional"]
    )
    
    # Cooking time
    st.subheader("Maximum Cooking Time")
    cooking_time = st.slider(
        "Time in minutes",
        min_value=15,
        max_value=180,
        value=45,
        step=15,
        help="Maximum time you want to spend cooking"
    )
    
    st.markdown("---")
    
    # Generate button
    generate_button = st.button("🔥 Generate Recipe", type="primary", use_container_width=True)
    
    # Quick suggestions
    if ingredients and len(ingredients.strip()) > 0:
        if st.button("💡 Get Quick Ideas", use_container_width=True):
            with st.spinner("Getting recipe ideas..."):
                suggestions = get_recipe_suggestions(ingredients)
                if suggestions:
                    st.subheader("Quick Recipe Ideas:")
                    for idx, suggestion in enumerate(suggestions, 1):
                        st.write(f"{idx}. {suggestion}")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    if generate_button:
        if not ingredients or len(ingredients.strip()) == 0:
            st.warning("⚠️ Please enter at least some ingredients to generate a recipe.")
        else:
            with st.spinner("👨‍🍳 Creating your personalized recipe..."):
                recipe = generate_recipe(
                    ingredients, 
                    dietary_restrictions, 
                    cuisine_preference, 
                    skill_level, 
                    cooking_time
                )
                
                if recipe:
                    st.session_state.generated_recipe = recipe
                    st.session_state.messages.append({
                        "ingredients": ingredients,
                        "restrictions": dietary_restrictions,
                        "cuisine": cuisine_preference,
                        "skill": skill_level,
                        "time": cooking_time,
                        "recipe": recipe
                    })
    
    # Display generated recipe
    if st.session_state.generated_recipe:
        st.markdown("## 📖 Your Personalized Recipe")
        st.markdown(st.session_state.generated_recipe)
        
        # Download button
        st.download_button(
            label="📥 Download Recipe",
            data=st.session_state.generated_recipe,
            file_name="my_recipe.txt",
            mime="text/plain"
        )
    else:
        # Welcome message
        st.info("""
        ### 👋 Welcome to AI Recipe Generator Agent!
        
        **How to use:**
        1. Enter your available ingredients in the sidebar
        2. Select any dietary restrictions
        3. Choose your preferred cuisine (optional)
        4. Set your cooking skill level
        5. Set maximum cooking time
        6. Click "Generate Recipe" to create your personalized recipe!
        
        **Features:**
        - ✅ Personalized recipes based on YOUR ingredients
        - ✅ Respects dietary restrictions and preferences
        - ✅ Adapts to your skill level
        - ✅ Considers your available time
        - ✅ Provides detailed instructions and tips
        - ✅ Suggests variations and substitutions
        """)

with col2:
    st.markdown("### 📝 Recipe History")
    
    if st.session_state.messages:
        for idx, msg in enumerate(reversed(st.session_state.messages[-5:]), 1):
            with st.expander(f"Recipe {len(st.session_state.messages) - idx + 1}"):
                st.write(f"**Ingredients:** {msg['ingredients'][:50]}...")
                st.write(f"**Cuisine:** {msg['cuisine']}")
                st.write(f"**Skill Level:** {msg['skill']}")
                if st.button(f"View Recipe {len(st.session_state.messages) - idx + 1}", key=f"view_{idx}"):
                    st.session_state.generated_recipe = msg['recipe']
                    st.rerun()
    else:
        st.info("No recipes generated yet. Start by entering your ingredients!")
    
    # Tips section
    st.markdown("---")
    st.markdown("### 💡 Cooking Tips")
    st.markdown("""
    - Always read the entire recipe before starting
    - Prep all ingredients before cooking (mise en place)
    - Taste and adjust seasoning as you cook
    - Don't be afraid to substitute ingredients
    - Keep a clean workspace
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Made with ❤️ using OpenAI GPT-4 | 
        <a href='https://github.com/Shubhamsaboo/awesome-llm-apps'>Awesome LLM Apps</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
