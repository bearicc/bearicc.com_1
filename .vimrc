set nocompatible
set ai ts=4 sts=4 et sw=4
set nobackup nowritebackup noswapfile
set nu
syntax on

" resize current buffer by +/- 5
nnoremap <C-left> :vertical resize -5<cr>
nnoremap <C-down> :resize +5<cr>
nnoremap <C-up> :resize -5<cr>
nnoremap <C-right> :vertical resize +5<cr>

" vundle
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'tpope/vim-pathogen'
Plugin 'Raimondi/delimitMate'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'kien/ctrlp.vim'
Plugin 'bling/vim-airline'
Plugin 'scrooloose/syntastic'
Plugin 'tomtom/tcomment_vim'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'mhinz/vim-startify'
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'mattn/emmet-vim'
Plugin 'nanotech/jellybeans.vim'
call vundle#end()
filetype plugin indent on

" pathogen
call pathogen#infect()

" YouCompleteMe
let g:ycm_collect_identifiers_from_tags_files = 1 " Let YCM read tags from Ctags file
let g:ycm_use_ultisnips_completer = 1 " Default 1, just ensure
let g:ycm_seed_identifiers_with_syntax = 1 " Completion for programming language's keyword
let g:ycm_complete_in_comments = 1 " Completion in comments
let g:ycm_complete_in_strings = 1 " Completion in string
let g:ycm_global_ycm_extra_conf = '/home/bear/.vim/bundle/.ycm_extra_conf.py'

" UltiSnips
let g:UltiSnipsExpandTrigger       = "<c-j>"
let g:UltiSnipsJumpForwardTrigger  = "<c-j>"
let g:UltiSnipsJumpBackwardTrigger = "<c-p>"
let g:UltiSnipsListSnippets        = "<c-k>" "List possible snippets based on current file

" syntastic
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list            = 1
let g:syntastic_check_on_open            = 1
let g:syntastic_check_on_wq              = 0

" TComment
nmap <leader>c :TComment<CR>
nmap <leader>= :TCommentBlock<CR>
vmap <leader>c :TComment<CR>
vmap <leader>= :TCommentBlock<CR>

" indent guides
let g:indent_guides_enable_on_vim_startup=1
let g:indent_guides_start_level = 2
let g:indent_guides_guide_size  = 1
let g:indent_guides_auto_colors = 0
let g:indent_guides_exclude_filetypes = ['help', 'nerdtree', 'startify']
autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  guibg = blue ctermbg  = 3
autocmd VimEnter,Colorscheme * :hi IndentGuidesEven guibg = green ctermbg = 4
hi IndentGuidesOdd  guibg = blue  ctermbg = 3
hi IndentGuidesEven guibg = green ctermbg = 4

" taglist
nnoremap <silent> <F8> :TlistToggle<CR>
let Tlist_File_Fold_Auto_Close = 1
let Tlist_Use_Right_Window = 1
let Tlist_Use_SingleClick = 1

" NERDTree
map <C-n> :NERDTreeTabsToggle<CR>
"let g:nerdtree_tabs_open_on_console_startup = 1
let g:NERDTreeMouseMode = 2
" Get both NERDTree and Startify working at startup
autocmd VimEnter *
    \   if !argc()
    \ |   Startify
    \ |   NERDTree
    \ |   wincmd w
    \ | endif

" vim-airline
set laststatus=2

" startify
let g:startify_custom_header = split(system('cowsay "Hello, BEAR!"'), '\n') + ['','']

set guifont=Monospace\ Bold\ 12
if has('gui_running')
    colorscheme jellybeans
    set lines=999 columns=999
    let Tlist_Auto_Open = 1
endif
