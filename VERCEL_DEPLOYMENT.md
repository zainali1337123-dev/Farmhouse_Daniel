# Farmhouse Application - Vercel Deployment Guide

## Prerequisites
- Vercel account (https://vercel.com)
- GitHub account with your repository connected

## Deployment Steps

### 1. Connect Your Repository to Vercel
```bash
# Visit https://vercel.com/new
# Select your GitHub repository
# Click "Import"
```

### 2. Configure Environment Variables (if needed)
In Vercel dashboard → Project Settings → Environment Variables, add:
- `STREAMLIT_SERVER_HEADLESS`: `true`
- `STREAMLIT_SERVER_PORT`: `8501`

### 3. Deploy
```bash
# Vercel will automatically detect and deploy
# Check Vercel dashboard for deployment status
```

### 4. View Your App
- Your app will be available at: `https://your-project-name.vercel.app`

## Important Notes

⚠️ **Streamlit Limitations on Vercel:**
- First load may take 10-30 seconds (cold start)
- Supabase connection must be properly configured
- Session state persists during the request lifecycle
- Database writes should be optimized for serverless

## Local Testing
```bash
# Test locally before pushing to Vercel
streamlit run app.py
```

## Troubleshooting

**If deployment fails:**
1. Check Vercel logs: `vercel logs`
2. Ensure all dependencies are in `requirements.txt`
3. Verify Supabase credentials in `.streamlit/secrets.toml`
4. Check that all imports are correct

**For database issues:**
- Make sure Supabase URL and key are in secrets
- Test Supabase connection locally first

## Contact & Support
For issues, check:
- Streamlit docs: https://docs.streamlit.io
- Vercel docs: https://vercel.com/docs
