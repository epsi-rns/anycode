#!/usr/bin/ruby

def get_lemon_parameters()
  # geometry: -g widthxheight+x+y
  xpos    = '0'
  ypos    = '0'
  width   = '640'
  height  = '24'

  geom_res = "#{width}x#{height}+#{xpos}+#{ypos}"

  # color, with transparency
  fgcolor = "'#000000'"
  bgcolor = "'#aaffffff'"

  # XFT: require lemonbar_xft_git
  font  = "monospace-9"

  parameters  = " -g #{geom_res} -u 2" \
                " -B #{bgcolor} -F #{fgcolor}" \
                " -f #{font}"
end

def generated_output(stdin)
  path    = __dir__+ "/../assets"
  cmdin   = 'conky -c ' + path + '/conky.lua'
    
  IO.popen(cmdin, "r") do |f| 
    while f do
      stdin.puts f.gets
    end
    f.close()    
  end
end

def run_lemon()
  cmdout  = 'lemonbar ' + get_lemon_parameters()
  IO.popen(cmdout, "w") do |f| 
    generated_output(f) 
        
    f.close()    
  end
end

def detach_lemon()
  # warning: Signal.trap is application wide
  Signal.trap("PIPE", "EXIT")
    
  pid = fork { run_lemon() }
  Process.detach(pid)
end

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
system('pkill lemonbar')

# run process in the background
detach_lemon()
