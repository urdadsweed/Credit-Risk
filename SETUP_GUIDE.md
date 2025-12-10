# Credit Risk Assessment Calculator - Complete Setup Guide

## Quick Start (Choose One)

### Option A: Run Locally (On Your Computer)
```bash
cd "C:\Users\AVISHKAR LOKHANDE\Desktop\credit_risk_app"
streamlit run streamlit_app.py
```
Then open: http://localhost:8502

**Pros:** Works immediately, no setup  
**Cons:** Need to keep computer running, not shareable online

---

### Option B: Deploy to Streamlit Cloud (RECOMMENDED - FREE & 24/7)

Follow: `STREAMLIT_DEPLOYMENT.md` in this folder

**Pros:** 
- FREE
- 24/7 automatic 
- Share with anyone via URL
- Professional domain
- Auto-updates on code push

Takes 5 minutes to set up!

---

## What's in This Folder?

```
credit_risk_app/
├── streamlit_app.py          ← Main app (pure Python!)
├── requirements.txt          ← Dependencies for Streamlit Cloud
├── app.py                    ← Old Flask version (optional)
├── .gitignore               ← For GitHub
├── README.md                ← Full documentation
├── QUICK_REFERENCE.txt      ← Quick startup
├── STREAMLIT_DEPLOYMENT.md  ← Deploy to cloud
├── start_app.bat            ← Local start script
└── templates/               ← Old HTML files
```

---

## Fixed in Streamlit Version

- **Interest Rate** - Now accepts ANY decimal (1.99, 14.5754, 8.125, etc.)  
- **All Amounts** - Accept any number (13245464, 999999, 500000.50, etc.)  
- **Auto-Calculate DTI** - Shown with formula breakdown  
- **Pure Python** - No HTML/JavaScript issues  
- **Beautiful UI** - Streamlit handles styling  
- **Mobile Responsive** - Works on phone too  

---

## Streamlit vs Flask

| Feature | Streamlit | Flask |
|---------|-----------|-------|
| Language | Pure Python | Python + HTML/JS |
| Setup | 1 file | Multiple files |
| Deployment | Click "Deploy" | Complex setup |
| 24/7 Hosting | Free (Cloud) | Need paid server |
| Mobile Ready | Yes | Need CSS tweaks |
| Maintenance | Low | High |

**Verdict**: Streamlit is much better for this project!

---

## 3-Step Cloud Deployment

### 1. Create GitHub Account
Go to https://github.com → Sign up

### 2. Push Your Code to GitHub
```bash
cd "C:\Users\AVISHKAR LOKHANDE\Desktop\credit_risk_app"
git init
git add .
git commit -m "Credit Risk App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/credit-risk-app.git
git push -u origin main
```

### 3. Deploy to Streamlit Cloud
Go to https://share.streamlit.io → Click "New app" → Select your repo

**Done!** Your app is now live 24/7 at:
```
https://credit-risk-app.streamlit.app
```

---

## Key Features

### Auto-Calculating DTI
- Shows: `₹ Monthly Loan ÷ ₹ Monthly Income = DTI`
- Updates instantly as you change values
- Formula-based, no manual calculation needed

### Any Number Format
- Income: 13245464, 500000.5, 123456.789
- Loan: 999999, 1000000.75, 2500000
- Interest: 1.99%, 14.5754%, 8.125%
- No validation errors!

### 10-Factor Mathematical Score
1. Age
2. Annual Income
3. CIBIL Credit Rating
4. Debt-to-Income Ratio
5. Employment Stability
6. Payment History
7. Number of Accounts
8. Savings Buffer
9. Loan-to-Value Ratio
10. Interest Rate Acceptance

**Risk Score**: 0-100 (lower is better)

---

## Ratings Explained

| Score | Rating | Status | Meaning |
|-------|--------|--------|------------|
| 0-20 | Excellent | Best | Best rates available |
| 21-35 | Good | Good | Easy loan approval |
| 36-50 | Average | Fair | Higher interest rates |
| 51-70 | Fair | Poor | Stricter conditions |
| 71-100 | Poor | Critical | Difficult to get loans |

---

## Local Running

### Start App
```bash
streamlit run streamlit_app.py
```

### Access
```
http://localhost:8502
```

### Stop App
Press `Ctrl+C` in terminal

---

## Next Steps

1. **Test Locally First**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Deploy to Cloud**
   - Follow `STREAMLIT_DEPLOYMENT.md`
   - Get a public URL

3. **Share**
   - Send URL to anyone
   - No installation needed on their end

---

## Cost Breakdown

| Option | Setup | Monthly Cost | 24/7 |
|--------|-------|-------------|------|
| Local (Batch File) | Free | Free | ❌ (Need PC on) |
| Local (Task Scheduler) | Free | Free | Yes (But PC must be on) |
| **Streamlit Cloud** | **Free** | **FREE** | **Yes Always on** |
| Heroku (paid) | Free | $7-50 | Yes |
| AWS | Free tier | Free* | Yes |

**Recommendation**: Streamlit Cloud (completely free, always running)

---

## Documentation

- **Full Docs**: `README.md`
- **Quick Start**: `QUICK_REFERENCE.txt`
- **Deployment**: `STREAMLIT_DEPLOYMENT.md`
- **This File**: Complete setup guide

---

## Checklist

- [ ] Run `streamlit run streamlit_app.py` locally
- [ ] Test all features (change income, loan, etc.)
- [ ] Create GitHub account
- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Deploy to Streamlit Cloud
- [ ] Share URL with others
- [ ] Monitor app in Streamlit Cloud dashboard

---

## Quick Troubleshooting

**"Module not found"**
```bash
pip install streamlit pandas
```

**"Port already in use"**
```bash
streamlit run streamlit_app.py --server.port 8503
```

**"DTI not calculating"**
- Change the Income or Loan Amount field
- Check browser console (F12) for errors

**"Interest rate showing error"**
- This is fixed in Streamlit version!
- Try: 1.99, 14.5754, 8.5, etc.

---

## Support Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **GitHub Help**: https://docs.github.com
- **Python Basics**: https://python.org/docs
- **Common Issues**: https://share.streamlit.io/docs/troubleshooting

---

**Ready to deploy?**

Follow `STREAMLIT_DEPLOYMENT.md` for free 24/7 hosting!

