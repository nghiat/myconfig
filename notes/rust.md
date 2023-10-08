.lvimrc
```
let g:rooter_patterns = ['.lvimrc']

noremap <F9> :terminal cargo build<CR>

set tags+=d:/projects/tags/rust_tags
set tags+=C:/Users/trant/.cargo/registry/src/tags

if executable('rust-analyzer')
  au User lsp_setup call lsp#register_server({
        \   'name': 'Rust Language Server',
        \   'cmd': {server_info->['rust-analyzer']},
        \   'whitelist': ['rust'],
        \   'initialization_options': {
        \     'cargo': {
        \       'buildScripts': {
        \         'enable': v:true,
        \       },
        \     },
        \     'linkedProjects': [
        \       'D:\projects\Hanoi\Cargo.toml',
        \     ],
        \     'procMacro': {
        \       'enable': v:true,
        \     },
        \   },
        \ })
endif

```
