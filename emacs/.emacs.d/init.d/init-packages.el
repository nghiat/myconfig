(if (getenv "http_proxy")
    ;; Use local mirror
    (progn
      (unless (file-directory-p "~/.emacs.d/mirror-elpa")
	((let ((default-directory "~/.emacs.d"))
           (shell-command-to-string "git clone https://github.com/d12frosted/elpa-mirror"))))
      (setq package-archives '(("melpa" . "~/.emacs.d/mirror-elpa/melpa/")
                               ("gnu"   . "~/.emacs.d/mirror-elpa/gnu/"))))
  (setq package-archives '(("melpa" . "https://melpa.org/packages/")
                           ("melpa-stable" . "https://stable.melpa.org/packages/")
                           ("gnu"   . "https://elpa.gnu.org/packages/"))))

;; Install 'use-package' if necessary
(package-initialize)
(unless (and (package-installed-p 'use-package)
             (package-installed-p 'general))
  (package-refresh-contents)
  (package-install 'use-package)
  (package-install 'general))

;; Enable use-package
(require 'use-package)
(setq use-package-always-ensure t)

(require 'general)
;; Global bindings
(general-define-key
 :states '(normal visual)
 :prefix "SPC"
 "o" 'mode-line-other-buffer
 "s" 'ff-get-other-file
 "f" 'format-code
 "h" 'windmove-left
 "j" 'windmove-down
 "k" 'windmove-up
 "l" 'windmove-right
 "wc" 'delete-window
 "wo" 'delete-other-windows
 "bd" 'kill-this-buffer)

(use-package auctex
  :mode ("\\.tex\\'" . TeX-latex-mode)
  :hook
  (LaTeX-mode . (lambda()
                  (auto-fill-mode 1)
                  (setq fill-column 80)))
  :init
  ;; https://stackoverflow.com/questions/9534239/emacs-auctex-latex-syntax-prevents-monospaced-font
  ;; Only change sectioning color
  (setq font-latex-fontify-sectioning 'color)
  ;; super-/sub-script on baseline
  (setq font-latex-script-display (quote (nil)))
  ;; Do not change super-/sub-script font
  (custom-set-faces
   '(font-latex-subscript-face ((t nil)))
   '(font-latex-superscript-face ((t nil))))
  ;; Exclude bold/italic from keywords
  (setq font-latex-deactivated-keyword-classes
        '("italic-command" "bold-command" "italic-declaration" "bold-declaration")))

(use-package clang-format
  :hook
  ((c-mode c++-mode) . (lambda()  (fset 'format-code 'clang-format-region))))

(use-package cmake-mode
  :mode ("CMakeLists.txt" "\\.cmake\\'"))

(use-package cquery
  :commands lsp-query-enable
  :hook
  ((c-mode c++-mode) . (lambda()
                         (condition-case nil
                             (lsp-cquery-enable)
                           (user-error nil)))))

(use-package column-enforce-mode
  :defer 5
  :config
  (global-column-enforce-mode t))

(use-package counsel
  :general
  ("M-x" 'counsel-M-x)
  (:states '(normal visual)
           :prefix "SPC"
            "cg" 'counsel-ag
            "e" 'counsel-find-file
            "r" 'counsel-recentf)
  :config
  (use-package flx)
  (use-package smex
    :config
    (smex-initialize)))

(use-package evil
  :config
  (evil-mode 1)
  (fset 'evil-visual-update-x-selection 'ignore)
  (setq evil-symbol-word-search t)
  (setq evil-want-fine-undo t)
  (setq undo-tree-enable-undo-in-region nil)
  :hook
  ((c++-mode gn-mode LaTeX-mode). (lambda () (setq evil-shift-width 2))))

(use-package evil-visualstar
  :after evil
  :config
  (global-evil-visualstar-mode))

(use-package flycheck
  :defer t
  :hook
  (python-mode . (lambda()
                   (flycheck-mode 1)
                   (if (eq system-type 'windows-nt)
                       (setq flycheck-python-flake8-executable "python.exe")
                     (setq flycheck-python-flake8-executable "python3")))))

(use-package gn-mode
  :load-path "init.d"
  :mode ("BUILD.gn" "\\.gni\\'"))

(use-package ivy
  :general
  (:states '(normal visual)
           :prefix "SPC"
           ";" 'ivy-switch-buffer)
  :config
  (ivy-mode 1)
  (setq enable-recursive-minibuffers t)
  (setq ivy-use-virtual-buffers t))

(use-package ivy-xref
  :after lsp-mode
  :init
  (setq xref-show-xrefs-function #'ivy-xref-show-xrefs))

(use-package json-mode
  :mode "\\.json\\'"
  :hook
  (json-mode . (lambda()
                 (fset 'format-code 'json-reformat-region)
                 (make-local-variable 'js-indent-level)
                 (setq js-indent-level 2))))

(use-package lsp-mode
  :defer t
  :disabled t)

(use-package lua-mode
  :mode "\\.lua\\'"
  :interpreter "lua")

(use-package magit
  :general
  (:states '(normal visual)
           :prefix "SPC"
           "vc" 'magit-commit
           "vd" 'magit-diff-buffer-file
           "vf" 'magit-pull
           "vp" 'magit-push
           "vs" 'magit-status))

(use-package projectile
  :defer t
  :pin melpa-stable
  :general
  (:states '(normal visual)
           :prefix "SPC"
           "p" '(:keymap projectile-command-map))
  :config
  (projectile-mode)
  (setq projectile-indexing-method 'alien)
  (setq projectile-enable-caching t)
  (use-package counsel-projectile
    :config
    (counsel-projectile-mode)))

(use-package qml-mode
  :mode "\\.qml\\'"
  :config
  (autoload 'qml-mode "qml-mode" "Editing Qt Declarative." t))

(use-package swiper
  :general
  (:states '(normal visual)
           :prefix "SPC"
           "/" 'swiper))

(use-package web-beautify
  :hook
  ((js2-mode js-mode json-mode) . (lambda()  (fset 'format-code 'web-beautify-js)))
  (sgml-mode . (lambda()  (fset 'format-code 'web-beautify-html)))
  (css-mode . (lambda()  (fset 'format-code 'web-beautify-css))))

(use-package yapfify
  :hook
  (python-mode . (lambda()  (fset 'format-code 'yapfify-region))))

(provide 'init-packages)
