#!/bin/bash

if test "$TRAVIS_SECURE_ENV_VARS" = "true" -a "$TRAVIS_BRANCH" = "master";
then
  openssl aes-256-cbc -K $encrypted_4f8d155c2793_key -iv $encrypted_4f8d155c2793_iv -in opengisch_rsa.enc -out ~/.ssh/id_rsa -d;
  chmod 600 ~/.ssh/id_rsa;
  git config --global user.email "info@opengis.ch";
  git config --global user.name "opengisch";
  git config --global push.default simple;
fi
