#!/usr/bin/lua

local timeformat = '%a %b %d %H:%M:%S'

function sleep (n)
    local t = os.clock()
    while os.clock() - t <= n do
        -- nothing
    end
end

local cmdout   = 'less' -- or 'dzen2'
local pipeout = assert(io.popen(cmdout, 'w'))

while true do
    local datestr = os.date(timeformat).."\n"
    pipeout:write(datestr)
    pipeout:flush()
    
    sleep(1)
end

pipeout:close()
