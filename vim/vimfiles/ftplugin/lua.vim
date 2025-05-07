function! LuaScopeStart()
  let l:currentScopeIndent = indent('.')
  let l:lnum = line('.') - 1 " Skip the current line
  while l:lnum > 0
    let l:line = getline(l:lnum)
    if l:line =~ '\v(<function>|<if>|<for>|<while>|<do>|<repeat>|<else>|<elseif>)' && (l:currentScopeIndent == 0 || indent(l:lnum) < l:currentScopeIndent)
      " Save to jumplist
      execute 'normal! ' . l:lnum . 'G'
      return
    endif
    if l:currentScopeIndent == 0
      let l:currentScopeIndent = indent(l:lnum)
    endif
    let l:lnum -= 1
  endwhile
endfunction

function! LuaScopeEnd()
  let l:currentScopeIndent = indent('.')
  echom l:currentScopeIndent
  let l:lnum = line('.') + 1 " Skip the current line
  let l:max = line('$')
  let l:depth = 0
  while l:lnum <= l:max
    let l:line = getline(l:lnum)
    if l:line =~ '\v(<end>|<else>|<elseif>)' && (l:currentScopeIndent == 0 || indent(l:lnum) < l:currentScopeIndent)
      " Save to jumplist
      execute 'normal! ' . l:lnum . 'G'
      return
    endif
    if l:currentScopeIndent == 0
      let l:currentScopeIndent = indent(l:lnum)
    endif
    let l:lnum += 1
  endwhile
endfunction

" Map the keys in normal mode
nnoremap [[ :call LuaScopeStart()<CR>
nnoremap ]] :call LuaScopeEnd()<CR>
