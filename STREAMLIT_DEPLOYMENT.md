# Deploy to Streamlit Cloud (FREE & 24/7)

This guide will deploy your app to Streamlit Cloud in 5 minutes with zero cost.

## Step-by-Step Deployment

### Step 1: Create a GitHub Account (if you don't have one)
- Go to https://github.com
- Click "Sign up"
- Fill in email, password, username
- Verify email
- Done!

### Step 2: Create a GitHub Repository

1. Go to https://github.com/new
2. Name your repository: `credit-risk-app`
3. Keep it **PUBLIC** (important for free Streamlit Cloud)
4. Click "Create repository"
5. You'll see instructions - follow them OR use these commands:

```bash
cd "C:\Users\AVISHKAR LOKHANDE\Desktop\credit_risk_app"
git init
git add .
git commit -m "Initial commit - Credit Risk Assessment App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/credit-risk-app.git
git push -u origin main
```

**Note**: Replace `YOUR_USERNAME` with your actual GitHub username

### Step 3: Install Git (if needed)

If you don't have Git installed:
1. Download from https://git-scm.com/download/win
2. Run installer with default settings
3. Restart your terminal/PowerShell

### Step 4: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "New app"
3. Sign in with GitHub (click "GitHub" button)
4. Fill in:
   - **Repository**: `YOUR_USERNAME/credit-risk-app`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
5. Click "Deploy"
6. Wait 2-3 minutes...
7. Your app will be live at: `https://credit-risk-app.streamlit.app`

## File Checklist

You need these files in your GitHub repo:

- `streamlit_app.py` (main app)
- `requirements.txt` (dependencies)
- `.gitignore` (optional but good)

Your repo already has these!

## What is `requirements.txt`?

This file tells Streamlit Cloud what Python packages to install.

Current `requirements.txt`:
```
streamlit
pandas
```

If you add new packages, update this file and push to GitHub.

## Advantages of Streamlit Cloud

| Feature | Status |
|---------|--------|
| Cost | 100% FREE |
| Uptime | 24/7 Always Running |
| Domain | You get a professional URL |
| Auto-deploy | Push to GitHub → Auto-updates |
| SSL/HTTPS | Built-in |
| Sharing | Just share the URL |

## After Deployment

### To make changes:
1. Edit files locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your message"
   git push
   ```
3. Streamlit Cloud auto-deploys (takes 1-2 minutes)

### To share your app:
Just send this URL: `https://credit-risk-app.streamlit.app`

Anyone can use it - no installation needed!

### To stop/delete app:
1. Go to https://share.streamlit.io
2. Click the three dots on your app
3. Click "Settings" or "Delete"

## Troubleshooting

**Problem: "Repository not found"**
- Make sure repo is PUBLIC (not private)
- Check repository name matches exactly
- Wait a few minutes after pushing code

**Problem: "ModuleNotFoundError"**
- Add missing package to `requirements.txt`
- Commit and push
- App will redeploy automatically

**Problem: "App is crashing"**
- Check Streamlit Cloud logs
- Look for errors in your Python code
- Test locally first: `streamlit run streamlit_app.py`

## Keep App Running 24/7

**Streamlit Cloud does this for you!**

Your app runs 24/7 on Streamlit's servers. No need to keep your computer on.

## Comparison: Local vs Streamlit Cloud

| Aspect | Local (Batch File) | Streamlit Cloud |
|--------|-------------------|-----------------|
| Cost | Free | Free |
| 24/7 Running | Need computer on | Yes, automatic |
| Sharing | Only local network | Anyone with URL |
| Updates | Manual restart | Auto on GitHub push |
| Best For | Personal use | Portfolio/Demo |

## Recommended Setup

**For this app**: Use Streamlit Cloud because:
- It's free
- 24/7 uptime
- Easy to share
- Professional URL
- Perfect for portfolio projects

---

**Questions?**

Check:
1. Streamlit Docs: https://docs.streamlit.io
2. GitHub Guides: https://guides.github.com
3. Common Issues: https://share.streamlit.io/docs/troubleshooting

**Need help with GitHub?**
Follow this guide step-by-step: https://docs.github.com/en/get-started
