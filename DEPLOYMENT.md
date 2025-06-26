# 🚀 Deployment Guide

## Step 1: Push to GitHub

1. **Create a new repository on GitHub**:
   - Go to https://github.com/new
   - Name it `manipur-virtual-gallery`
   - Don't initialize with README (we already have one)

2. **Add GitHub as remote and push**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/manipur-virtual-gallery.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy to Render (Free)

1. **Go to https://render.com** and sign up/login
2. **Connect your GitHub account**
3. **Click "New +" → "Web Service"**
4. **Select your repository** (`manipur-virtual-gallery`)
5. **Configure deployment**:
   - **Name**: `manipur-virtual-gallery`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Select "Free"

6. **Add Environment Variables**:
   - Key: `OPENAI_API_KEY`
   - Value: `your_actual_api_key_here` (when you get one)

7. **Deploy**: Click "Create Web Service"

Your website will be live at: `https://manipur-virtual-gallery.onrender.com`

## Alternative: Deploy to Railway

1. **Go to https://railway.app** and sign up
2. **Click "New Project" → "Deploy from GitHub repo"**
3. **Select your repository**
4. **Add environment variable**: `OPENAI_API_KEY`
5. **Deploy automatically**

## Alternative: Deploy to Heroku

1. **Install Heroku CLI**
2. **Login**: `heroku login`
3. **Create app**: `heroku create manipur-virtual-gallery`
4. **Set environment variable**: `heroku config:set OPENAI_API_KEY=your_key`
5. **Deploy**: `git push heroku main`

## 📝 Notes

- The website works with mock responses even without OpenAI API key
- Free hosting tiers may sleep after inactivity
- For production, consider upgrading to paid plans for better performance
