#!/usr/bin/lua

local timeformat = '%a %b %d %H:%M:%S'

function sleep (n)
    local t = os.clock()
    while os.clock() - t <= n do
        -- nothing
    end
end

while true do
    print(os.date(timeformat))
    sleep(1)
end
