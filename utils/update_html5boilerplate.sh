#!/bin/bash

set -o errexit
set -o nounset

HERE=`dirname $0`
APP=`python -c "import os,sys;print os.path.abspath(os.path.join('$HERE','../flasktool/templates/apps/'))"`/static
STATIC="$APP/static"

curl -fsSL 'http://github.com/paulirish/html5-boilerplate/zipball/v2.0' -o BOIL
unzip -q BOIL

command rm -rf $STATIC
mv paulirish* $STATIC
rm BOIL

cat << EOF $STATIC/README.rst
How To Use html5boilerplate (with flask)
==========================================

http://html5boilerplate.com/docs/Home

In particular, this adaptation keeps the 'build' 
stuff around, so 'ant build' if necessary to get
minified js and styles, which will end up in the 
'static' directory.  YOU WILL NEED TO MOVE THEM
'up' a directory.  

EOF


cat << EOF
1) new files were updated and moved into "$STATIC"
2) use "git status" to see the new files, and make updates as you see fit.
   git ls-files -d might help here.
3) Update "$APP/templates/base.html" to new version of jquery and modernizer
4) rm $STATIC/*html  # after working them into base.html, they are superfluous.
5) rm $STATIC/static # after making any changes you want to make here.

`git status`

EOF

