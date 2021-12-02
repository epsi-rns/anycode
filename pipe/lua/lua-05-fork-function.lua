#!/usr/bin/lua

-- luaposix available in AUR
local posix = require "posix"

-- https://github.com/luaposix/luaposix
-- $ sudo luarocks install luaposix

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- helper

function sleep (n)
    local t = os.clock()
    while os.clock() - t <= n do
        -- nothing
    end
end

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- application related function

function get_dzen2_parameters ()
    local xpos    = '0'
    local ypos    = '0'
    local width   = '640'
    local height  = '24'
    local fgcolor = '#000000'
    local bgcolor = '#ffffff'
    local font    = '-*-fixed-medium-*-*-*-12-*-*-*-*-*-*-*'

    local parameters = ""
        .. " -x "..xpos.." -y "..ypos
        .. " -w "..width.." -h "..height
        .. " -fn '"..font.."'"
        .. " -ta c -bg '"..bgcolor.."' -fg '"..fgcolor.."'"
--      .. " -title-name dzentop"

    return parameters
end

function generated_output (process)
    local timeformat = '%a %b %d %H:%M:%S'

    while true do
        local datestr = os.date(timeformat).."\n"
        process:write(datestr)
        process:flush()

        sleep(1)
    end
end

function run_dzen2 ()
    local cmdout  = 'dzen2 ' .. get_dzen2_parameters()
    local pipeout = assert(io.popen(cmdout, 'w'))
    
    generated_output(pipeout)
    
    pipeout:close()
end


function detach_dzen2()
    local pid = posix.fork()

    if pid == 0 then -- this is the child process
        run_dzen2()
    else             -- this is the parent process
        -- nothing
    end
end

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- main

-- remove all dzen2 instance
os.execute('pkill dzen2')

-- run process in the background
detach_dzen2()
