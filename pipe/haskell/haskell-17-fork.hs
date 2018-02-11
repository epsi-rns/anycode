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
cmdout = "lemonbar"

-- Source directory is irrelevant in Haskell
-- but we'll do it anyway for the sake of learning
wConkyFileName :: String -> String
wConkyFileName dirName = dirName ++ "/../assets" ++ "/conky.lua"

getLemonParameters :: [String]
getLemonParameters = [
      "-g", geom_res,  "-u", "2",
      "-B", bgcolor, "-F", fgcolor,
      "-f", font
    ]
  where
    -- geometry: -g widthxheight++y
    xpos     = "0"
    ypos     = "0"
    width    = "640"
    height   = "24"

    geom_res = width ++ "x" ++ height
            ++ "+" ++ xpos ++ "+" ++ ypos

    -- color, with transparency    
    fgcolor  = "#000000"
    bgcolor  = "#aaffffff"

    -- XFT: require lemonbar_xft_git 
    font     = "monospace-9"

wSleep :: Int -> IO ()
wSleep mySecond = threadDelay (1000000 * mySecond)

detachLemon :: IO ()
detachLemon = do
    dirName <- getCurrentDirectory
    let conkyFileName = wConkyFileName dirName  

    (_, Just pipeout, _, _) <- 
        createProcess (proc cmdin ["-c", conkyFileName])
        { std_out = CreatePipe } 

    (_, _, _, ph)  <- 
        createProcess (proc cmdout getLemonParameters) 
        { std_in = UseHandle pipeout }
      
    hClose pipeout

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- main

main = do
    -- remove all lemonbar instance
    system "pkill lemonbar"

    -- run process in the background
    detachLemon

    -- end of IO
    return ()
