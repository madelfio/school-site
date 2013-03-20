Title: How to add OAuth to a Node.js app using Passport
Date: 2013-03-15 16:19
Summary:
Slug: node-auth
Category: Notes

I want to have usernames and sessions in some node.js apps.  Here's how I set
it up using [Passport][1] (which has a user guide, but does not seem to have a
cookbook-like tutorial for getting everything set up).

## Install

First install Passport and the Google "Strategy" (not a fan of this name):

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

#### App.js

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




[1]: http://passportjs.org/
