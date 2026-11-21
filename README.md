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

## Deploy with Firebase Hosting
One-time setup (needs Node.js):

```bash
npm install -g firebase-tools
firebase login
firebase use --add        # pick your Firebase project; creates .firebaserc
```

Share a preview link (expires after 7 days by default):

```bash
firebase hosting:channel:deploy preview
```

Publish to the live site:

```bash
firebase deploy --only hosting
```

## Notes
- The contact form currently opens the visitor's email app (`mailto:`). It is not stored anywhere.
  Hooking it to Firebase (Firestore + email) is the next step.
