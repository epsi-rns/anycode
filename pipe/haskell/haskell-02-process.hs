import System.Process
import System.Directory

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- wrap Funktion

-- Source directory is irrelevant in Haskell
-- but we'll do it anyway for the sake of learning
wConkyFileName :: String -> String
wConkyFileName dirName = dirName ++ "/../assets" ++ "/conky.lua"

cmdin  = "conky"
cmdout = "less" -- or dzen2

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- main

main = do
    dirName <- getCurrentDirectory
    let conkyFileName = wConkyFileName dirName   
  
    (_, Just pipeout, _, _) <- 
        createProcess (proc cmdin ["-c", conkyFileName])
        { std_out = CreatePipe } 

    (_, _, _, ph)  <- 
        createProcess (proc cmdout []) 
        { std_in = UseHandle pipeout }
    
    -- just remove this waitForProcess line to detach dzen2
    _ <- waitForProcess ph

    putStr ""
  


