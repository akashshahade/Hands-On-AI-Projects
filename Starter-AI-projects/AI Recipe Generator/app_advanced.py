import streamlit as st
import os
from openai import OpenAI
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Recipe Generator Agent Pro",
    page_icon="👨‍🍳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .recipe-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .ingredient-tag {
        display: inline-block;
        background-color: #e8f4f8;
        color: #0066cc;
        padding: 5px 10px;
        border-radius: 15px;
        margin: 3px;
        font-size: 14px;
    }
    .tip-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

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
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "ingredient_pantry" not in st.session_state:
    st.session_state.ingredient_pantry = []

def generate_recipe_with_nutrition(ingredients, dietary_restrictions, cuisine_preference, 
                                   skill_level, cooking_time, servings, meal_type):
    """Generate a detailed recipe with nutritional information"""
    
    system_prompt = """You are an expert chef and nutritionist with 20 years of experience. 
    You create delicious, balanced recipes that are both tasty and nutritious.
    
    Provide recipes in the following structured format:
    
    # [Recipe Name]
    
    ## Description
    [A compelling 2-3 sentence description]
    
    ## Info
    - **Prep Time:** X minutes
    - **Cook Time:** X minutes
    - **Total Time:** X minutes
    - **Difficulty:** [Beginner/Intermediate/Advanced]
    - **Servings:** X
    - **Meal Type:** [Breakfast/Lunch/Dinner/Snack/Dessert]
    
    ## Ingredients
    [List with exact measurements]
    
    ## Instructions
    [Detailed numbered steps]
    
    ## Cooking Tips
    [Professional tips and tricks]
    
    ## Nutritional Information (per serving)
    - Calories: X kcal
    - Protein: X g
    - Carbohydrates: X g
    - Fat: X g
    - Fiber: X g
    - Sugar: X g
    
    ## Variations
    [Possible substitutions and variations]
    
    ## Wine/Beverage Pairing
    [Suggested drink pairing]
    """
    
    user_prompt = f"""Create an exceptional {meal_type} recipe with these specifications:

**Available Ingredients:** {ingredients}
**Dietary Restrictions:** {dietary_restrictions if dietary_restrictions else 'None'}
**Cuisine:** {cuisine_preference if cuisine_preference else 'Any'}
**Skill Level:** {skill_level}
**Max Cooking Time:** {cooking_time} minutes
**Servings:** {servings}

Requirements:
1. Make the best use of available ingredients
2. Strictly follow dietary restrictions
3. Match the cuisine style
4. Be appropriate for skill level
5. Complete within time limit
6. Provide accurate nutritional estimates
7. Include professional cooking techniques
8. Suggest complementary ingredients if needed"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=2500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating recipe: {str(e)}")
        return None

def generate_meal_plan(ingredients, days, dietary_restrictions):
    """Generate a multi-day meal plan"""
    
    system_prompt = """You are a meal planning expert. Create balanced, varied meal plans 
    that use available ingredients efficiently and minimize food waste."""
    
    user_prompt = f"""Create a {days}-day meal plan using these ingredients: {ingredients}
    
Dietary Restrictions: {dietary_restrictions if dietary_restrictions else 'None'}

For each day provide:
- Breakfast
- Lunch
- Dinner
- Snack (optional)

Include brief descriptions and ensure variety across days."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating meal plan: {str(e)}")
        return None

