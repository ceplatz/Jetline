# Jetline Training — website redesign concept

Static, responsive redesign of the Jetline Training site (white + vibrant blue), built from the
content and branding of jetline-training.com. Type ratings are the hero; line training is a
secondary, newer offering.

```
public/          <- what gets deployed
  index.html     <- the whole site (HTML + CSS + a little JS)
  assets/        <- logo and optimised photos
firebase.json    <- Firebase Hosting config
```

## Preview locally
Open `public/index.html` in a browser. No build step.

## Firebase (project: `jetline-training`)

One-time setup in the [Firebase console](https://console.firebase.google.com/project/jetline-training):
1. **Add a Web app** (Project settings → Your apps → `</>`). Hosting then serves the project config
   at `/__/firebase/init.json`, which the contact form uses. No keys are stored in this repo.
2. **Create a Firestore database** (Build → Firestore Database → production mode, pick a region, e.g. `eur3`).

Then, with Node.js installed:

```bash
npm install -g firebase-tools
firebase login
firebase deploy --only firestore:rules,hosting
```

Share a preview link instead of going live (expires after 7 days by default):

```bash
firebase hosting:channel:deploy preview
```

Note: the contact form saves to Firestore only on a Firebase-hosted URL (live or preview channel).
Opened locally, it falls back to preparing an email to info@jetline-training.com.

## Contact form
- Submissions are stored in the Firestore collection `enquiries` (read them in the console).
- `firestore.rules` lets visitors create an enquiry (validated fields and sizes, server timestamp)
  but never read, change or delete one. A hidden honeypot field catches simple bots.
- **Email notifications (optional):** on the Blaze plan, install the *Trigger Email from Firestore*
  extension (or a small Cloud Function) to email each new enquiry to Jetline.
- Stronger spam protection: add Firebase App Check (reCAPTCHA) when going live.
