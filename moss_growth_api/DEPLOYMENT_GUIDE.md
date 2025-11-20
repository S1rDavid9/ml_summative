# ============================================================================
# DEPLOYMENT GUIDE - MOSS GROWTH PREDICTION API ON RENDER
# ============================================================================

## 📋 PREREQUISITES
- GitHub account
- Render account (free tier available at https://render.com)
- Your project pushed to a GitHub repository

---

## 🚀 STEP-BY-STEP DEPLOYMENT INSTRUCTIONS

### STEP 1: PREPARE YOUR PROJECT FOR DEPLOYMENT

1. **Ensure all files are in the `moss_growth_api` folder:**
   - main.py
   - predict.py
   - requirements.txt
   - best_model.pkl
   - scaler.pkl
   - model_info.json

2. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Add FastAPI deployment files"
   git push origin main
   ```

---

### STEP 2: CREATE A NEW WEB SERVICE ON RENDER

1. **Log in to Render:**
   - Go to https://dashboard.render.com
   - Sign up or log in

2. **Create New Web Service:**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub repository

3. **Configure the service:**
   - **Name**: `moss-growth-api` (or your preferred name)
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: `moss_growth_api`
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```
     pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```
     uvicorn main:app --host 0.0.0.0 --port $PORT
     ```

4. **Set Environment Variables (Optional):**
   - Click "Advanced"
   - Add any environment variables if needed
   - PORT is automatically set by Render

5. **Choose Plan:**
   - Select "Free" for testing
   - Or choose a paid plan for production

6. **Deploy:**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes first time)

---

### STEP 3: VERIFY DEPLOYMENT

1. **Check deployment status:**
   - Monitor the deployment logs in Render dashboard
   - Look for "API is ready to accept requests" message

2. **Test the API:**
   - Once deployed, Render will provide a URL like:
     `https://moss-growth-api.onrender.com`
   
3. **Access documentation:**
   - Visit: `https://your-app-name.onrender.com/docs`
   - This opens the interactive Swagger UI

4. **Check health endpoint:**
   - Visit: `https://your-app-name.onrender.com/health`
   - Should return status "healthy"

---

### STEP 4: CONFIGURE CUSTOM DOMAIN (OPTIONAL)

1. **In Render Dashboard:**
   - Go to your service settings
   - Click "Custom Domain"
   - Follow instructions to add your domain

---

## 🔧 TROUBLESHOOTING

### Issue: Deployment fails during build
**Solution**: 
- Check build logs for specific error
- Ensure requirements.txt is correct
- Verify Python version compatibility

### Issue: Model files not found
**Solution**: 
- Ensure .pkl files are committed to git
- Check if files are in .gitignore
- Verify Root Directory setting in Render

### Issue: API returns 500 errors
**Solution**: 
- Check application logs in Render
- Verify model files loaded correctly
- Test /health endpoint for details

### Issue: Slow cold starts (Free tier)
**Solution**: 
- Free tier spins down after inactivity
- First request after idle may be slow (30-60s)
- Consider upgrading to paid tier for always-on service

---

## 📊 MONITORING

1. **View Logs:**
   - Go to Render dashboard
   - Click on your service
   - View "Logs" tab for real-time logging

2. **Metrics:**
   - Monitor response times
   - Track error rates
   - Check memory usage

---

## 🔄 UPDATING YOUR API

1. **Make changes locally:**
   ```bash
   # Edit your code
   git add .
   git commit -m "Update API"
   git push origin main
   ```

2. **Automatic deployment:**
   - Render automatically detects changes
   - Rebuilds and redeploys your service
   - Monitor deployment in dashboard

---

## 💰 PRICING NOTES

**Free Tier:**
- 750 hours/month
- Spins down after 15 minutes of inactivity
- Slower performance
- Good for development/testing

**Starter Tier ($7/month):**
- Always on
- Better performance
- Custom domains
- Good for production

---

## 🔐 SECURITY BEST PRACTICES

1. **Never commit sensitive data:**
   - Use environment variables for secrets
   - Add .env to .gitignore

2. **CORS Configuration:**
   - In production, replace ["*"] with specific domains:
     ```python
     allow_origins=["https://yourfrontend.com"]
     ```

3. **Rate Limiting:**
   - Consider adding rate limiting for production
   - Use slowapi or similar libraries

---

## 📝 ADDITIONAL NOTES

- **Free tier limitations**: Service spins down after inactivity
- **Wake-up time**: First request after idle ~30-60 seconds
- **Logs retention**: Free tier keeps logs for 7 days
- **SSL/HTTPS**: Automatically provided by Render
- **Auto-scaling**: Available on paid tiers

---

## ✅ POST-DEPLOYMENT CHECKLIST

- [ ] API is accessible at Render URL
- [ ] /docs endpoint shows Swagger UI
- [ ] /health endpoint returns "healthy"
- [ ] /predict endpoint accepts and returns predictions
- [ ] Logs show successful model loading
- [ ] Error handling works correctly
- [ ] CORS works if testing from frontend

---

**Need Help?**
- Render Documentation: https://render.com/docs
- FastAPI Documentation: https://fastapi.tiangolo.com
- GitHub Issues: Check your repository's issues page

---

**Your API will be live at:**
`https://[your-service-name].onrender.com`

**Replace [your-service-name] with the name you chose during setup.**
