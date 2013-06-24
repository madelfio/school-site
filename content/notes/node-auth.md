Title: How to add OAuth to a Node.js app using Passport
Date: 2013-03-15 16:19
Summary:
Slug: node-auth
Category: Notes
Status: draft

I want to have usernames and sessions in some node.js apps.  Here's how I set
it up using [Passport][1] (which has a user guide, including a [section on
Google OpenID][2], but does not seem to have a cookbook-like tutorial for getting
everything set up).

## Install

First install Passport and the Google "Strategy" (not a fan of this name).
You can install other strategies from the list here if you have other OpenID
endpoints to use:

    :::console
    $ npm install passport passport-google

## Files

You will be editing app.js and adding several files to your app:

    :::console
    ./my-app
    ├── app.js  (Modify existing)
    ├── auth.js
    ├── public
    │   └── images
    │       └── google.png
    └── views
        ├── login.ejs
        └── unauthorized.ejs

### app.js

In app.js, we (1) require auth.js:

    :::javascript
    var fs = require('fs'),
        express = require('express'),
        ...
        /* Authentication */
        auth = require('./auth');

(2) initialize it:

    :::javascript
    app.use(auth.initialize());
    app.use(auth.session());
    app.use(auth.setup());

(3) add routes:

    :::javascript
    app.get('/auth/google', auth.google('/login'));
    app.get('/auth/google/return', auth.google_return('/', '/login'));
    app.get('/logout', auth.logout());
    app.get('/unauthorized', auth.unauthorized());

(4) require authentication for some pages (if necessary):

    :::javascipt
    /* existing routes */
    app.get('/some_page', auth.check(), some_route_func);


### auth.js

We put all the real logic and interface with passport and passport-google in
auth.js.

    :::javascript
    var passport = require('passport'),
        GoogleStrategy = require('passport-google');

    var returnURL = 'http://example.com/auth/google/return',
        realm = 'http://example.com/',
        goog_auth_settings = {returnURL: returnURL, realm: realm},
        authHandler = function(identifier, profile, done) {
          process.nextTick(function() {
            profile.identifier = identifier;
            return done(null, profile);
          }
        };
    passport.serializeUser(function(user, done) {done(null, user);});
    passport.deserializeUser(function(obj, done) {done(null, obj);});
    passport.use(new GoogleStrategy(goog_auth_settings, authHandler));

    exports.initialize = passport.initialize;
    exports.session = passport.session;

    exports.setup = function() {
      return function(req, res) {
        res.locals.user = req.user || '';
        return next();
      };
    };

    exports.google = 










First, require passport, passport-google (or other strategies), and the
soon-to-be-created `auth.js`:

    :::javascript
    var fs = require('fs'),
        express = require('express'),
        ...
        /* Authentication */
        passport = require('passport'),
        GoogleStrategy = require('passport-google'),
        auth = require('./auth');

You need to enable the GoogleStrategy by adding this before setting up Express
to use Passport.  This simply saves the username in profile.identifier and
does not persist it to storage:

    :::javascript
    var returnURL = 'http://example.com/auth/google/return',
        realm = 'http://example.com/',
        goog_auth_settings = {returnURL: returnURL, realm: realm},
        authHandler = function(identifier, profile, done) {
          process.nextTick(function() {
            profile.identifier = identifier;
            return done(null, profile);
          }
        };
    passport.serializeUser(function(user, done) {done(null, user);});
    passport.deserializeUser(function(obj, done) {done(null, obj);});
    passport.use(new GoogleStrategy(goog_auth_settings, authHandler));

Add these lines to enable passport, after a call to
`app.use(express.session())` (Marco: is `express.session()` required?):

    :::javascript
    app.use(passport.initialize());
    app.use(passport.session());
    app.use(auth.setup);

Then add these among/after your routes:

    :::javascript
    app.get('/auth/google',
      passport.authenticate('google', {failureRedirect: '/site/login'});
    );

    app.get('/auth/google/return',
      passport.authenticate('google', {
        successReturnToOrRedirect: '/site/',
        failureRedirect: '/site/login'
      }),
      function(req, res) {res.redirect('/site/');}
    );

    app.get('/logout', auth.logout);
    app.get('/unauthorized', auth.unauthorized);


[1]: http://passportjs.org/
[2]: http://passportjs.org/guide/google/
