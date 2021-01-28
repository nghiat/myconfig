#b::
  Run, "chrome.exe"
  Return
#c::
  Run, "code.exe"
  Return
#d::
  Run, "Everything.exe"
  Return
#m::
  Run, "runemacs.exe"
  Return
#Return::
  Run, "cmd.exe" /c start /max cmd.exe
  Return
#x::
  Run, "cmd.exe" /c start /max gvim.exe
  Return
