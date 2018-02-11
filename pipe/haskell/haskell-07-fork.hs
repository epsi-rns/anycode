import System.Process
import System.Directory
import System.IO
import System.Posix.Process
import System.Posix.Types

import Control.Concurrent
import Control.Monad

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- wrap Funktion

cmdin  = "conky"
cmdout = "dzen2"

-- Source directory is irrelevant in Haskell
-- but we'll do it anyway for the sake of learning
wConkyFileName :: String -> String
wConkyFileName dirName = dirName ++ "/../assets" ++ "/conky.lua"

getDzen2Parameters :: [String]
getDzen2Parameters = [
      "-x", xpos,  "-y", ypos,
      "-w", width, "-h", height,
      "-fn", font,
      "-ta", "c",
      "-bg", bgcolor,
      "-fg", fgcolor       --,
--    "-title-name", "dzentop"
    ]
  where    
    xpos    = "0"
    ypos    = "0"
    width   = "640"
    height  = "24"
    fgcolor = "#000000"
    bgcolor = "#ffffff"
    font    = "-*-fixed-medium-*-*-*-12-*-*-*-*-*-*-*"

wSleep :: Int -> IO ()
wSleep mySecond = threadDelay (1000000 * mySecond)

detachDzen2 :: IO ()
detachDzen2 = do
    dirName <- getCurrentDirectory
    let conkyFileName = wConkyFileName dirName  

    (_, Just pipeout, _, _) <- 
        createProcess (proc cmdin ["-c", conkyFileName])
        { std_out = CreatePipe } 

    (_, _, _, ph)  <- 
        createProcess (proc cmdout getDzen2Parameters) 
        { std_in = UseHandle pipeout }
      
    hClose pipeout

detachTransset :: IO ProcessID
detachTransset = forkProcess $ do    
    wSleep 1
    system "transset .8 -n dzentop >/dev/null"
    return ()

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- main

main = do
    -- remove all dzen2 instance
    system "pkill dzen2"

    -- run process in the background
    detachDzen2

    -- optional transparency
    -- detachTransset
    
    return ()
