-- vim: ts=4 sw=4 noet ai cindent syntax=lua

--[[
Conky, a system monitor, based on torsmo
]]

conky.config = {
    out_to_x = false,
    out_to_console = true,
    short_units = true,
    update_interval = 1
}

--[[
Common Variables
]]

-- base color
-- escape hash (#) character in conky with slash (\#)
colWhite = '\\#ffffff'
colBlack = '\\#000000'

-- also using google material
-- https://material.io/guidelines/style/color.html
colRed500    = '\\#f44336'
colYellow500 = '\\#ffeb3b'
colBlue500   = '\\#2196f3'
colGrey500   = '\\#9e9e9e'
colGreen500  = '\\#4caf50'
colPink500   = '\\#e91e63'
colOrange500 = '\\#ff9800'
colIndigo500 = '\\#3f51b5'
colCyan500   = '\\#00bcd4'

-- http://fontawesome.io/
FontAwesome = '^fn(FontAwesome-9)'

-- icon 
preIcon  = '^fg(' .. colYellow500 .. ')' .. FontAwesome
postIcon = '^fn()^fg()'

-- glyph icon decoration
decoPath = 'Documents/standalone/dzen2/assets/xbm'

-- diagonal corner
decoCornerTopLeft     = '^i(' .. decoPath .. '/dc-024-tl.xbm)'
decoCornerTopRight    = '^i(' .. decoPath .. '/dc-024-tr.xbm)'
decoCornerBottomLeft  = '^i(' .. decoPath .. '/dc-024-bl.xbm)'
decoCornerBottomRight = '^i(' .. decoPath .. '/dc-024-br.xbm)'

-- single arrow and double arrow
decoSingleArrowLeft  = '^i(' .. decoPath .. '/sa-024-l.xbm)'
decoSingleArrowRight = '^i(' .. decoPath .. '/sa-024-r.xbm)'
decoDoubleArrowLeft  = '^i(' .. decoPath .. '/da-024-l.xbm)'
decoDoubleArrowRight = '^i(' .. decoPath .. '/da-024-r.xbm)'

--[[
Segment
]]

-- date
dateIcon     = ' ' .. preIcon .. '' .. postIcon .. ' '
datePre      = '^bg(' .. colIndigo500 .. ')'
    .. '^fg(' .. colYellow500 .. ')'
dateCommand  = '^fg(' .. colWhite .. ')${time %a %b %d} '
datePost     = '^bg()^fg()'

dateDecoPre  = '^bg(' .. colIndigo500 .. ')'
    .. '^fg(' .. colWhite .. ')' .. decoCornerTopLeft
dateDecoPost = '^bg(' .. colWhite .. ')'
    .. '^fg(' .. colIndigo500 .. ')' .. decoCornerBottomLeft

dateText     = dateDecoPre .. datePre .. dateIcon 
    .. dateCommand .. datePost .. dateDecoPost

-- time
timeIcon     = ' ' .. preIcon .. '' .. postIcon .. ' '
timePre      = '^bg(' .. colPink500 .. ')'
timeCommand  = '^fg(' .. colWhite .. ')${time %H:%M:%S} '
timePost     = '^bg()'

timeDecoPre  = '^bg(' .. colWhite .. ')'
    .. '^fg(' .. colPink500 .. ')' .. decoDoubleArrowLeft
timeDecoPost = '^bg(' .. colWhite .. ')'
    .. '^fg(' .. colPink500 .. ')' .. decoDoubleArrowRight

timeText     = timeDecoPre .. timePre .. timeIcon 
    .. timeCommand .. timePost .. timeDecoPost

--[[
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
]] .. dateText .. [[\
  \
]] .. timeText ..[[\
]]
