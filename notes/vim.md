# .gutctags
```
-R
--languages=C++,C#
#Enable parsing function declarations
--kinds-C++=+p
--exclude=ThirdParty
--exclude=Intermediate
--exclude-exception=*PS4\*
```

# .lvimrc
```
if &ft == "lua"
  setlocal noexpandtab
elseif &ft == "cpp"
  setlocal expandtab
endif

set tags+=C:/Program\\\ Files/Epic\\\ Games/UE_4.24/Engine/Source/tags
noremap <F9> :terminal ++shell ninja64.exe -C d:/projects/ngen/out/debug dx12_sample<CR>
inoremap <F9> <C-O>:terminal ++shell ninja64.exe -C d:/projects/ngen/out/debug dx12_sample<CR>
```


# Misc
Type this to open font popup:  
set guifont=*

H move to top of screen  
M - move to middle of screen  
L - move to bottom of screen  
w - jump forwards to the start of a word  
W - jump forwards to the start of a word (words can contain punctuation)  
e - jump forwards to the end of a word  
E - jump forwards to the end of a word (words can contain punctuation)  
b - jump backwards to the start of a word  
B - jump backwards to the start of a word (words can contain punctuation)  

register % - current file name  
^ fist non-blank  
:ab - add abbreviation  
