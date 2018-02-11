import System.Process
import System.Directory

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- wrap Funktion

-- source directory is irrelevant in Haskell
-- but we'll do it anyway for the sake of learning
wGetCmdIn :: String -> String
wGetCmdIn dirname = "conky -c " 
    ++ dirname ++ "/../assets" ++ "/conky.lua"

cmdout = "less" -- or dzen2

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- main

main = do
    dirname <- getCurrentDirectory
    let cmdin = wGetCmdIn dirname
    system $ cmdin ++ " | " ++ cmdout
  