def generate_shopping_list(recipe_text, pantry_items):
    """Generate a shopping list from recipe minus pantry items"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Extract ingredients from recipe and create a shopping list. Remove items already in pantry. Format as a clean bullet list."},
                {"role": "user", "content": f"Recipe:\n{recipe_text}\n\nPantry Items:\n{', '.join(pantry_items) if pantry_items else 'None'}"}
            ],
            temperature=0.3,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return None

# App Header
st.title("👨‍🍳 AI Recipe Generator Agent Pro")
st.markdown("### Your personal AI chef with advanced features")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["🥘 Recipe Generator", "📅 Meal Planner", "❤️ Favorites", "🛒 Pantry"])

# Sidebar for common inputs
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Model selection
    model_choice = st.selectbox(
        "AI Model",
        ["gpt-4o-mini (Fast & Cheap)", "gpt-4o (Balanced)", "gpt-4 (Best Quality)"],
        help="Choose based on speed vs quality preference"
    )
    
    st.markdown("---")
    
    # Quick access buttons
    st.subheader("Quick Actions")
    if st.button("🍳 Random Recipe", use_container_width=True):
        st.info("Coming soon! Will generate a random recipe from your pantry.")
    
    if st.button("📊 Nutrition Analysis", use_container_width=True):
        st.info("Coming soon! Will analyze nutritional balance.")
    
    st.markdown("---")
    
    # Statistics
    st.subheader("📈 Your Stats")
    st.metric("Recipes Generated", len(st.session_state.messages))
    st.metric("Favorites Saved", len(st.session_state.favorites))
    st.metric("Pantry Items", len(st.session_state.ingredient_pantry))

# TAB 1: Recipe Generator
with tab1:
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("🥗 Recipe Preferences")
        
        # Ingredients input with suggestions
        ingredients = st.text_area(
            "Available Ingredients",
            placeholder="e.g., chicken breast, tomatoes, onions, garlic, olive oil, basil",
            height=100,
            help="Enter ingredients separated by commas"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Dietary restrictions
            dietary_options = st.multiselect(
                "Dietary Restrictions",
                ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Nut-Free", 
                 "Keto", "Paleo", "Low-Carb", "Halal", "Kosher", "Low-Sodium"],
            )
            dietary_restrictions = ", ".join(dietary_options) if dietary_options else "None"
            
            # Cuisine preference
            cuisine_preference = st.selectbox(
                "Cuisine Style",
                ["Any", "Italian", "Mexican", "Chinese", "Indian", "Japanese", "Thai", 
                 "Mediterranean", "American", "French", "Korean", "Middle Eastern", 
                 "Greek", "Spanish", "Vietnamese", "Caribbean"]
            )
            
            # Skill level
            skill_level = st.select_slider(
                "Cooking Skill Level",
                options=["Beginner", "Intermediate", "Advanced", "Professional"]
            )
        
        with col2:
            # Meal type
            meal_type = st.selectbox(
                "Meal Type",
                ["Any", "Breakfast", "Brunch", "Lunch", "Dinner", "Snack", "Dessert", "Appetizer"]
            )
            
            # Servings
            servings = st.number_input(
                "Number of Servings",
                min_value=1,
                max_value=12,
                value=4,
                step=1
            )
            
            # Cooking time
            cooking_time = st.slider(
                "Maximum Time (minutes)",
                min_value=15,
                max_value=180,
                value=45,
                step=15
            )
        
        # Generate buttons
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            generate_button = st.button("🔥 Generate Recipe", type="primary", use_container_width=True)
        with col_btn2:
            if st.button("💡 Quick Ideas", use_container_width=True):
                st.info("Getting quick recipe ideas...")
        
        # Display recipe
        if generate_button:
            if not ingredients or len(ingredients.strip()) == 0:
                st.warning("⚠️ Please enter at least some ingredients.")
            else:
                with st.spinner("👨‍🍳 Creating your personalized recipe..."):
                    recipe = generate_recipe_with_nutrition(
                        ingredients, dietary_restrictions, cuisine_preference, 
                        skill_level, cooking_time, servings, meal_type
                    )
                    
                    if recipe:
                        st.session_state.generated_recipe = recipe
                        recipe_data = {
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "ingredients": ingredients,
                            "restrictions": dietary_restrictions,
                            "cuisine": cuisine_preference,
                            "skill": skill_level,
                            "time": cooking_time,
                            "servings": servings,
                            "meal_type": meal_type,
                            "recipe": recipe
                        }
                        st.session_state.messages.append(recipe_data)
        
        if st.session_state.generated_recipe:
            st.markdown("---")
            st.markdown("## 📖 Your Recipe")
            st.markdown(st.session_state.generated_recipe)
            
            # Action buttons
            col_action1, col_action2, col_action3 = st.columns(3)
            
            with col_action1:
                if st.button("❤️ Add to Favorites", use_container_width=True):
                    if st.session_state.generated_recipe not in st.session_state.favorites:
                        st.session_state.favorites.append({
                            "recipe": st.session_state.generated_recipe,
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })
                        st.success("Added to favorites!")
                    else:
                        st.info("Already in favorites!")
            
            with col_action2:
                st.download_button(
                    label="📥 Download Recipe",
                    data=st.session_state.generated_recipe,
                    file_name=f"recipe_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            with col_action3:
                if st.button("🛒 Shopping List", use_container_width=True):
                    with st.spinner("Generating shopping list..."):
                        shopping_list = generate_shopping_list(
                            st.session_state.generated_recipe, 
                            st.session_state.ingredient_pantry
                        )
                        if shopping_list:
                            st.markdown("### 🛒 Shopping List")
                            st.markdown(shopping_list)
    
    with col_right:
        st.subheader("📜 Recent Recipes")
        
        if st.session_state.messages:
            for idx, msg in enumerate(reversed(st.session_state.messages[-5:])):
                with st.expander(f"Recipe {len(st.session_state.messages) - idx}", expanded=False):
                    st.write(f"**Time:** {msg.get('timestamp', 'N/A')}")
                    st.write(f"**Cuisine:** {msg['cuisine']}")
                    st.write(f"**Meal:** {msg.get('meal_type', 'N/A')}")
                    st.write(f"**Servings:** {msg.get('servings', 'N/A')}")
                    if st.button(f"View Full Recipe", key=f"view_{idx}", use_container_width=True):
                        st.session_state.generated_recipe = msg['recipe']
                        st.rerun()
        else:
            st.info("No recipes yet. Start generating!")
        
        st.markdown("---")
        st.markdown("### 💡 Pro Tips")
        st.markdown("""
        - Use **fresh herbs** for better flavor
        - **Taste as you cook** and adjust seasoning
        - **Prep everything** before you start (mise en place)
        - **Room temperature** ingredients mix better
        - **Rest your meat** before cutting
        """)

# TAB 2: Meal Planner
with tab2:
    st.subheader("📅 Weekly Meal Planner")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        meal_plan_ingredients = st.text_area(
            "Available Ingredients for Meal Plan",
            placeholder="Enter all ingredients you want to use this week",
            height=100
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            meal_plan_days = st.slider("Number of Days", 1, 7, 7)
        with col_b:
            meal_plan_restrictions = st.multiselect(
                "Dietary Restrictions",
                ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Keto"],
                key="meal_plan_restrictions"
            )
        
        if st.button("📅 Generate Meal Plan", type="primary", use_container_width=True):
            if meal_plan_ingredients:
                with st.spinner("Creating your meal plan..."):
                    restrictions = ", ".join(meal_plan_restrictions) if meal_plan_restrictions else "None"
                    meal_plan = generate_meal_plan(meal_plan_ingredients, meal_plan_days, restrictions)
                    if meal_plan:
                        st.markdown("## 📅 Your Meal Plan")
                        st.markdown(meal_plan)
                        
                        st.download_button(
                            label="📥 Download Meal Plan",
                            data=meal_plan,
                            file_name=f"meal_plan_{datetime.now().strftime('%Y%m%d')}.txt",
                            mime="text/plain"
                        )
            else:
                st.warning("Please enter ingredients for meal planning")
    
    with col2:
        st.info("""
        ### How Meal Planning Works
        
        1. Enter all ingredients you have
        2. Select number of days
        3. Choose dietary restrictions
        4. Get a complete meal plan!
        
        **Benefits:**
        - Reduces food waste
        - Saves time
        - Ensures variety
        - Balanced nutrition
        """)

# TAB 3: Favorites
with tab3:
    st.subheader("❤️ Your Favorite Recipes")
    
    if st.session_state.favorites:
        for idx, fav in enumerate(st.session_state.favorites):
            with st.expander(f"Favorite Recipe {idx + 1} - {fav['timestamp']}", expanded=False):
                st.markdown(fav['recipe'])
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"🗑️ Remove", key=f"remove_fav_{idx}", use_container_width=True):
                        st.session_state.favorites.pop(idx)
                        st.rerun()
                with col2:
                    st.download_button(
                        label="📥 Download",
                        data=fav['recipe'],
                        file_name=f"favorite_recipe_{idx+1}.txt",
                        mime="text/plain",
                        key=f"download_fav_{idx}",
                        use_container_width=True
                    )
    else:
        st.info("No favorite recipes yet. Generate recipes and add them to favorites!")

# TAB 4: Pantry
with tab4:
    st.subheader("🛒 Virtual Pantry")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Add Items to Pantry")
        new_item = st.text_input("Enter ingredient name")
        
        col_add, col_clear = st.columns(2)
        with col_add:
            if st.button("➕ Add to Pantry", use_container_width=True):
                if new_item and new_item not in st.session_state.ingredient_pantry:
                    st.session_state.ingredient_pantry.append(new_item)
                    st.success(f"Added {new_item}!")
                    st.rerun()
        
        with col_clear:
            if st.button("🗑️ Clear All", use_container_width=True):
                st.session_state.ingredient_pantry = []
                st.rerun()
        
        st.markdown("---")
        st.markdown("### 📦 Your Pantry Items")
        
        if st.session_state.ingredient_pantry:
            # Display as tags
            tags_html = ""
            for item in st.session_state.ingredient_pantry:
                tags_html += f'<span class="ingredient-tag">{item}</span>'
            st.markdown(tags_html, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Remove individual items
            item_to_remove = st.selectbox("Select item to remove", st.session_state.ingredient_pantry)
            if st.button("Remove Selected", use_container_width=True):
                st.session_state.ingredient_pantry.remove(item_to_remove)
                st.rerun()
        else:
            st.info("Your pantry is empty. Add ingredients above!")
    
    with col2:
        st.info("""
        ### Pantry Benefits
        
        - Track available ingredients
        - Quick recipe generation
        - Smart shopping lists
        - Reduce waste
        
        **Tip:** Keep your pantry updated for best results!
        """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>AI Recipe Generator Agent Pro v2.0 | Powered by OpenAI GPT-4 | 
        Made with ❤️ for food lovers</p>
        <p><a href='https://github.com/Shubhamsaboo/awesome-llm-apps'>Awesome LLM Apps</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
