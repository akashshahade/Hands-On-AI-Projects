import streamlit as st
import os
from openai import OpenAI
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Workout Planner Agent",
    page_icon="💪",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .workout-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 15px 0;
    }
    .exercise-item {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border: 1px solid #e0e0e0;
    }
    .tip-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    .metric-card {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin: 10px 0;
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
if "workout_history" not in st.session_state:
    st.session_state.workout_history = []
if "current_workout" not in st.session_state:
    st.session_state.current_workout = None

def generate_workout_plan(fitness_goal, experience_level, workout_days, duration, 
                         equipment, target_areas, limitations):
    """Generate a personalized workout plan using OpenAI GPT-4"""
    
    system_prompt = """You are a certified personal trainer and fitness expert with 15+ years of experience. 
    You create safe, effective, and personalized workout plans tailored to individual goals and limitations.
    
    Provide workout plans in the following structured format:
    
    # [Workout Plan Title]
    
    ## Overview
    [Brief description of the workout program and its benefits]
    
    ## Weekly Schedule
    [Outline of the weekly workout structure]
    
    ## Detailed Workout Routine
    
    ### Day 1: [Focus Area]
    
    **Warm-up (5-10 minutes)**
    - [Exercise 1]: [Duration/Reps]
    - [Exercise 2]: [Duration/Reps]
    
    **Main Workout**
    
    1. **[Exercise Name]**
       - Sets: X
       - Reps: X (or Duration)
       - Rest: X seconds
       - Notes: [Proper form tips]
    
    [Continue for all exercises]
    
    **Cool-down (5-10 minutes)**
    - [Stretching exercises]
    
    [Repeat structure for each workout day]
    
    ## Exercise Modifications
    [Easier and harder variations for key exercises]
    
    ## Nutrition Tips
    [Brief dietary recommendations to support the fitness goal]
    
    ## Progress Tracking
    [How to measure progress and when to increase intensity]
    
    ## Safety Tips
    [Important safety considerations and injury prevention]
    """
    
    user_prompt = f"""Create a personalized workout plan with the following specifications:

**Fitness Goal:** {fitness_goal}
**Experience Level:** {experience_level}
**Workout Days per Week:** {workout_days}
**Session Duration:** {duration} minutes
**Available Equipment:** {equipment}
**Target Areas:** {target_areas}
**Limitations/Injuries:** {limitations if limitations else 'None'}

Requirements:
1. Design a progressive workout plan suitable for {experience_level} level
2. Focus on exercises that support the goal: {fitness_goal}
3. Include proper warm-up and cool-down routines
4. Provide clear instructions for each exercise
5. Include sets, reps, rest periods, and form cues
6. Suggest modifications for different fitness levels
7. Ensure the plan respects any mentioned limitations
8. Include recovery and rest day recommendations
9. Provide tips for tracking progress
10. Keep workouts within the {duration}-minute timeframe"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=3000
        )
        
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating workout plan: {str(e)}")
        return None

def get_exercise_tips(exercise_name):
    """Get detailed tips for a specific exercise"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a fitness expert. Provide concise, practical tips for proper exercise form and technique."},
                {"role": "user", "content": f"Provide 5 key tips for proper form when doing: {exercise_name}"}
            ],
            temperature=0.5,
            max_tokens=300
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return None

