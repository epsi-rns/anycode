#!/usr/bin/lua

-- luaposix available in AUR
local posix = require "posix"

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

function get_lemon_parameters ()
    -- geometry: -g widthxheight+x+y
    local xpos     = '0'
    local ypos     = '0'
    local width    = '640'
    local height   = '24'

    local geom_res = width .. 'x' .. height
           .. '+' .. xpos  .. '+' .. ypos

    -- color, with transparency
    local fgcolor  = "'#000000'"
    local bgcolor  = "'#aaffffff'"

    -- XFT: require lemonbar_xft_git 
    local font     = "monospace-9"

    -- finally
    local parameters = ""
        .. " -g "..geom_res.." -u 2"
        .. " -B "..bgcolor.." -F "..fgcolor
        .. " -f "..font

    return parameters
end

function generated_output (process)
    local dirname  = debug.getinfo(1).source:match("@?(.*/)")
    local path     = dirname .. "../assets"
    local cmdin    = 'conky -c ' .. path .. '/conky.lua'
    
    local pipein  = assert(io.popen(cmdin,  'r'))
  
    for line in pipein:lines() do
        process:write(line.."\n")
        process:flush()
    end -- for loop
   
    pipein:close()
end

function run_lemon ()
    local cmdout  = 'lemonbar ' .. get_lemon_parameters()
    local pipeout = assert(io.popen(cmdout, 'w'))
    
    generated_output(pipeout)
    
    pipeout:close()
end


function detach_lemon()
    local pid = posix.fork()

    if pid == 0 then -- this is the child process
        run_lemon()
    else             -- this is the parent process
        -- nothing
    end
end

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- main

-- remove all lemonbar instance
os.execute('pkill lemonbar')

-- run process in the background
detach_lemon()
