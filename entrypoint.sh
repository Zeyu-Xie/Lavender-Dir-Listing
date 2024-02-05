#!/bin/sh -l

mkdir -p /_site_Lavender_Dir_Listing

python /main.py $1

cp -R /_site_Lavender_Dir_Listing /github/workspace/_site_Lavender_Dir_Listing

rm -R /github/workspace/*

cp -R /_site_Lavender_Dir_Listing/* /github/workspace/

ls -R /github/workspace