-- vim: ts=4 sw=4 noet ai cindent syntax=lua

--[[
Conky, a system monitor, based on torsmo
]]

conky.config = {
    out_to_x = false,
    out_to_console = true,
    short_units = true,
    update_interval = 1
}--[[
Execute Conky
]]

-- Lua Function Demo 
-- https://github.com/brndnmtthws/conky/issues/62

function exec(command)
    local file = assert(io.popen(command, 'r'))
    local s = file:read('*all')
    file:close()

    s = string.gsub(s, '^%s+', '') 
    s = string.gsub(s, '%s+$', '') 
    s = string.gsub(s, '[\n\r]+', ' ')

    return s
end


function gototopleft()
  return exec('tput cup 0 0') 
end

conky.text = gototopleft() .. [[\
${time %a %b %d %H:%M:%S}\
]]





