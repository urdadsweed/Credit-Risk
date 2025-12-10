# Credit Risk Assessment Calculator

A professional, mathematical formula-based credit risk calculator designed for Indian banking standards.

## Features

- Auto-calculating DTI Ratio - Automatically calculates Debt-to-Income based on income and loan amount
- Flexible Input Values - Accept any decimal number (e.g., 13245464, 1.99%, 14.5754%)
- Dark/Light Mode - Toggle between themes with saved preference
- Professional Design - Sophisticated, English-only interface
- RBI Compliant - Uses mathematical formulas based on Indian banking standards
- Real-time Calculation - Instant DTI updates as you type

## How to Run

### Option 1: Quick Start (Manual)

1. Double-click `start_app.bat` 
2. Wait for the terminal to show "Running on http://localhost:8501"
3. Open browser to `http://localhost:8501`

### Option 2: Auto-Start on Boot (24/7)

1. Right-click `setup_auto_start.bat`
2. Select **"Run as Administrator"**
3. Click "Yes" when prompted
4. App will now start automatically every time Windows boots

To disable auto-start later:
- Open Windows Task Scheduler
- Find "CreditRiskApp"
- Right-click and delete

## Features Explained

### Auto-Calculate DTI
- The **Debt-to-Income (DTI)** field updates automatically
- Formula: `(Monthly Loan Amount ÷ Monthly Income)`
- Shows real-time calculation as you change values
- Cannot be manually edited (read-only)

### Any Number Format
- Income: 13245464, 500000.50, etc.
- Loan Amount: 999999, 1000000.75, etc.
- Interest Rate: 1.99%, 14.5754%, 8.25%, etc.
- No restrictions on decimal places or step values

### Dark/Light Mode
- Click "Dark Mode" button (top-right) to toggle
- Your preference is saved automatically

### Mathematical Scoring
The calculator uses 10 factors based on RBI guidelines:
1. Age (Risk: <25 or >60 years)
2. Annual Income (Minimum threshold: ₹150K)
3. CIBIL Credit Rating (750-900 = Excellent)
4. Debt-to-Income Ratio (<50% is RBI guideline)
5. Employment Stability (Years in current job)
6. Payment History (Late payments count)
7. Active Accounts (Fewer is better)
8. Savings Buffer (Emergency fund)
9. Loan-to-Value Ratio (Loan vs annual income)
10. Interest Rate Acceptance

**Risk Score Scale: 0-100**
- **0-20**: Excellent (Best rates available)
- **21-35**: Good (Easy approval)
- **36-50**: Average (Higher interest rates)
- **51-70**: Fair (Stricter conditions)
- **71-100**: Poor (Difficulty getting loans)

## Files in This Folder

- `app.py` - Flask backend server
- `templates/index.html` - Web interface
- `start_app.bat` - Quick-start script (double-click to run)
- `setup_auto_start.bat` - Set up auto-start on Windows boot
- `requirements.txt` - Python dependencies

## Troubleshooting

### "Unable to connect to server" error
- Make sure `start_app.bat` or `app.py` is running
- Check that port 8501 is not blocked
- Refresh browser page (Ctrl+R)

### DTI not calculating
- Make sure you're entering valid numbers
- Try changing the Loan Amount or Income field
- Check browser console for errors (F12 → Console)

### Port 8501 already in use
Edit `app.py` and change this line:
```python
app.run(debug=False, host='0.0.0.0', port=8502, threaded=True)
```
Use port 8502 (or any free port) instead

## Support

For issues or feature requests, contact the development team.

---

**Version**: 1.0  
**Last Updated**: December 2025
