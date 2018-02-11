#!/usr/bin/lua

local dirname  = debug.getinfo(1).source:match("@?(.*/)")
local path     = dirname .. "../assets"
local cmdin    = 'conky -c ' .. path .. '/conky.lua'
local cmdout   = 'less' -- or 'dzen2'

local pipein  = assert(io.popen(cmdin,  'r'))
local pipeout = assert(io.popen(cmdout, 'w'))
  
for line in pipein:lines() do
    pipeout:write(line.."\n")
    pipeout:flush()
end -- for loop
   
pipein:close()
pipeout:close()
