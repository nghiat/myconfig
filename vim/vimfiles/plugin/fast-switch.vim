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

    if has("win32")
      let slash = '\'
    else
      let slash = '/'
    endif
    let pairs = [
      \[ "Public", "Private"],
      \[ "Classes", "Private"],
      \[ "Classes" . slash . "Engine", "Private"],
      \[ "Classes" . slash . "GameFramework", "Private"],
      \[ "Classes" . slash . "GameFramework", "Private" . slash . "Components"],
      \]
    for pair in pairs
      for i in [0, 1]
        let folder1 = pair[i]
        let folder2 = pair[1 - i]
        let folder1Slashed = slash . folder1 . slash
        let folder2Slashed = slash . folder2 . slash
        " Read substitute docs
        " Don't ask me why we need 8 slashes
        let folder1DoubleSlashed = substitute(folder1Slashed, "\\\\", "\\\\\\\\", "g")
        let folder2DoubleSlashed = substitute(folder2Slashed, "\\\\", "\\\\\\\\", "g")
        if stridx(a:fullPathWithoutExt, folder1Slashed) > -1
          for toExt in a:toExts
            let otherFile = substitute(a:fullPathWithoutExt, folder1DoubleSlashed, folder2DoubleSlashed, "") . toExt
            if filereadable(otherFile)
              execute 'edit' otherFile
              return 1
            endif
          endfor
        endif
      endfor
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
