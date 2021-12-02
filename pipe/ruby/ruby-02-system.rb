#!/usr/bin/ruby
# http://blog.bigbinary.com/2012/10/18/backtick-system-exec-in-ruby.html

path    = __dir__+ "/../assets"
cmdin   = 'conky -c ' + path + '/conky.lua'
cmdout  = 'less' # or 'dzen2'
cmd     = cmdin + ' | ' + cmdout

system(cmd)