# App Header
st.markdown("""
<div class="main-header">
    <h1>💪 AI Workout Planner Agent</h1>
    <p>Generate personalized fitness routines based on your goals</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("🎯 Your Fitness Profile")
    
    # Fitness Goal
    fitness_goal = st.selectbox(
        "Primary Fitness Goal",
        [
            "Build Muscle (Hypertrophy)",
            "Lose Weight (Fat Loss)",
            "Increase Strength",
            "Improve Endurance",
            "General Fitness",
            "Athletic Performance",
            "Flexibility & Mobility",
            "Body Recomposition"
        ],
        help="Select your main fitness objective"
    )
    
    # Experience Level
    experience_level = st.select_slider(
        "Experience Level",
        options=["Beginner", "Intermediate", "Advanced"],
        value="Beginner",
        help="Your current fitness level"
    )
    
    # Workout Frequency
    workout_days = st.slider(
        "Workout Days per Week",
        min_value=2,
        max_value=7,
        value=4,
        step=1,
        help="How many days per week can you commit to working out?"
    )
    
    # Session Duration
    duration = st.select_slider(
        "Session Duration (minutes)",
        options=[20, 30, 45, 60, 75, 90],
        value=45,
        help="How long is each workout session?"
    )
    
    # Available Equipment
    st.subheader("Available Equipment")
    equipment_options = st.multiselect(
        "Select all that apply",
        [
            "No Equipment (Bodyweight)",
            "Dumbbells",
            "Barbell",
            "Resistance Bands",
            "Pull-up Bar",
            "Bench",
            "Kettlebells",
            "Cable Machine",
            "Full Gym Access"
        ],
        default=["No Equipment (Bodyweight)"]
    )
    equipment = ", ".join(equipment_options) if equipment_options else "No Equipment"
    
    # Target Areas
    st.subheader("Target Areas")
    target_options = st.multiselect(
        "Focus areas (optional)",
        [
            "Chest",
            "Back",
            "Shoulders",
            "Arms",
            "Core/Abs",
            "Legs",
            "Glutes",
            "Full Body"
        ],
        default=["Full Body"]
    )
    target_areas = ", ".join(target_options) if target_options else "Full Body"
    
    # Limitations
    limitations = st.text_area(
        "Injuries or Limitations",
        placeholder="e.g., Lower back pain, knee injury, etc.",
        help="Any injuries or physical limitations we should consider"
    )
    
    st.markdown("---")
    
    # Generate button
    generate_button = st.button("🔥 Generate Workout Plan", type="primary", use_container_width=True)

# Main content area
col1, col2 = st.columns([3, 1])

with col1:
    if generate_button:
        with st.spinner("💪 Creating your personalized workout plan..."):
            workout_plan = generate_workout_plan(
                fitness_goal,
                experience_level,
                workout_days,
                duration,
                equipment,
                target_areas,
                limitations
            )
            
            if workout_plan:
                st.session_state.current_workout = workout_plan
                workout_data = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "goal": fitness_goal,
                    "level": experience_level,
                    "days": workout_days,
                    "duration": duration,
                    "equipment": equipment,
                    "plan": workout_plan
                }
                st.session_state.workout_history.append(workout_data)
    
    # Display workout plan
    if st.session_state.current_workout:
        st.markdown("## 📋 Your Personalized Workout Plan")
        
        # Action buttons at the top
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            st.download_button(
                label="📥 Download Plan",
                data=st.session_state.current_workout,
                file_name=f"workout_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col_btn2:
            if st.button("📧 Email Plan", use_container_width=True):
                st.info("Email functionality coming soon! For now, use the download button.")
        
        with col_btn3:
            if st.button("📊 Track Workout", use_container_width=True):
                st.info("Workout tracking feature coming soon!")
        
        st.markdown("---")
        
        # Display the workout plan
        st.markdown(st.session_state.current_workout)
        
        st.markdown("---")
        
        # Exercise Tips Section
        with st.expander("💡 Need help with specific exercises?", expanded=False):
            st.write("Enter an exercise name to get detailed form tips:")
            exercise_name = st.text_input("Exercise name", placeholder="e.g., Push-ups, Squats, Deadlift")
            
            if st.button("Get Exercise Tips"):
                if exercise_name:
                    with st.spinner("Getting exercise tips..."):
                        tips = get_exercise_tips(exercise_name)
                        if tips:
                            st.markdown(f"### Tips for {exercise_name}")
                            st.markdown(tips)
                else:
                    st.warning("Please enter an exercise name")
    
    else:
        # Welcome message
        st.info("""
        ### 👋 Welcome to AI Workout Planner Agent!
        
        **Get started in 3 easy steps:**
        
        1. **Set Your Goal** - Choose what you want to achieve (build muscle, lose weight, etc.)
        2. **Configure Your Profile** - Tell us about your experience level, available equipment, and schedule
        3. **Generate Your Plan** - Click the button and get a personalized workout routine!
        
        **What You'll Get:**
        - ✅ Customized workout routine for your fitness level
        - ✅ Detailed exercise instructions with sets and reps
        - ✅ Proper warm-up and cool-down routines
        - ✅ Safety tips and form guidance
        - ✅ Progress tracking recommendations
        - ✅ Nutrition tips to support your goals
        
        **No equipment? No problem!** We can create effective bodyweight workouts for you.
        """)
        
        # Quick Start Guide
        st.markdown("### 🚀 Quick Start Examples")
        
        example_col1, example_col2 = st.columns(2)
        
        with example_col1:
            st.markdown("""
            <div class="workout-card">
            <h4>🏋️ Beginner at Home</h4>
            <p><strong>Goal:</strong> General Fitness<br>
            <strong>Equipment:</strong> None<br>
            <strong>Frequency:</strong> 3x per week<br>
            <strong>Duration:</strong> 30 minutes</p>
            </div>
            """, unsafe_allow_html=True)
        
        with example_col2:
            st.markdown("""
            <div class="workout-card">
            <h4>💪 Gym Muscle Building</h4>
            <p><strong>Goal:</strong> Build Muscle<br>
            <strong>Equipment:</strong> Full Gym<br>
            <strong>Frequency:</strong> 5x per week<br>
            <strong>Duration:</strong> 60 minutes</p>
            </div>
            """, unsafe_allow_html=True)

with col2:
    st.markdown("### 📈 Your Progress")
    
    # Display stats
    st.markdown(f"""
    <div class="metric-card">
        <h3>{len(st.session_state.workout_history)}</h3>
        <p>Plans Generated</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recent Plans
    st.markdown("### 🕐 Recent Plans")
    
    if st.session_state.workout_history:
        for idx, workout in enumerate(reversed(st.session_state.workout_history[-3:])):
            with st.expander(f"Plan {len(st.session_state.workout_history) - idx}", expanded=False):
                st.write(f"**Date:** {workout['timestamp']}")
                st.write(f"**Goal:** {workout['goal']}")
                st.write(f"**Level:** {workout['level']}")
                st.write(f"**Days/Week:** {workout['days']}")
                if st.button(f"View", key=f"view_{idx}", use_container_width=True):
                    st.session_state.current_workout = workout['plan']
                    st.rerun()
    else:
        st.info("No workout plans yet. Generate your first one!")
    
    st.markdown("---")
    
    # Quick Tips
    st.markdown("### 💡 Fitness Tips")
    st.markdown("""
    - **Consistency** beats perfection
    - **Progressive overload** builds strength
    - **Rest days** are crucial for growth
    - **Nutrition** is 70% of results
    - **Form** over weight always
    - **Track** your progress weekly
    """)
    
    st.markdown("---")
    
    # Resources
    st.markdown("### 📚 Resources")
    st.markdown("""
    - [Exercise Form Videos](https://www.youtube.com)
    - [Nutrition Guide](https://www.nutrition.gov)
    - [Progress Tracker](https://www.myfitnesspal.com)
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>💪 AI Workout Planner Agent | Powered by OpenAI GPT-4</p>
        <p>⚠️ Always consult a healthcare professional before starting a new exercise program</p>
        <p>Made with ❤️ for fitness enthusiasts | 
        <a href='https://github.com/Shubhamsaboo/awesome-llm-apps'>Awesome LLM Apps</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
