if exists("g:fast_switch")
    finish
endif

let g:fast_switch = 1

function! s:FastSwitchFrom(fullPathWithoutExt, ext, fromExts, toExts)
  if index(a:fromExts, a:ext) >= 0
    for toExt in a:toExts
      let otherFile = a:fullPathWithoutExt . toExt
      if filereadable(otherFile)
        execute 'edit' otherFile
        return 1
      endif
    endfor
  endif
  return 0
endfunction

function! s:FastSwitchBetween(fullPathWithoutExt, ext, exts1, exts2)
  if s:FastSwitchFrom(a:fullPathWithoutExt, a:ext, a:exts1, a:exts2)
    return 1
  elseif s:FastSwitchFrom(a:fullPathWithoutExt, a:ext, a:exts2, a:exts1)
    return 1
  endif
  return 0
endfunction

function! FastSwitch()
  let fullPath = expand('%:p')
  let ext = expand("%:e")
  let fullPathWithoutExt = substitute(fullPath, '\.' . ext, '\.', "")
  if s:FastSwitchBetween(fullPathWithoutExt, ext, ["c", "cpp", "cc", "m", "mm"], ["h", "hpp"])
    return
  elseif s:FastSwitchBetween(fullPathWithoutExt, ext, ["inl"], ["h", "hpp"])
    return
  elseif s:FastSwitchBetween(fullPathWithoutExt, ext, ["html"], ["js"])
    return
  endif
endfunction

comm FastSwitch call FastSwitch()
