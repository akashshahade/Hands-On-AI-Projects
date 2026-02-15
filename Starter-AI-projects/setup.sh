#!/bin/bash

echo "💪 AI Workout Planner Agent - Setup Script"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found"
echo ""

# Check Python version
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "📌 Python version: $PYTHON_VERSION"
echo ""

# Create virtual environment (optional)
read -p "Do you want to create a virtual environment? (y/n): " CREATE_VENV

if [ "$CREATE_VENV" = "y" ] || [ "$CREATE_VENV" = "Y" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
    
    echo "🔄 Activating virtual environment..."
    source venv/bin/activate
    echo "✅ Virtual environment activated"
    echo ""
fi

# Install requirements
echo "📦 Installing required packages..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All packages installed successfully!"
else
    echo "❌ Failed to install packages. Please check the error messages above."
    exit 1
fi

echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚙️ Setting up environment variables..."
    cp .env.example .env
    echo "✅ Created .env file from template"
    echo ""
    echo "⚠️  IMPORTANT: Please edit the .env file and add your OpenAI API key!"
    echo "   You can get one from: https://platform.openai.com/api-keys"
    echo ""
    read -p "Press Enter to open .env file in default editor..."
    ${EDITOR:-nano} .env
else
    echo "✅ .env file already exists"
fi

echo ""
echo "=========================================="
echo "🎉 Setup complete!"
echo ""
echo "To run the application:"
echo ""
if [ "$CREATE_VENV" = "y" ] || [ "$CREATE_VENV" = "Y" ]; then
    echo "1. Activate the virtual environment:"
    echo "   source venv/bin/activate"
    echo ""
    echo "2. Run the app:"
    echo "   streamlit run app.py"
else
    echo "   streamlit run app.py"
fi
echo ""
echo "💪 Get ready to transform your fitness journey!"
echo "=========================================="
