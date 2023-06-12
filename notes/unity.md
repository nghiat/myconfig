Ctags
```
dotnet tool install ilspycmd -g
ilspycmd -o d:\projects\tags\unity -p Unity.InputSystem.dll
```

.lvimrc
```
set shiftwidth=4
set tabstop=4
set softtabstop=4

noremap <F9> :terminal ++shell "C:/Program Files/Microsoft Visual Studio/2022/Community/MSBuild/Current/Bin/MSBuild.exe" D:/projects/Unity1/Assembly-CSharp.csproj<CR>
inoremap <F9> <C-O>:terminal ++shell "C:/Program Files/Microsoft Visual Studio/2022/Community/MSBuild/Current/Bin/MSBuild.exe" D:/projects/Unity1/Assembly-CSharp.csproj<CR>

set tags+=d:/projects/tags/unity_tags
```
