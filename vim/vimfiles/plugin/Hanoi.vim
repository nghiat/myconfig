function! s:SetupHanoiServer()
  let fullPath = expand('%')
  let currParent = fnamemodify(fullPath, ':h')
  let projectRoot = ''
  let markers = [ '.git', '.gutctags' ]
  while 1
    for marker in markers
      if !empty(glob(currParent .. '/' .. marker))
        let projectRoot = currParent
        break
      endif
    endfor
    let newParent = fnamemodify(currParent, ':p:h')
    if newParent == currParent
      break
    else
      let currParent = newParent
    endif
  endwhile

  if len(projectRoot)
    let output = system('cmd.exe /C start /MIN D:/projects/Hanoi/target/debug/Hanoi.exe --mode=server --root=' .. projectRoot)
  endif
endfunction

autocmd BufNewFile,BufReadPost *  call s:SetupHanoiServer()
