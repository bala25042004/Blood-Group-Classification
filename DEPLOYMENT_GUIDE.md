# Railway Deployment Guide for Blood Group Prediction App

## Prerequisites
- Git installed
- Railway account (sign up at https://railway.app)
- Docker installed locally (optional, for testing)

## Project Status
✅ Project cleaned and optimized for deployment (~11MB)
✅ Dockerfile configured for Railway
✅ Railway configuration file created (railway.json)
✅ App updated to use environment variables

## Deployment Steps

### Step 1: Prepare Your Project
The project has been cleaned and optimized:
- Removed unnecessary model files (train locally)
- Removed test images and large assets
- Updated app.py for Railway deployment
- Configured Dockerfile for Railway

### Step 2: Push to GitHub
1. Create a new repository on GitHub
2. Initialize git in your project folder:
   
```
   git init
   git add .
   git commit -m "Prepare for Railway deployment"
   
```
3. Add your GitHub repository:
   
```
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   
```

### Step 3: Deploy on Railway
1. Go to https://railway.app and sign in
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will auto-detect the Dockerfile
6. Click "Deploy"

### Step 4: Environment Variables (Optional)
If needed, set these in Railway dashboard:
- `SECRET_KEY`: Your secret key for sessions
- `PORT`: Will be auto-set by Railway

### Step 5: Access Your App
Once deployed, Railway will provide a URL like:
`https://your-app-name.railway.app`

## Important Notes

### Model Training
Since the free tier has limited resources:
1. **Train locally first** - Train your model on your local machine with your dataset
2. **Upload trained model** - Add the trained model files to your project:
   - `trained_model.h5`
   - `scaler.pkl`
   - `encoder.pkl`
3. **Deploy** - Push to Railway

### For Local Training
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `python app.py`
3. Upload a CSV dataset through the /train route
4. The model will be saved locally
5. Add those files to your GitHub repo

## Free Tier Limits
- 500 hours of execution per month
- $5 credit per month
- 1 GB database storage
- Sleeps after 5 minutes of inactivity ( wakes on request)

## Troubleshooting
If deployment fails:
1. Check Railway logs in dashboard
2. Ensure Dockerfile is correct
3. Verify requirements.txt has correct versions
4. Make sure port is set to 5000

## Files Structure
```
Blood Eye Project/
├── app.py              # Main Flask application
├── Dockerfile          # Docker configuration
├── railway.json        # Railway config
├── requirements.txt    # Python dependencies
├── feature_Code_fundus.py  # Fundus feature extraction
├── feature_Code_scelera.py # Sclera feature extraction
├── templates/          # HTML templates
├── static/            # CSS, JS, uploads
└── uploads/           # User uploads directory
