if exists("g:switch_background")
    finish
endif

let g:switch_background = 1

func! EZSetBackground()
  let l:main_background = "light"
  let l:other_background = "dark"
  let l:start = g:ez_sunrise
  let l:end = g:ez_sunset

  let l:H = str2nr(strftime("%H"))
  if l:H >= l:start && l:H < l:end
    let &background = l:main_background
  else
    let &background = l:other_background
  endif

  " Schedule next background change.
  let l:M = str2nr(strftime("%M"))
  let l:S = str2nr(strftime("%S"))

  let l:dS = 60 - l:S
  let l:dM = 60 - l:M - 1
  let l:dH = 0
  if l:H < l:start
    let l:dH = l:start - l:H - 1
  elseif l:H < l:end
    let l:dH = l:end - l:H - 1
  else
    let l:dH = 24 - l:H - 1 + l:start
  endif
  let l:dT = l:dS * 1000
  let l:dT += l:dM * 60 * 1000
  let l:dT += l:dH  * 60 * 60 * 1000
  call timer_start(l:dT, {timer -> execute("call EZSetBackground()", "")})
endfunc

call EZSetBackground()
